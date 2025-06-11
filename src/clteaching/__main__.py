"""Command line management."""

import argparse
from pathlib import Path

from clteaching import cli


def main() -> None:
    """Parse command line arguments and execute."""
    parser = argparse.ArgumentParser(
        prog="Command Line Teaching",
        description="Create a course, add a module, or upload a module.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase verbosity level",
        action="count",
        default=0,
    )
    parser.add_argument("-t", "--test-run", help="test the action", action="store_true")
    subparsers = parser.add_subparsers(dest="action", required=True)
    parser_newcourse = subparsers.add_parser("newcourse", help="create new course")
    parser_newcourse.set_defaults(func=cli.newcourse)
    parser_addmod = subparsers.add_parser("addmod", help="add module to course")
    parser_addmod.set_defaults(func=cli.addmod)
    parser_upmod = subparsers.add_parser("upmod", help="upload module to Canvas")
    parser_upmod.set_defaults(func=cli.upmod)
    parser.add_argument("name", help="name of the course or module")
    args = parser.parse_args()
    if args.action == "upmod":
        args.func(Path(args.name), args.verbose, args.test_run)
    else:
        args.func(Path(args.name), args.verbose)


if __name__ == "__main__":
    main()
