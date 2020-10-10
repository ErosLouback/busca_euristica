import PySimpleGUI as sg

import file_processing as file
import A_stars
import numpy
import time
sg.theme('DarkAmber')   # Add a touch of color

GRASS = 10 
SAND = 20
FLOREST = 100
MOUNTAIN = 150
WATER = 180

RES = 16 # Change size of map

def render_square(graph,t,x,y):
    square = int
    e = []
    GRASS_C =  '#92D050'
    DESERT_C = '#DDD9C3'
    FLOREST_C = '#00B050'
    MOUNTAIN_C = '#948A54'
    WATER_C = '#0070C0'

    if t == 'G':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 )
        e.append(' ')
    elif t == 'D':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 )
        e.append(' ')

    elif t == 'F':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=FLOREST_C,line_width = 0  )
        e.append(' ')

    elif t == 'M':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=MOUNTAIN_C,line_width = 0  )
        e.append(' ')

    elif t == 'W':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=WATER_C,line_width = 0  )
        e.append(' ')

    elif t == 'S':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 )

        e = (['fg',
                graph.DrawImage("images/sword.png",location= (x*RES,y*RES)),
                [x,y]])
    elif t == 'L':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=GRASS_C,line_width = 0 )
        e = (['L',
                graph.DrawImage("images/link.png",location= (x*RES,y*RES)),
                [x,y]])            
    elif t == 'R':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 )
        e= ([
                'g',
                graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Red',line_color="black",line_width=3),
                [x,y]])
    elif t == 'E':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 )
        e.append(['g',
                graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Green',line_color="black",line_width=3),
                [x,y]])

    elif t == 'B':
        square = graph.DrawRectangle((x*RES,y*RES), (x*RES +RES,y*RES +RES), fill_color=DESERT_C,line_width = 0 )
        e.append(['g',
                graph.DrawCircle(center_location = (x*RES +RES/2,y*RES+ RES/2),radius = RES*0.25,fill_color='Blue',line_color="black",line_width=3),
                [x,y]])

    return square,e


def initial_map(world_map,graph):
    #makes the basic map shown on screen

    map_layout = {}

    for i in range(len(world_map)):
        for j in range(len(world_map[i])):
            square,aux = render_square(graph,world_map[i][j],j,i)
            map_layout[(i,j)] = square
            a= aux.pop(0)
            if a == 'g':
                if 'goal key' in map_layout:
                    map_layout['goal key'] = [map_layout['goal key'],aux[0]]
                    map_layout['goal location'] = [map_layout['goal location'],aux[1]]
                else:
                    map_layout['goal key'] = aux[0]
                    map_layout['goal location'] = aux[1]
            elif a == 'fg':
                map_layout['final goal key'] = aux[0]
                map_layout['final goal location'] = aux[1]
            elif a == 'L':
                map_layout['link key'] = aux[0]
                map_layout['link location'] = aux[1]    
        
    return map_layout


def build_main_layout():

    world_map = file.color_map("hyrule.txt")

    graph = sg.Graph(
                canvas_size=(len(world_map)*RES,len(world_map)*RES),
                graph_bottom_left=(0,len(world_map)*RES),
                graph_top_right=(len(world_map)*RES,0),
                background_color='red',
                key='graph',
                enable_events=True)

    column = sg.Column([
                [sg.T('selecione o tipo de terreno')],
                [sg.T('Clique na posição que deseja alterar ')],
                [sg.T('Quando terminar de editar clique em salvar')],
                [sg.Listbox(
                    values=[
                        'G-Grama',
                        'D-Areia',
                        'F-Floresta',
                        'M-Montanha',
                        'W-Água',
                        'S-Master Sword',
                        'L-Link',
                        'R-Pingente da Virtude Vermelho',
                        'E-Pingente da Virtude Verde',
                        'B-Pingente da Virtude Azul'
                    ],
                    select_mode='LISTBOX_SELECT_MODE_SINGLE',
                    enable_events=True,
                    size=(30,10),
                    key='listbox',
                    no_scrollbar=True,
                    visible=True)],
                [sg.SaveAs("Salvar",enable_events=True,target='Salvar')]

                ],
                justification='right',
                vertical_alignment='t',
                expand_x=True,
                expand_y=True,
                visible=False,
                key='column')

    layout = [[graph,column],[sg.T('Opções'), sg.Button('Editar'),sg.Button('Iniciar')]
    ,[sg.B(sg.SYMBOL_UP),sg.B(sg.SYMBOL_DOWN),sg.B(sg.SYMBOL_LEFT),sg.B(sg.SYMBOL_RIGHT)]]

    window = sg.Window('Busca Euristica', layout)
    window.finalize()

    map_ = initial_map(world_map,graph)


    return window,graph,map_,world_map


