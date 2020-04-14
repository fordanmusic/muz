import argparse
from notes import check_if_note

def translate_enharmonic(note_name):
    check_if_note(note_name)
    translator = {
        "A#": "Bb",
        "Bb": "A#",
        "B#": "C",
        "Cb": "B",
        "C#": "Db",
        "Db": "C#",
        "D#": "Eb",
        "Eb": "D#",
        "E#": "F",
        "Fb": "E",
        "F#": "Gb",
        "Gb": "F#",
        "G#": "Ab",
        "Ab": "G#",
    }
    return translator.get(note_name, note_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate note to enharmonic equivalent.')
    parser.add_argument("note_name", type=str)
    args = parser.parse_args()

    note = args.note_name
    print(translate_enharmonic(note))