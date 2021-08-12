from flask import Flask , render_template , send_file , redirect , url_for , session , flash
import webbrowser
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from form import Info
import os

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = 'ADAD'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)


class messages(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    message = db.Column(db.Text)

    def __init__(self,name,email,message):
        self.name = name
        self.email = email
        self.message = message
    
    def __repr__(self):
         return f"Name : {self.name} , Email : {self.email} , Message : {self.message}"


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/resume-pdf/')
def resume_pdf():
    return send_file(r'C:\My Portfolio\static\tushar(tushardhankhar98@gmail.com).pdf', attachment_filename='tushar(tushardhankhar98@gmail.com).pdf')
	
@app.route('/test')
def test():
    webbrowser.open_new_tab('http://127.0.0.1:5000/resume-pdf/')
    return redirect(url_for("index"))

@app.route('/git')
def github():
    webbrowser.open_new_tab('https://github.com/tushardhankhar')
    return redirect(url_for("index"))

@app.route('/linkedin')
def linkedin():
    webbrowser.open_new_tab('www.linkedin.com/in/tushar-dhankhar')
    return redirect(url_for("index"))

@app.route('/twitter')
def twitter():
    webbrowser.open_new_tab('https://twitter.com/dhankhar0075?s=08')
    return redirect(url_for("index"))

@app.route('/contact',methods = ['GET','POST'])
def contact():
    mess = Info()
    if mess.validate_on_submit():
        flash('Message sent!!!!!!')
        name = mess.name.data
        email = mess.email.data
        message = mess.message.data
        new_mess = messages(name,email,message)
        db.create_all()
        db.session.add(new_mess)
        db.session.commit()
        return redirect(url_for('contact'))
        
    return render_template('contact.html',mess=mess)

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/display')
def display():
    messa = messages.query.all()
    return render_template('messages_display.html',messa=messa)


if __name__ == '__main__':
    app.run(debug=True)