from dokareni_base import *
import random
import signal
import sys

print(f"---- Identify the notes (given the intervals) ----")

# get notes and direction
RAND_INLUDED_NOTES = [d,k,r,n,m,f,z,s,p,l,v,t] # all
def get_random():
    num1 = random.randrange(len(RAND_INLUDED_NOTES))
    note1 = RAND_INLUDED_NOTES[num1]
    drct = '/' if random.randrange(2) == 1 else "\\" # ascending or descending
    return note1, drct

# guess intervals
def get_random_intervals(intr = [3,6,9], keep=3):
    if keep == 1:
        rand_i = random.randrange(len(intr))
        return [intr[rand_i]]
    # shuffle does not work great
    random.shuffle(intr)
    while keep < len(intr):
        random.shuffle(intr)
        intr.pop()
    intr = list(sorted(intr))
    return intr

def check(root_note, drct, guess_intr, ans = []):
    is_correct = True
    correct_notes = []
    for i, dist in enumerate(guess_intr):
        if drct == "/":
            correct_note_num = (root_note.num + dist) % 12
        else: # drct == "\":
            correct_note_num = (root_note.num + 12 - dist) % 12
        correct_note = notes_vec[correct_note_num]
        correct_notes.append(correct_note)
        # if len(ans) <= i or ans[i] != correct_note.syl:
        if len(ans) <= i or ans[i] != correct_note.let: 
            is_correct = False
    return is_correct, correct_notes

while True:
    root_note, drct = get_random()
    # guess_intr = [4,8]
    # guess_intr = [1,2]
    # guess_intr = [1]
    # guess_intr = [2]
    # guess_intr = [1,2,3]
    # guess_intr = get_random_intervals([2,4,6,8,10])
    guess_intr = get_random_intervals()
    try:
        print(f" {pnote(root_note)} {drct} {guess_intr}: ", end="", flush=True)
        play_note(root_note)
        inp = input()
        ans = inp.strip().split()
    except ValueError:
        print("Incorrect input :|")
        is_correct, correct_notes = check(root_note, drct, guess_intr)
        print(f"    Actually, the notes where {' '.join([pnote(x) for x in correct_notes])}")
        continue
    is_correct, correct_notes = check(root_note, drct, guess_intr, ans)
    if is_correct: 
        print(f"    Correct :)")
        # print(f"    Correct :), the notes where {' '.join([pnote(x) for x in correct_notes])}")
    else:
        print(f"    Actually, the notes where {' '.join([pnote(x) for x in correct_notes])}")

