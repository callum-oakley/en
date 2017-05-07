from sys import argv
from en import default, edit, list, find, cat, output

def head(args):
    if args:
        return args[0]
    return None

def main():
    if len(argv) <= 1:
        default()
        return
    command, args = argv[1], argv[2:]
    if command == "open" or command == "o":
        edit(args)
    elif command == "cat" or command == "c":
        cat(args)
    elif command == "list" or command == "l":
        output(list(head(args)))
    elif command == "find" or command == "f":
        output(find(head(args)))
    elif command == "list-open" or command == "lo":
        edit(list(head(args)))
    elif command == "list-cat" or command == "lc":
        cat(list(head(args)))
    elif command == "find-open" or command == "fo":
        edit(find(head(args)))
    elif command == "find-cat" or command == "fc":
        cat(find(head(args)))
    else:
        print("Command not recognised")

# TODO append, prepend lines from single command
# TODO help text
# TODO readme
# TODO publish to pypi
