from dokareni_base import *
import random
import signal
import sys

print(f"---- Color Names ----")
print(f"{pnote(d)} {d.full_name} (chartreuse)")
print(f"{pnote(k)} {k.full_name} (green)")
print(f"{pnote(r)} {r.full_name} (springgreen)")
print(f"{pnote(n)} {n.full_name} (cyan)")
print(f"{pnote(m)} {m.full_name} (azure)")
print(f"{pnote(f)} {f.full_name} (blue)")
print(f"{pnote(z)} {z.full_name} (violet)")
print(f"{pnote(s)} {s.full_name} (magenta)")
print(f"{pnote(p)} {p.full_name} (rose)")
print(f"{pnote(l)} {l.full_name} (red)")
print(f"{pnote(v)} {v.full_name} (orange)")
print(f"{pnote(t)} {t.full_name} (yellow)")


print(f"---- Clockwise Triplets ----")
print(f"o triplet: {pnote(d)}{pnote(m)}{pnote(p)} {pnote(m)}{pnote(p)}{pnote(d)} {pnote(p)}{pnote(d)}{pnote(m)}")
print(f"a triplet: {pnote(k)}{pnote(f)}{pnote(l)} {pnote(f)}{pnote(l)}{pnote(k)} {pnote(l)}{pnote(k)}{pnote(f)}")
print(f"e triplet: {pnote(r)}{pnote(z)}{pnote(v)} {pnote(z)}{pnote(v)}{pnote(r)} {pnote(v)}{pnote(r)}{pnote(z)}")
print(f"i triplet: {pnote(n)}{pnote(s)}{pnote(t)} {pnote(s)}{pnote(t)}{pnote(n)} {pnote(t)}{pnote(n)}{pnote(s)}")
print(f"---- Anti-clockwise Triplets ----")
print(f"o triplet: {pnote(d)}{pnote(p)}{pnote(m)} {pnote(p)}{pnote(m)}{pnote(d)} {pnote(m)}{pnote(d)}{pnote(p)}")
print(f"a triplet: {pnote(k)}{pnote(l)}{pnote(f)} {pnote(l)}{pnote(f)}{pnote(k)} {pnote(f)}{pnote(k)}{pnote(l)}")
print(f"e triplet: {pnote(r)}{pnote(v)}{pnote(z)} {pnote(v)}{pnote(z)}{pnote(r)} {pnote(z)}{pnote(r)}{pnote(v)}")
print(f"i triplet: {pnote(n)}{pnote(t)}{pnote(s)} {pnote(t)}{pnote(s)}{pnote(n)} {pnote(s)}{pnote(n)}{pnote(t)}")
print(f"---- Notes in Line ----")
print(3*f"{pnote(d)}{pnote(k)}{pnote(r)}{pnote(n)}{pnote(m)}{pnote(f)}{pnote(z)}{pnote(s)}{pnote(p)}{pnote(l)}{pnote(v)}{pnote(t)}")

print(f"---- Identify the interval (given two notes) ----")
# get notes and direction
RAND_INLUDED_NOTES = [d,k,r,n,m,f,z,s,p,l,v,t] # all
# RAND_INLUDED_NOTES = [d,m,p] # o triplet
# RAND_INLUDED_NOTES = [k,f,l] # a triplet
# RAND_INLUDED_NOTES = [r,z,v] # e triplet
# RAND_INLUDED_NOTES = [n,s,t] # i triplet
# RAND_INLUDED_NOTES = [d,r,m,z,p,v] # cycle of 2s (oe sixet)
# RAND_INLUDED_NOTES = [k,n,f,s,l,t] # cycle of 2s (ai sixet)
def get_random():
    num1 = random.randrange(len(RAND_INLUDED_NOTES))
    # num1 = 10
    num2 = num1
    while num2 == num1:
        num2 = random.randrange(len(RAND_INLUDED_NOTES))
    drct = '/' if random.randrange(2) == 1 else "\\" # ascending or descending
    # drct = '\\' 
    note1 = RAND_INLUDED_NOTES[num1]
    note2 = RAND_INLUDED_NOTES[num2]
    return note1, note2, drct

def notes_dist(note1, note2, drct = '/'):
    if drct == '/':
        if note1.num < note2.num:
            return note2.num - note1.num
        else: # note1.num > note2.num
            return N_NOTES + note2.num - note1.num
    else: # drct == '\':
        if note1.num > note2.num:
            return note2.num - note1.num
        else: # note1.num < note2.num
            return note2.num - note1.num - N_NOTES

def play_two_notes(note1, note2, drct = '/'):
    # B3 -> Bb3 -> C4 -> Db4 
    if drct == '/' and note1.num > note2.num:
        play_note(note1, 3)
        play_note(note2, 4)
    elif  drct == '\\' and note1.num < note2.num:
        play_note(note1, 4)
        play_note(note2, 3)
    else:
        lvl = 3 if random.randrange(2) == 1 else 4 # 50% chance
        play_note(note1, lvl)
        play_note(note2, lvl)

# Ctrl+C handler
def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!\nThe wheel of notes:')
    print(f'   {pnote(t)}{pnote(d)}  \n  {pnote(v)}  {pnote(k)} \n {pnote(l)}    {pnote(r)}\n {pnote(p)}    {pnote(n)}\n  {pnote(s)}  {pnote(m)} \n   {pnote(z)}{pnote(f)}  ')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    note1, note2, drct = get_random()
    # print(f" {pnote(note1)} {drct} {pnote(note2)} : {notes_dist(note1, note2, drct)}")
    dist = notes_dist(note1, note2, drct)
    try:
        print(f" {pnote(note1)} {drct} {pnote(note2)} : ", end="", flush=True)
        play_two_notes(note1, note2, drct) # uncomment to play note
        ans = int(input())
    except ValueError:
        print("Incorrect input :|")
        print(f"    Actually, {pnote(note1)} {drct} {pnote(note2)} : {dist}")
        continue
    if ans == dist:
        print("    Correct :)")
    else:
        print(f"    Actually, {pnote(note1)} {drct} {pnote(note2)} : {dist}")


## TODO: make a second test to give interval and provide the note!