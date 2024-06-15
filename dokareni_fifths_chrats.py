import matplotlib.pyplot as plt
import numpy as np

# styles: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# style = 'Solarize_Light2' # plot style
style = 'dark_background'
# style = 'classic'
plt.style.use(style) 

notes = "dkrnmfzsplvt"
notes_arr = [c for c in notes] 
# notes = "do (C)-ka-re (D)-ni-mo (E)-fa (F)-ze-si (G)-po-la (A)-ve-ti (B)"
# notes_arr = notes.split("-")

pie_nums = [1] * 12
notes_colors = ['#80FF00','#00FF00','#00FF80','#00FFFF','#0080FF','#0000FF','#8000FF','#FF00FF','#FF0080','#FF0000','#FF8000','#FFFF00']

def rotate(x):
    copy = [c for c in x[1:]]
    copy.append(x[0])
    return copy

def reorder_5ths(arr):
    new_arr = []
    times = 12
    step = 7
    for i in range(0, times*step, step):
        new_arr.append(arr[i%times])
    return new_arr

notes_arr = reorder_5ths(notes_arr) 
notes_colors = reorder_5ths(notes_colors) 

for i in range(12):
    plt.pie(pie_nums, labels=notes_arr, colors=notes_colors)
    plt.savefig(f"colorwheel_4ths_{i:02d}_{''.join(notes_arr)}_style{style}.jpg")
    plt.clf()
    notes_arr = rotate(notes_arr)
    notes_colors = rotate(notes_colors)

notes_arr = list(reversed(notes_arr))
notes_colors = list(reversed(notes_colors))

for i in range(12):
    plt.pie(pie_nums, labels=notes_arr, colors=notes_colors)
    plt.savefig(f"colorwheel_5ths_{i:02d}_{''.join(notes_arr)}_style{style}.jpg")
    plt.clf()
    notes_arr = rotate(notes_arr)
    notes_colors = rotate(notes_colors)