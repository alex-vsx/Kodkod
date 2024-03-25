import re
import sys


def main() -> int:

    with open(".git/COMMIT_EDITMSG", 'r') as file:
        first_line = file.readline().strip()
    # Define the regex pattern for checking the commit message
    pattern = r'^(\[\w{9}\])+ (feat|chore|fix|ci|refactor|test|style|build|docs)(\(\w*\))?!?: .'
    if not re.match(pattern, first_line):
        print("Commit message should have ClickUp ticket id and types(feat|chore|fix|ci|refactor|test|style|build|docs).", file=sys.stderr)
        print("Please follow https://www.conventionalcommits.org/en/v1.0.0/", file=sys.stderr)
        print("Required format:", file=sys.stderr)
        print("    [ticketid] feat: commit message", file=sys.stderr)
        print("    [ticketid] feat!: breaking change", file=sys.stderr)
        print("    [ticketid] docs(api): commit message", file=sys.stderr)
        print("    [ticketid][ticketid] feat: multiple ticket id", file=sys.stderr)
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
