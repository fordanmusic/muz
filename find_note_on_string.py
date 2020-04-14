import argparse
from guitar import notes_on_string
from translate_enharmonic import translate_enharmonic


def find_note_on_string(note_to_find, string_choice, threshold=0):
    note_list = notes_on_string(string_choice)
    if note_to_find in note_list:
        fret = note_list.index(note_to_find)
        if fret >= threshold:
            return fret
        else:
            return fret+12
    else:
        translated = translate_enharmonic(note_to_find)
        if translated in note_list:
            fret = note_list.index(translated)
            if fret >= threshold:
                return fret
            else:
                return fret+12


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find note on guitar string. Returns fret position.')
    parser.add_argument("note_to_find", type=str)
    parser.add_argument("string_choice", type=int)
    #parser.add_argument("threshold", type=int)
    args = parser.parse_args()

    print(find_note_on_string(args.note_to_find, args.string_choice))
