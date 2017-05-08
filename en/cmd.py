import sys
import pkg_resources
from en import (output, edit, cat, getNotesByName, getNotesByContent,
        getNotesByNameOrContent, append, rename, delete)

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
rename      r  Rename a note
delete         Delete the specified note (no short option, to minimise mistakes)
help        h  Print this help text to stdout, or examples for specific commands
version     v  Print version information""")

    elif command in ["open", "o"]:
        print("""
en open <note>
    opens <note> with $EDITOR

en open <note1> <note2> ... <noteN>
    opens <note1> <note2> ... <noteN> with $EDITOR

en open
    opens core with $EDITOR""")

    elif command in ["cat", "c"]:
        print("""
en cat <note>
    prints the content of <note> to stdout

en cat <note1> <note2> ... <noteN>
    prints the content of <note1>, <note2>, ... <noteN> all to stdout

en cat
    prints the content of core to stdout""")

    elif command in ["list", "l"]:
        print("""
en list <pattern>
    lists those notes with names containing <pattern>

en list <pattern1> <pattern2> ... <patternN>
    lists those notes with names containing all of <pattern1>, <pattern2>
    ... <patternN>

en list
    lists the names of every note""")

    elif command in ["list-open", "lo"]:
        print("""
list notes as with the list command, then immediately open them""")

    elif command in ["list-cat", "lc"]:
        print("""
list notes as with the list command, then immediately cat them""")

    else:
        print("Help text not found...")

def main():
    if len(sys.argv) <= 1:
        help(None)
        return
    command, args = sys.argv[1], sys.argv[2:]
    if command in ["open", "o"]:
        edit(args)
    elif command in ["cat", "c"]:
        cat(args)
    elif command in ["list", "l"]:
        output(getNotesByName(args))
    elif command in ["list-open", "lo"]:
        edit(getNotesByName(args))
    elif command in ["list-cat", "lc"]:
        cat(getNotesByName(args))
    elif command in ["search", "s"]:
        output(getNotesByContent(args))
    elif command in ["search-open", "so"]:
        edit(getNotesByContent(args))
    elif command in ["search-cat", "sc"]:
        cat(getNotesByContent(args))
    elif command in ["find", "f"]:
        output(getNotesByNameOrContent(args))
    elif command in ["find-open", "fo"]:
        edit(getNotesByNameOrContent(args))
    elif command in ["find-cat", "fc"]:
        cat(getNotesByNameOrContent(args))
    elif command in ["append", "a"]:
        append(head(args), head(args[1:]))
    elif command in ["append-cat", "ac"]:
        cat(append(head(args), head(args[1:])))
    elif command in ["rename", "r"]:
        output(rename(head(args), head(args[1:])))
    # No short option to guard against accidental deletion
    elif command == "delete":
        delete(head(args))
        output(getNotesByName([]))
    elif command in ["help", "h"]:
        help(head(args))
    elif command in ["version", "v"]:
        print(pkg_resources.require("en")[0].version)
    else:
        print("Command not recognised...\n")
        help(None)
