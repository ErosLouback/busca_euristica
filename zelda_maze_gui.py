import PySimpleGUI as sg

import file_processing as file

sg.theme('DarkAmber')   # Add a touch of color

GRASS = 10 
SAND = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

RES = 16
def render_square(graph,t,x,y):
    square = []
    GRASS_C =  '#92D050'
    DESERT_C = '#DDD9C3'
    FLOREST_C = '#00B050'
    MOUNTAIN_C = '#948A54'
    WATER_C = '#0070C0'

    if t == 'G':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 )
    elif t == 'D':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 )
    elif t == 'F':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=FLOREST_C,line_width = 0  )
    elif t == 'M':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=MOUNTAIN_C,line_width = 0  )
    elif t == 'W':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=WATER_C,line_width = 0  )
    


def initial_map(world_map,graph):
    #makes the basic map shown on screen
    map_layout = []

    for i in range(len(world_map)):
        row = []
        for j in range(len(world_map[i])):
            row.append(render_square(graph,world_map[i][j],i,j))
        map_layout.append(row)
    return map_layout,graph


#def build_main_layout:
world_map = file.color_map("hyrule.txt")
#layout =  [[sg.Button('?', size=(1, 1), key=(i,j), pad=(0,0)) for j in range(len(world_map))] for i in range(len(world_map))]

graph = sg.Graph(
                canvas_size=(len(world_map)*RES,len(world_map)*RES),
                graph_bottom_left=(len(world_map)*RES,0),
                graph_top_right=(0, len(world_map)*RES),
                background_color='red',
                key='graph')
layout = [
    [graph]
]

window = sg.Window('Busca Euristica', layout)
window.finalize()
 
map_layout,graph = initial_map(world_map,graph)

while True:      
    event, values = window.read()
    if event == sg.WIN_CLOSED:      
        break
window.close()
