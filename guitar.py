from notes import chromatic_notes

def check_if_string(string, no_of_strings=6):
    assert (string >= 1 and string <= no_of_strings), "invalid string number"

def standard_tuning(string_choice):
    check_if_string(string_choice, 6)
    strings = [ "E", "B", "G", "D", "A", "E"]
    return strings[string_choice-1]

def notes_on_string(string_choice, max_fret=19):
    note_list = chromatic_notes()
    elems = len(note_list)

    start_note = standard_tuning(string_choice)
    start = note_list.index(start_note)
    end = start + max_fret+1

    string_notes = [note_list[n%elems] for n in range(start, end)]
    return string_notes

if __name__ == "__main__":
    pass