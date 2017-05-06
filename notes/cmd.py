from sys import argv
from notes import default, edit, list, find

def main():
    if len(argv) <= 1:
        default()
        return
    command, args = argv[1], argv[2:]
    if command == "open" or command == "o":
        edit(args)
    elif command == "list" or command == "l":
        if args:
            list(args[0])
        else:
            list()
    elif command == "find" or command == "f":
        if args:
            find(args[0])
        else:
            list()
    else:
        print("Command not recognised")
