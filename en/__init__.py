import os, subprocess

# Would be nice to get these from a config file
root = "{}/notes".format(os.getenv("HOME"))
editor = os.getenv("EDITOR", "vim")
core = "core"
extension = ".md"
# Set this to something not weird by default...
catTitleTemplate = "/bin/zsh -c 'echo \"\e[3m{}\e[23m\"'"

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
    subprocess.call(command)

def getText(note):
    return open(path(note)).read()

def separator():
    return "-" * int(subprocess.check_output(["stty", "size"]).split()[1])

def display(note):
    text = ""
    print()
    try:
        text = getText(note)
    except FileNotFoundError:
        print("Couldn't find note: ", end="", flush=True)
    subprocess.call(catTitleTemplate.format(note), shell=True)
    print("{}\n{}".format(separator(), text))

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
    return (stripExtension(file) for file in os.listdir(root) if
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

def rename(old, new):
    if not old or not new:
        print("Nothing to rename...\n")
    else:
        try:
            os.rename(path(old), path(new))
        except FileNotFoundError:
            print("File not found...\n")
    return getNotes()

def delete(note):
    if not note:
        print("Nothing to delete...\n")
        return
    try:
        os.remove(path(note))
    except FileNotFoundError:
        print("File not found...\n")
