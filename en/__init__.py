from os import getenv, listdir, remove
from subprocess import call, check_output

# Would be nice to get these from a config file
root = "{}/notes".format(getenv("HOME"))
editor = getenv("EDITOR", "vim")
core = "core"
extension = ".md"

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

def filterNotes(patterns):
    notes = getNotes()
    for pattern in patterns:
        for note in list(notes):
            if pattern not in note:
                notes.remove(note)
    return notes

def search(patterns):
    notes = getNotes()
    for pattern in patterns:
        for note in list(notes):
            text = open(path(note)).read()
            # Case insensitive search unless there are capitals in pattern
            if pattern.islower():
                text = text.lower()
            if pattern not in text:
                notes.remove(note)
    return notes

def find(patterns):
    notes = getNotes()
    for pattern in patterns:
        for note in list(notes):
            text = open(path(note)).read()
            if pattern.islower():
                text = text.lower()
            if pattern not in text and pattern not in note:
                notes.remove(note)
    return notes

def append(note, line):
    if not note:
        print("Nothing to add...")
        return []
    if not line:
        note, line = core, note
    open(path(note), "a").write(line + "\n")
    return [note]

def delete(note):
    if not note:
        print("Nothing to delete...\n")
        return
    try:
        remove(path(note))
    except FileNotFoundError:
        print("File not found...\n")
