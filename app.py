from flask import Flask , render_template , send_file , redirect , url_for , session , flash
import webbrowser
from form import Info

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = 'ADAD'

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
        session['name']=mess.name.data
        session['email']=mess.email.data
        session['message']=mess.message.data
        return redirect(url_for('contact'))
        
    return render_template('contact.html',mess=mess)

@app.route('/project')
def project():
    return render_template('project.html')


if __name__ == '__main__':
    app.run(debug=True)