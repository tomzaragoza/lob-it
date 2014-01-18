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
		pc = []
		postcards = lob.Postcard.list()
		print dir(postcards[0])
		for p in postcards:
			to_address = '{0}, {1}, {2}, {3}'.format(p.to.address_line1, p.to.address_city, p.to.address_state, p.to.address_country)
			from_address = '{0}, {1}, {2}, {3}'.format(p.from_address.address_line1, p.from_address.address_city, p.from_address.address_state, p.from_address.address_country)
			pc.append({
						'name': p.name, 
						'to': to_address,
						'from': from_address
					}) 
		
		return render_template('map.html', hi='hi', postcards=pc)

@app.route('/map')
def map():
	return render_template('map.html')

if __name__ == "__main__":
    app.run()