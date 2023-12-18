from flask import Flask, render_template, request, send_file
app = Flask(__name__)


#RoutIndex
@app.route('/')
def index():
    if request.method == 'POST':
        #post function
        pass
    else:
        #GET function
        pass
    images = ['spa_img1.png', 'spa_img2.png','spa_img3.png']
    #images = []
    return render_template('index.html', images=images)

    

@app.route('/staff')
def staff():
    if request.method == 'POST':
        #post function
        pass
    else:
        #GET function
        pass
    return render_template('staff.html')

@app.route('/gift_cards')
def gift_cards():
    if request.method == 'POST':
        #post function
        pass
    else:
        #GET function
        pass
    return render_template('gift_cards.html')

@app.route('/services')
def services():
    if request.method == 'POST':
        #post function
        pass
    else:
        #GET function
        pass
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)