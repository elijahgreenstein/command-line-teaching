"""Course creation, module creation, and module upload."""

import pathlib

import jinja2

from clteaching import loaders, objects, util


FS = util.FileStructure()


def get_tpl_dict(tpl_path):
    """Load a dictionary of templates."""
    tpl_dict = {}
    course = [FS.cset, FS.qdesc, FS.token]
    mod = [FS.mod / file for file in [FS.mset, FS.intro, FS.quiz, FS.disc]]
    for path in course + mod:
        with open(tpl_path / path, encoding="utf-8") as f:
            tpl_text = f.read()
        tpl_dict[str(path)] = tpl_text
    return tpl_dict


def get_env(tpl_dict):
    """Get environment."""
    return jinja2.Environment(
        loader=jinja2.DictLoader(tpl_dict),
        autoescape=jinja2.select_autoescape,
    )


def get_template_paths(dirname, tpl_path):
    """Get template paths in ``template/dirname``."""
    tpl_dict = get_tpl_dict(tpl_path)
    env = get_env(tpl_dict)
    return env.list_templates(filter_func=lambda x: x.startswith(str(dirname)))


def render_template(tpl_name, variables, tpl_path):
    """Render a template with a dictionary of variables."""
    tpl_dict = get_tpl_dict(tpl_path)
    env = get_env(tpl_dict)
    template = env.get_template(tpl_name)
    return template.render(variables)


def newcourse(name, verb, tpl_path):
    """Create a new course from templates."""
    if name.exists():
        raise FileExistsError(f"'{name}' already exists.")
    user = util.UserInput(name)
    user.get_course_input()
    tpls = get_newcourse(user.course_conf, tpl_path)
    write_newcourse(name, tpls, verb)


def get_newcourse(user_input, tpl_path):
    """Get keyed templates rendered from user input."""
    # Get templates
    tpl_names = get_template_paths(str(FS.course), tpl_path)
    # Render templates
    rendered = {}
    for tpl in tpl_names:
        rendered[tpl] = render_template(tpl, user_input, tpl_path)
    return rendered


def write_newcourse(name, tpls, verb):
    """Write rendered templates to default locations."""
    # Set up logger
    log = util.Logger(verb)
    log.log(1, log.msgs["newcourse"].format(course=name))
    # Make directories
    log.log(1, log.msgs["create_dir"])
    for dname in [name, name / FS.course, name / FS.mod]:
        dname.mkdir()
        log.log(1, log.msgs["create"].format(name=dname))
    # Write files
    log.log(1, log.msgs["create_files"])
    for tpl in tpls:
        with open(name / tpl, "w", encoding="utf-8") as f:
            f.write(tpls[tpl])
        log.log(1, log.msgs["create"].format(name=tpl))


def addmod(name, verb, tpl_path):
    """Add a module with template files."""
    cset = FS.course / "settings.yaml"
    mpath = FS.mod / name
    if cset.exists() and not mpath.exists():
        # Load course settings and get user input
        cset = util.load_yaml(cset)
        user = util.UserInput(name)
        user.get_mod_input()
        # Update user input with times from course settings
        user.add_mod_conf(cset["times"])
        # Get templates and write
        tpls = get_mod_tpls(name, user.mod_conf, tpl_path)
        write_mod(name, tpls, verb)
    elif mpath.exists():
        raise FileExistsError(f"'{name}' already exists.")
    else:
        raise FileNotFoundError(f"No course settings file, '{cset}'.")


def get_mod_tpls(name, user_input, tpl_path):
    """Get keyed templates rendered from user input."""
    # Get templates
    tpl_names = get_template_paths(str(FS.mod), tpl_path)
    # Render templates and change output path in process
    rendered = {}
    for tpl in tpl_names:
        outpath = FS.mod / name / pathlib.Path(tpl).name
        rendered[outpath] = render_template(tpl, user_input, tpl_path)
    return rendered