def move(graph,info,x,y):
    # move to position (x,y)
    
    old_x,old_y= info['link location']

    figure = info['link key']

    a= graph.GetFiguresAtLocation((x*RES +RES/2,y*RES+ RES/2))
    if len(a) > 1:
        graph.draw_point((x*RES +RES/2,y*RES+ RES/2),size=4,color="black")

    graph.SendFigureToBack(a[0])

    graph.RelocateFigure(figure,x*RES,y*RES)

    graph.DrawLine(point_from = (old_x*RES + RES/2,old_y*RES + RES/2),
                point_to = (x*RES +RES/2,y*RES+ RES/2),
                color="black",
                width=2)
    
    info['link location'] = (x,y)
    
    graph.BringFigureToFront(figure)
    #return info

def edit(graph,world_map,dicti,target,terrain):

    x = int(target[0]/RES)
    y = int(target[1]/RES)

    world_map[y][x] = terrain[0][0]
    #graph.DeleteFigure(dicti[(x,y)])
    dicti[(x,y)],aux = render_square(graph,terrain[0][0],x,y)
    a= aux.pop(0)
    if a == 'g':
        loc = dicti['goal location']
        if loc:
            graph.DeleteFigure(dicti['goal key'])
            world_map[y][x] = 'D'

        dicti['goal key'] = aux[0]
        dicti['goal location'] = aux[1]
    elif a == 'fg':
        if dicti['final goal location']:
            graph.DeleteFigure(dicti['final goal key'])
            world_map[y][x] = 'G'

        dicti['final goal key'] = aux[0]
        dicti['final goal location'] = aux[1]
    elif a == 'L':
        if dicti['link location']:
            graph.DeleteFigure(dicti['link key'])
            world_map[y][x] = 'G'

        dicti['link key'] = aux[0]
        dicti['link location'] = aux[1]   



    return world_map


def main():
    ed=False

    window,graph,dicti,world_map = build_main_layout()

    while True:      
        event, values = window.read()

        if event == sg.WIN_CLOSED:      
            break
        elif event == 'Iniciar':
            path = A_stars.main()
            #print(path.caminho)
            for i in path:
                for k in i:
                    print(k)
                    move(graph,dicti,x,y)


        elif event == 'Editar':
            ed = not ed
            window['column'].Update(visible=ed)
        elif event == sg.ELEM_TYPE_GRAPH:
            if ed and len(values['listbox']) > 0:
                world_map = edit(graph,world_map,dicti,values['graph'],values['listbox'])
        elif event == 'Salvar':
            file.save(world_map,values['Salvar'])
            graph.erase()
            dicti = initial_map(world_map,graph)
        
        #DEBUG
        elif event == sg.SYMBOL_DOWN:
            y = y+1
            move(graph,dicti,x,y)
        elif event == sg.SYMBOL_LEFT:
            x = x-1
            move(graph,dicti,x,y)
        elif event == sg.SYMBOL_RIGHT:
            x = x+1
            move(graph,dicti,x,y)
        elif event == sg.SYMBOL_UP:
            y = y-1
            move(graph,dicti,x,y)
    
    
    window.close()

if __name__ == "__main__":
    main()


