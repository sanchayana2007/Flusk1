from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import Form
from wtforms import RadioField,SubmitField
#pass the Module name to the Flask
app = Flask(__name__)
app.config['SECRET_KEY']='secret!'

@app.route('/')
def todo():
    return render_template('index.html')


@app.route('/new',methods=['POS'])
def new(id):
    return redirect(url_for('todo'))



if __name__ == '__main__':
    #This 0.0.0.0 will be connected to any machine can ping  your computer
    app.run(host='0.0.0.0',port=5000,debug=True)