import argparse

###
# find specified note on each guitar string
###

# user can give note name in terminal
parser = argparse.ArgumentParser(description='Find note on guitar string. Returns fret position.')
parser.add_argument("search_note", type=str)
args = parser.parse_args()

wanna_find = args.search_note

# can alter to do other styles of search
list_of_notes = ["A", "B", "C", "D", "E", "F", "G"]

# tuning
string1 = "E"
string2 = "B"
string3 = "G"
string4 = "D"
string5 = "A"
string6 = string1
strings = [string1, string2, string3, string4, string5, string6]


# find it
for string in strings:
    fret = 0
    note = string
    amount = len(list_of_notes)
    while note != wanna_find:
        pos = list_of_notes.index(note)
        next_pos = (pos + 1)%amount
        next_note = list_of_notes[next_pos]
        # this is not yet dynamic, but ok for now
        if next_note == "C" or next_note == "F":
            fret = fret + 1
        else:
            fret = fret + 2
        note = list_of_notes[next_pos]
    print(string, ":", fret)
