FILEPATH = "smartlist.txt"


def get_notes(filepath=FILEPATH):
    with open(filepath, 'r') as notes_local:
        notes_local = notes_local.readlines()
    return notes_local


def write_notes(notes_arg, filepath=FILEPATH):
    with open(filepath, 'w') as doc:
        doc.writelines(notes_arg)
