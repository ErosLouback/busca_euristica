import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

GRASS = 10 
SAND = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

# All the stuff inside your window.
hyrule = [[1 for j in range(42)] for i in range(42)]
layout =  [[sg.Button('?', size=(1, 1), key=(i,j), pad=(0,0)) for j in range(42)] for i in range(42)]

def create_map(self):
    map_layout =[]
    for i in range(42):
        row = []
        for j in range(42):



# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
