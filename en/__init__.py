from os import getenv, listdir, remove
from subprocess import call, check_output

# Would be nice to get these from a config file
root = "{}/notes".format(getenv("HOME"))
editor = getenv("EDITOR", "vim")
core = "core"
extension = ".md"

def output(notes):
    for note in notes:
        print(note)

def path(note):
    return "{}/{}.md".format(root, note)

def edit(notes):
    if not notes:
        notes = [core]
    command = [editor]
    for note in notes:
        command.append(path(note))
    call(command)

def getText(note):
    return open(path(note)).read()

def separator():
    return "-" * int(check_output(["stty", "size"]).split()[1])

def display(note):
    # The italics here are super non-portable...
    try:
        text = getText(note)
        call("/bin/zsh -c 'echo \"\n\e[3m{}\e[23m\"'".format(note), shell=True)
        print("{}\n{}".format(separator(), text))
    except FileNotFoundError:
        call("/bin/zsh -c $'echo \"\nCouldn\\'t find note: \e[3m{}\e[23m\"'".format(note), shell=True)
        print("{}\n".format(separator()))

def cat(notes):
    if not notes:
        notes = [core]
    for note in notes:
        display(note)

def smartCaseIn(x, y):
    if x.islower():
        y = y.lower()
    return x in y

def stripExtension(file):
    return file.rpartition(".")[0]

def getNotes():
    return (stripExtension(file) for file in listdir(root) if
            file.endswith(extension))

def getNotesByName(patterns):
    return (note for note in getNotes() if
            all(smartCaseIn(pattern, note) for pattern in patterns))

def getNotesByContent(patterns):
    return (note for note in getNotes() if
            all(smartCaseIn(pattern, getText(note)) for pattern in patterns))

def getNotesByNameOrContent(patterns):
    return (note for note in getNotes() if
            all(smartCaseIn(pattern, note) or
                smartCaseIn(pattern, getText(note)) for pattern in patterns))

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
