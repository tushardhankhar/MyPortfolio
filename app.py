from flask import Flask , render_template , send_file

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/resume-pdf/')
def resume_pdf():
	return send_file(r'C:\My Portfolio\static\tushar(tushardhankhar98@gmail.com).pdf', attachment_filename='tushar(tushardhankhar98@gmail.com).pdf')
	

if __name__ == '__main__':
    app.run(debug=True)