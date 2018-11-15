from flask import Flask
from flask import render_template, request
from database import get_all_cats, create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
	cats = get_all_cats()
	return render_template("home.html", cats=cats)

@app.route('/cats/<string:id>')
def cat_profile(id):
	return render_template('cat.html', cat_id=id)

@app.route('/create_cats', methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':
		cats = get_all_cats()
		return render_template("home.html", cats=cats)
	if request.method == 'POST':
		name = request.form['name']
		new_cat = create_cat(name)
		cats = get_all_cats()
		return render_template("home.html", cats=cats)


if __name__ == '__main__':
	app.run(debug = True)
