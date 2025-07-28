import matplotlib.pyplot as plt
import numpy as np

# styles: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# style = 'Solarize_Light2' # plot style
style = 'dark_background'
# style = 'classic'
plt.style.use(style) 



notes = "dkrnmfzsplvt"
notes_arr = [c for c in notes] 
notes = "do-ka-re-ni-mo-fa-ze-si-po-la-ve-ti"
# notes = "do (C)-ka-re (D)-ni-mo (E)-fa (F)-ze-si (G)-po-la (A)-ve-ti (B)"
notes_arr = notes.split("-")

pie_nums = [1] * 12
# RGB cycle, start with red, add saturation and paleness
notes_colors = ["#dd0000", "#ff8000", "#dddd22", "#80ff00", "#00dd00", "#00ff80", "#22dddd", "#0080ff", "#0000dd", "#8000ff", "#dd22dd", "#ff0080"] 
# notes_colors = ["#cc0000", "#ff8000", "#cccc33", "#80ff00", "#00cc00", "#00ff80", "#33cccc", "#0080ff", "#0000cc", "#8000ff", "#cc33cc", "#ff0080"] 

# notes_colors = ['#80FF00','#00FF00','#00FF80','#00FFFF','#0080FF','#0000FF','#8000FF','#FF00FF','#FF0080','#FF0000','#FF8000','#FFFF00']
# notes_colors = ['#80FF00','#00FF00','#00FF80','#00FFFF','#0080FF','#0000FF','#8000FF','#FF00FF','#FF0080','#FF0000','#FF8000','#FFFF00']
# notes_colors = ['#80DD20','#20DD20','#20DD80','#20DDDD','#2080DD','#2020DD','#8020DD','#DD20DD','#DD2080','#DD2020','#DD8020','#DDDD20'] # saturation brings everything towards grey #808080
# notes_colors = ['#80BB40','#40BB40','#40BB80','#40BBBB','#4080BB','#4040BB','#8040BB','#BB40BB','#BB4080','#BB4040','#BB8040','#BBBB40'] # more saturation 
# notes_colors = ['#809960','#609960','#609980','#609999','#608099','#606099','#806099','#996099','#996080','#996060','#998060','#999960'] # more saturation 
# notes_colors = ['#fe2712','#fc600a','#fb7902','#fccc1a','#fefe33','#b2d732','#66b032','#347c98','#0247fe','#4424d6','#8601af','#c21460'] # ryk notes


# this color picker can be used to create equally spaced colors as well: https://www.w3schools.com/colors/colors_picker.asp
# bright and darkness and saturation manipulation (think of how to play with them)

def rotate(x):
    copy = [c for c in x[1:]]
    copy.append(x[0])
    return copy

# for i in range(12):
#     plt.pie(pie_nums, labels=notes_arr, colors=notes_colors)
#     plt.savefig(f"colorwheel_reverse_{i:02d}_{''.join(notes_arr)}_style{style}.jpg")
#     plt.clf()
#     notes_arr = rotate(notes_arr)
#     notes_colors = rotate(notes_colors)

notes_arr = list(reversed(notes_arr))
notes_colors = list(reversed(notes_colors))

for i in range(12):
    plt.pie(pie_nums, labels=notes_arr, colors=notes_colors)
    plt.savefig(f"colorwheel_normal_{i:02d}_{''.join(notes_arr)}_style_{style}.jpg")
    plt.clf()
    notes_arr = rotate(notes_arr)
    notes_colors = rotate(notes_colors)