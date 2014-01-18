import lob
from forms import ApiKey
from flask import *
from pymongo import MongoClient


app = Flask(__name__)
app.debug = True
app.config.from_object('config')

mongo = MongoClient()
db = mongo['lob']
collection = db['postcards']
lob.api = ''

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		form = ApiKey(request.form)
		return render_template('index.html', form=form)

def get_post_cards():
	pass

@app.route('/api_key', methods=['POST'])
def add_api_key():
	""" Once the button was pressed for API key getting passed in,
		we verify, pull in data""" 
	if request.method == 'POST':
		form = request.form
		lob.api_key = str(form['apikey'])

		postcards = lob.Postcard.list()
		return render_template('map.html', hi='hi', postcards=postcards)

@app.route('/map')
def map():
	return render_template('map.html')

if __name__ == "__main__":
    app.run()