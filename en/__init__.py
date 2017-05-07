from os import getenv, listdir
from subprocess import call, check_output

# Would be nice to get these from a config file
root = "{}/notes".format(getenv("HOME"))
editor = getenv("EDITOR", "vim")
core = "core"
extension = ".md"

def default():
    edit([core])

def path(note):
    return "{}/{}.md".format(root, note)

def edit(notes):
    command = [editor]
    for note in notes:
        command.append(path(note))
    call(command)

def separator():
    return "-" * int(check_output(["stty", "size"]).split()[1])

def display(note):
    try:
        print("\n{}\n{}\n{}".format(note, separator(), open(path(note)).read()))
    except FileNotFoundError:
        print("\nCouldn't find note: {}\n{}\n".format(note, separator()))

def cat(notes):
    if not notes:
        notes = [core]
    for note in notes:
        display(note)

def stripExtension(file):
    return file.rpartition(".")[0]

def getNotes():
    notes = []
    for file in listdir(root):
        if file.endswith(extension):
            notes.append(stripExtension(file))
    return notes

def output(notes):
    for note in notes:
        print(note)

def list(pattern):
    if pattern == None:
        pattern = ""
    matches = []
    for note in getNotes():
        if pattern in note:
            matches.append(note)
    return matches

def find(pattern):
    if pattern == None:
        pattern = ""
    matches = []
    for note in getNotes():
        text = open(path(note)).read()
        # Case insensitive search unless there are capitals in pattern
        if pattern.islower():
            text = text.lower()
        if pattern in text:
            matches.append(note)
    return matches
