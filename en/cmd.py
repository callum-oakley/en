from sys import argv
from en import output, edit, cat, filterNotes, search, find, append, delete

def head(args):
    if args:
        return args[0]
    return None

def help(command):
    if command == None:
        print("""
usage: en <command> [args]

Available commands are as follows (in both long and short form):

open        o  Open the specified note(s) with $EDITOR
cat         c  Print the content of the specified note(s) to stdout
list        l  List the notes with names that contain the provided string
list-open   lo As above, but open the matching notes for editing
list-cat    lc As above, but print the content of the matching notes to stdout
search      s  List the notes with content that contains the provided string
search-open so As above, but open the matching notes for editing
search-cat  sc As above, but print the content of the matching notes to stdout
find        f  List the union of the results of list and search
find-open   fo As above, but open the matching notes for editing
find-cat    fc As above, but print the content of the matching notes to stdout
append      a  Append a line to the specified note
append-cat  ac As above, then prints the content of the updated note to stdout
delete         Delete the specified note (no short option, to minimise mistakes)
help        h  Print this help text to stdout, or examples for specific commands""")
    elif command == "open" or command == "o":
        print("""
en open <note>
    opens <note> with $EDITOR

en open <note1> <note2> ... <noteN>
    opens <note1> <note2> ... <noteN> with $EDITOR

en open
    opens core with $EDITOR""")
    elif command == "cat" or command == "c":
        print("""
en cat <note>
    prints the content of <note> to stdout

en cat <note1> <note2> ... <noteN>
    prints the content of <note1>, <note2>, ... <noteN> all to stdout

en cat
    prints the content of core to stdout""")
    else:
        print("Help text not found...")

def main():
    if len(argv) <= 1:
        help(None)
        return
    command, args = argv[1], argv[2:]
    if command == "open" or command == "o":
        edit(args)
    elif command == "cat" or command == "c":
        cat(args)
    elif command == "list" or command == "l":
        output(filterNotes(args))
    elif command == "list-open" or command == "lo":
        edit(filterNotes(args))
    elif command == "list-cat" or command == "lc":
        cat(filterNotes(args))
    elif command == "search" or command == "s":
        output(search(args))
    elif command == "search-open" or command == "so":
        edit(search(args))
    elif command == "search-cat" or command == "sc":
        cat(search(args))
    elif command == "find" or command == "f":
        output(find(args))
    elif command == "find-open" or command == "fo":
        edit(find(args))
    elif command == "find-cat" or command == "fc":
        cat(find(args))
    elif command == "append" or command == "a":
        append(head(args), head(args[1:]))
    elif command == "append-cat" or command == "ac":
        cat(append(head(args), head(args[1:])))
    # No short option to guard against accidental deletion
    elif command == "delete":
        delete(head(args))
        output(filterNotes([]))
    elif command == "help" or command == "h":
        help(head(args))
    else:
        print("Command not recognised...\n")
        help(None)
