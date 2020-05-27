from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home', img_path1 = "cleantech2-tn.png")

@app.route('/cleantech')
def cleantech():
	return render_template('cleantech.html', title='Cleantech')