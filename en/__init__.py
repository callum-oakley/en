from os import getenv, listdir
from subprocess import call

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

def stripExtension(file):
    return file.rpartition(".")[0]

def getNotes():
    notes = []
    for file in listdir(root):
        if file.endswith(extension):
            notes.append(stripExtension(file))
    return notes

def list(pattern=""):
    for note in getNotes():
        if pattern in note:
            print(note)

def find(pattern):
    for note in getNotes():
        text = open(path(note)).read()
        # Case insensitive search unless there are capitals in pattern
        if pattern.islower():
            text = text.lower()
        if pattern in text:
            print(note)

def cat(note):
    print("\n{}\n{}\n{}".format(note, "-" * 80, open(path(note)).read()))
