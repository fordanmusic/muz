def check_if_note(note_name):
    allowed = { "Ab",
                "A",
                "A#",
                "Bb",
                "B",
                "B#",
                "Cb",
                "C",
                "C#",
                "Db",
                "D",
                "D#",
                "Eb",
                "E",
                "E#",
                "Fb",
                "F",
                "F#",
                "Gb",
                "G",
                "G#"
            }
    assert note_name in allowed, "invalid note name"

def chromatic_notes():
    return ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

if __name__ == "__main__":
    pass