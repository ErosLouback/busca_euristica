import PySimpleGUI as sg

import file_processing as file

sg.theme('DarkAmber')   # Add a touch of color

GRASS = 10 
SAND = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

RES = 16 # Change size of map

def render_square(graph,t,x,y):
    square =[]
    GRASS_C =  '#92D050'
    DESERT_C = '#DDD9C3'
    FLOREST_C = '#00B050'
    MOUNTAIN_C = '#948A54'
    WATER_C = '#0070C0'

    if t == 'G':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 ))
    elif t == 'D':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
    elif t == 'F':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=FLOREST_C,line_width = 0  ))
    elif t == 'M':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=MOUNTAIN_C,line_width = 0  ))
    elif t == 'W':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=WATER_C,line_width = 0  ))
    elif t == 'S':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 ))
        square.append(graph.DrawImage("images/sword.png",location= (x*RES,y*RES)))
    elif t == 'L':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 ))
        square.append(graph.DrawImage("images/link.png",location= (x*RES,y*RES)))
    elif t == 'R':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        square.append(graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Red',line_color="black",line_width=3))
    elif t == 'E':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        square.append(graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Green',line_color="black",line_width=3))
    elif t == 'B':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        square.append(graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Blue',line_color="black",line_width=3))
    return square


def initial_map(world_map,graph):
    #makes the basic map shown on screen

    map_layout = []

    for i in range(len(world_map)):
        row = []
        for j in range(len(world_map[i])):
            row.append(render_square(graph,world_map[j][i],i,j))
        map_layout.append(row)
    return map_layout


def build_main_layout():

    world_map = file.color_map("hyrule.txt")

    graph = sg.Graph(
                canvas_size=(len(world_map)*RES,len(world_map)*RES),
                graph_bottom_left=(0,len(world_map)*RES),
                graph_top_right=(len(world_map)*RES,0),
                background_color='red',
                key='graph')
    
    layout = [
        [graph],
        [sg.T('Opções'), sg.Button('Editar'), sg.Button('Iniciar')]
    ]

    window = sg.Window('Busca Euristica', layout)
    window.finalize()

    map_ids = initial_map(world_map,graph)
    print(map_ids)

    return window



def main():
    window = build_main_layout()

    while True:      
        event, values = window.read()
        if event == sg.WIN_CLOSED:      
            break
        elif event == 'Iniciar':
            sg.popup_error('Ainda não foi implementado')
        elif event == 'Editar':
            sg.popup_error('Ainda não foi implementado')
    window.close()

if __name__ == "__main__":
    main()


