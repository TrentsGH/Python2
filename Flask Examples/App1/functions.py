'''
working functions
'''
from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
from app_const import dir_path, options

Dic = {'title':'untitled',
           'x':'0',
           'y':'0',
           'grid':'noGrid',
           'line':'Line',
           'sizex':500,
           'sizey':400}
def str_to_list(x):
    temp = x.replace(',\n',',')
    temp = temp.replace(',,',',')
    temp = temp.replace('\t',',')
    temp = temp.replace(',,',',')
    temp = temp.replace('\n',',')
    temp = temp.replace(',,',',')
    X = temp.split(',')
    for i in range(len(X)):
            X[i] = float(X[i])
    return X

def ifGrid(g,ax):
    grid = ''
    nogrid = ''
    if g=='Grid':
        ax.grid(True)
        grid = 'checked'
    else:
        ax.grid(False)
        nogrid = 'checked'
    return grid, nogrid

     

def rect_(config=Dic):

    #Get the variables/configurations from the
    #Dictionary
    title=config['title']
    x=config['x']
    y=config['y']
    g=config['grid']
    line=config['line']
    sizex=int(config['sizex'])
    sizey=int(config['sizey'])
    path = dir_path+'static/image.png'
    path2 = dir_path+'download/image.png'
    
    try:
        #Make the graph
        X = str_to_list(x)
        Y = str_to_list(y)
        fig, ax = plt.subplots(figsize=(sizex/80, sizey/80), dpi=80)
        ax.plot(X,Y,options[line])
        plt.title(title)
        grid,nogrid = ifGrid(g)
        fig.savefig(path)
        fig.savefig(path2)

    except:
        return 'Unable to Graph', "fail", title,x,y, nogrid, grid, line
    return 'Graphed', 'pass', title,x,y,nogrid, grid, line