'''
Purpose: To refresh my Flask Skills very barebones basic
'''
from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
from app_const import dir_path, options


curDir = dir_path
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        title = request.form['graph_title']
        user_input_x = request.form['user_input_x']
        user_input_y = request.form['user_input_y']
        user_input_grid = request.form['options_grid']
        selected_line = request.form['selected_line']
        processed_result = process_input(title,
                                         user_input_x,user_input_y,
                                         user_input_grid,selected_line)
        return render_template('index.html', result=processed_result,options=options)
    return render_template('index.html', options=options)

@app.route('/circular')
def circular():
    return render_template('circular.html')

@app.route('/multiD')
def multiD():
    return render_template('multiD.html')



def process_input(title='Untitled',
                  x='1,2,3,4',
                  y='1,2,3,4',z='Grid'
                  ,line='Line'):
    
    path = dir_path+'static/image.png'
    path2 = dir_path+'download/image.png'
    grid = ''
    nogrid = ''
    try:
        X = x.split(',')
        Y = y.split(',')

        for i in range(len(X)):
            X[i] = float(X[i])
            Y[i] = float(Y[i])
        
        fig, ax = plt.subplots(figsize=(500/80, 400/80), dpi=80)
        ax.plot(X,Y,options[line])
        plt.title(title)
        if z=='Grid':
            ax.grid(True)
            grid = 'checked'
            
        else:
            ax.grid(False)
            nogrid = 'checked'


        
        
        #os.system('rm {}'.format(path))
        fig.savefig(path)
        fig.savefig(path2)
    
    except:
        return 'Unable to Graph', "fail", title,x,y, nogrid, grid, line
        
    return 'DONE!', 'pass', title,x,y,nogrid, grid, line




    

if __name__ == '__main__':
    #wb.open('http://127.0.0.1:5000/')
    process_input()
    app.run(debug=True)