def write_mod(name, tpls, verb):
    """Write rendered templates to default locations."""
    # Set up logger
    log = util.Logger(verb)
    log.log(1, log.msgs["addmod"].format(mod=name))
    # Make module directory
    log.log(1, log.msgs["create_dir"])
    (FS.mod / name).mkdir()
    log.log(1, log.msgs["create"].format(name=FS.mod / name))
    # Write files
    log.log(1, log.msgs["create_files"])
    for tpl in tpls:
        with open(tpl, "w", encoding="utf-8") as f:
            f.write(tpls[tpl])
        log.log(1, log.msgs["create"].format(name=tpl))


def upmod(name, verb, test):
    """Upload a module to Canvas through API calls."""
    cset = FS.cset
    mpath = FS.mod / name
    if cset.exists() and mpath.exists():
        # Load user, course, and module
        user, crs, mod = load_mod(pathlib.Path("./"), mpath)
        # Run the upload sequence
        results = upload_seq(user, crs, mod, verb, test)
        # Print test results
        if test:
            print("TEST COMPLETE:")
            for rtype in ["module", "items", "moves", "quiz"]:
                for item in results[rtype]:
                    print(item)
    elif not mpath.exists():
        raise FileNotFoundError(f"'{name}' does not exist.")
    else:
        raise FileNotFoundError(f"No course settings file, '{cset}'.")


def load_mod(cpath, mpath):
    """Load User, Course, Module, and all Module items."""
    cset = cpath / FS.cset
    qdesc_path = cpath / FS.qdesc
    user = loaders.load_user(cpath / FS.token)
    qdesc = qdesc_path if qdesc_path.exists() else None
    course = loaders.load_course(cset, qdesc)
    mod = loaders.load_module(mpath, FS.mset, course)
    course.add_mod(mod)
    user.add_course(course)
    return (user, course, mod)


def upload_seq(user, course, module, verb, test):
    """Create Module and upload its content."""
    # Set up logger for verbose output
    log = util.Logger(verb)
    log.log(1, log.msgs["upmod"].format(mod=module.mname))
    # Create module
    log.log(1, log.msgs["upmod_mod"])
    mod_resp = user.create(course, module, test)
    if not test:
        log.log(1, log.msgs["status"].format(status=mod_resp.status_code))
        log.log(2, log.msgs["details"].format(resp=mod_resp.json()))
    mod_resp = [mod_resp]
    # Create items
    item_resp = []
    for item in module.items:
        log.log(1, log.msgs["upmod_item"].format(item=item.title))
        resp = user.create(course, item, test)
        item_resp.append(resp)
        if not test:
            log.log(1, log.msgs["status"].format(status=resp.status_code))
            log.log(2, log.msgs["details"].format(resp=resp.json()))
    # Move items to module
    move_resp = []
    for idx, item in enumerate(module.items):
        log.log(1, log.msgs["upmod_move"].format(item=item.title))
        position = idx + 1
        resp = user.move(course, module, item, position, test)
        move_resp.append(resp)
        if not test:
            log.log(1, log.msgs["status"].format(status=resp.status_code))
            log.log(2, log.msgs["details"].format(resp=resp.json()))
    # Handle quizzes
    quiz_resp = []
    for item in module.items:
        if isinstance(item, objects.Quiz):
            log.log(1, log.msgs["upmod_add_qst"].format(item=item.title))
            resps = user.add_quiz_questions(course, item, test)
            if not test:
                for resp in resps:
                    log.log(1, log.msgs["status"].format(status=resp.status_code))
                    log.log(2, log.msgs["details"].format(resp=resp.json()))
            quiz_resp.append(resps)
            log.log(1, log.msgs["upmod_update_pts"].format(item=item.title))
            resp = user.update_quiz_pts(course, item, test)
            if not test:
                log.log(1, log.msgs["status"].format(status=resp.status_code))
                log.log(2, log.msgs["details"].format(resp=resp.json()))
            quiz_resp.append(resp)

    # Return responses
    return {
        "module": mod_resp,
        "items": item_resp,
        "moves": move_resp,
        "quiz": quiz_resp,
    }
