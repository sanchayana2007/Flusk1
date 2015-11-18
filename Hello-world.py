from flask import Flask,render_template
#pass the Module name to the Flask
app = Flask(__name__)

guesses = ['Python','perl','C++']


@app.route('/')
def hello_world():
    return render_template('index.html')



'''
@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html',guess=guesses[id])
'''
@app.route('/question/<int:id>')
def question(id):
    return render_template('guess.html',question=guesses[id])


if __name__ == '__main__':
    #This 0.0.0.0 will be connected to any machine can ping  your computer
    app.run(host='0.0.0.0',port=5000,debug=True)