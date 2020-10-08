import PySimpleGUI as sg

import file_processing as file
import numpy

sg.theme('DarkAmber')   # Add a touch of color

GRASS = 10 
SAND = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

RES = 16 # Change size of map

def render_square(graph,t,x,y):
    square =[]
    e = []
    GRASS_C =  '#92D050'
    DESERT_C = '#DDD9C3'
    FLOREST_C = '#00B050'
    MOUNTAIN_C = '#948A54'
    WATER_C = '#0070C0'

    if t == 'G':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 ))
        e.append(' ')
    elif t == 'D':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        e.append(' ')

    elif t == 'F':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=FLOREST_C,line_width = 0  ))
        e.append(' ')

    elif t == 'M':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=MOUNTAIN_C,line_width = 0  ))
        e.append(' ')

    elif t == 'W':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=WATER_C,line_width = 0  ))
        e.append(' ')

    elif t == 'S':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 ))

        e = (['fg',
                (square.append(graph.DrawImage("images/sword.png",location= (x*RES,y*RES)))),
                [x*RES,y*RES]])
    elif t == 'L':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 ))
        e = (['L',
                graph.DrawImage("images/link.png",location= (x*RES,y*RES)),
                [x,y]])
            
        print (e)
    elif t == 'R':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        e= ([
                'g',
                graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Red',line_color="black",line_width=3),
                [x*RES +RES/2,y*RES+ RES/2]])
    elif t == 'E':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        e.append(['g',
                graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Green',line_color="black",line_width=3),
                [x*RES +RES/2,y*RES+ RES/2]])

    elif t == 'B':
        square.append(graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 ))
        e.append(['g',
                graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Blue',line_color="black",line_width=3),
                [x*RES +RES/2,y*RES+ RES/2]])

    return square,e


def initial_map(world_map,graph):
    #makes the basic map shown on screen

    map_layout = []
    start_location=goals_location= [] # final goal in first position


    for i in range(len(world_map)):
        row = []
        for j in range(len(world_map[i])):
            square,aux = render_square(graph,world_map[j][i],i,j)

            a= aux.pop(0)
            if a == 'g':
                goals_location.append(aux)
            elif a == 'fg':
                goals_location.insert(0,aux)
            elif a == 'L':
                start_location = aux

            row.append(square)
        map_layout.append(row)
    return map_layout,start_location,goals_location


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
        [sg.T('Opções'), sg.Button('Editar'), sg.Button('Iniciar'),sg.Button('down'),sg.Button('left')]
    ]

    window = sg.Window('Busca Euristica', layout)
    window.finalize()

    map_,link_info,goals_info = initial_map(world_map,graph)

    return window,graph,map_,link_info,goals_info 

def movement(graph,info,x,y):
    # move to position (x,y)
    
    old_x= info[1][0]
    old_y= info[1][1]

    figure = info[0]
    
    graph.RelocateFigure(figure,x*RES,y*RES)

    graph.DrawLine(point_from = (old_x*RES + RES/2,old_y*RES + RES/2),
                point_to = (x*RES +RES/2,y*RES+ RES/2),
                color="black",
                width=2)
    
    info[1][0] = x
    info[1][1] = y
    graph.BringFigureToFront(figure)

    
    


def main():
    window,graph,map_ids,link,goals = build_main_layout()

    x=23
    y =27

    while True:      
        event, values = window.read()
        if event == sg.WIN_CLOSED:      
            break
        elif event == 'Iniciar':
            sg.popup_error('Ainda não foi implementado')
        elif event == 'Editar':
            sg.popup_error('Ainda não foi implementado')
        
        elif event == 'down':
            y = y+1
            movement(graph,link,x,y)
        elif event == 'left':
            x = x-1
            movement(graph,link,x,y)
    
    
    window.close()

if __name__ == "__main__":
    main()


