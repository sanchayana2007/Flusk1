from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import Form
from wtforms import RadioField,SubmitField
#pass the Module name to the Flask
app = Flask(__name__)
app.config['SECRET_KEY']='secret!'


guesses = ['Python','perl','C++']
questions = ['Does it6 compile','Can we run that on VM']

#Same HTML form template conveterd to class wtfform secured version
class YesNoVersion(Form):
    answer = RadioField('Yor answer',choices=[('yes','Yes'),('no','No')])
    submit = SubmitField('Submit')



@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html',guess=guesses[id])
#this is invoked by the index and it has a form
#this form will be updated and POSTED
# The answer field of the form will be found
@app.route('/question/<int:id>',methods= ['GET','POST'])
def question(id):
    if request.method == 'POST':
        if request.form['answer'] == "yes":
            return redirect(url_for('question',id=id+1))
    return render_template('question.html',question=questions[id])
# Does the same work
#It Dosent need a template it will render the Wtf form described in class
@app.route('/question_wtf/<int:id>',methods= ['GET','POST'])
def question_wtf(id):
    form = YesNoVersion()
    if form.validate_on_submit():
        if form.answer.data == 'yes':
            return redirect(url_for('question',id=id+1))
    return render_template('question_wtf.html',question=questions[id],form=form)



if __name__ == '__main__':
    #This 0.0.0.0 will be connected to any machine can ping  your computer
    app.run(host='0.0.0.0',port=5000,debug=True)