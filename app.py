from flask import Flask , render_template , send_file , redirect , url_for
import webbrowser

app = Flask(__name__,template_folder='templates')

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

if __name__ == '__main__':
    app.run(debug=True)