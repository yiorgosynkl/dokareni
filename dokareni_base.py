from collections import namedtuple
import os

# play background C note with this video: https://www.youtube.com/watch?v=OEEKE3wY9Yk&ab_channel=HealingVibrations
Note = namedtuple("Note", "let syl num color mp3_name full_name") # letter, syllable, number
N_NOTES = 12
d = Note('d', 'do', 0, '#80ff00', "C", "C")
k = Note('k', 'ka', 1, '#00ff00', "Db", "C#/Db")
r = Note('r', 're', 2, '#00ff80', "D", "D")
n = Note('n', 'ni', 3, '#00ffff', "Eb", "D#/Eb")
m = Note('m', 'mo', 4, '#0080ff', "E", "E")
f = Note('f', 'fa', 5, '#0000ff', "F", "F")
z = Note('z', 'ze', 6, '#8000ff', "Gb", "F#/Gb")
s = Note('s', 'si', 7, '#ff00ff', "G", "G")
p = Note('p', 'po', 8, '#ff0080', "Ab", "G#/Ab")
l = Note('l', 'la', 9, '#ff0000', "A", "A")
v = Note('v', 've', 10, '#ff8000', "Bb", "A#/Bb")
t = Note('t', 'ti', 11, '#ffff00', "B", "B")

def play_note(note: Note, lvl = 4):
    filepath = f"./piano-mp3/{note.mp3_name}{lvl}.mp3"
    os.system("afplay " + filepath)

notes_vec = [d,k,r,n,m,f,z,s,p,l,v,t]

# # write pythonic and clean code with namedtuple
# notes_dic = {
#     'd': d,
#     'k': k,
#     'r': r,
#     'n': n,
#     'm': m,
#     'f': f,
#     'z': z,
#     's': s,
#     'p': p,
#     'l': l,
#     'v': v,
#     't': t,
# }


# if we change d, the other places don't change
# print(d)
# print(notes_vec[0])
# d = Note('x', 'xxxxx', 11111, '#999999')
# print(d)
# print(notes_vec[0])

# printable format for note (using the color)
def pnote(note: Note):
    rd,gr,bl = tuple(int(note.color[i:i+2], 16) for i in (1, 3, 5))     # hex to rgb convert
    # return f'\033[38;2;{rd};{gr};{bl}m{note.let}\033[0m' # foreground color
    # return f'\033[48;2;{rd};{gr};{bl}m{note.let}\033[0m' # background color
    return f'\033[38;2;0;0;0m\033[48;2;{rd};{gr};{bl}m{note.let}\033[0m' # foreground and background color, syllable print
    # return f'\033[38;2;0;0;0m\033[48;2;{rd};{gr};{bl}m{note.let}\033[0m' # foreground and background color, letter print