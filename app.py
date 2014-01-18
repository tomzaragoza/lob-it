import lob
import geopy
import json
from forms import ApiKey
from flask import *
from pymongo import MongoClient


app = Flask(__name__)
app.debug = True
app.config.from_object('config')

mongo = MongoClient()
db = mongo['lob']
postcards_collection = db['postcards']
settings_collection = db['settings']

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		form = ApiKey(request.form)
		return render_template('index.html', form=form)

def get_post_cards():
	pass

def get_lat_long(city, state, address):

	from geopy.geocoders import GeocoderDotUS
	f_string = "%s {0} {1}".format(city, state)
	geolocator = GeocoderDotUS(format_string=f_string)
	address, (latitude, longitude) = geolocator.geocode(address)
	return (address, latitude, longitude)

@app.route('/map', methods=['POST', 'GET'])
def add_api_key():
	""" Once the button was pressed for API key getting passed in,
		we verify, pull in data.
	""" 
	if request.method == 'POST':
		form = request.form
		lob.api_key = str(form['apikey'])

		if not settings_collection.find_one():
			settings_collection.insert({'api-key': lob.api_key}, upsert=True)
	elif request.method == 'GET':
		lob.api_key = settings_collection.find_one({})['api-key']

	pc = []
	postcards = lob.Postcard.list()
	for p in postcards:
		
		try:
			to_address = '{0}, {1}, {2}, {3}'.format(p.to.address_line1, p.to.address_city, p.to.address_state, p.to.address_country)
			from_address = '{0}, {1}, {2}, {3}'.format(p.from_address.address_line1, p.from_address.address_city, p.from_address.address_state, p.from_address.address_country)
			to_lat_long = get_lat_long(p.to.address_city, p.to.address_state, p.to.address_line1)
			from_lat_long = get_lat_long(p.from_address.address_city, p.from_address.address_state, p.from_address.address_line1)
			pc.append({
						'name': p.name, 
						'to': to_address,
						'to_city': p.to.address_city,
						'from': from_address,
						'from_city': p.from_address.address_city,
						'to_latitude': to_lat_long[1],
						'to_longitude': to_lat_long[2],
						'from_latitude': from_lat_long[1],
						'from_longitude': from_lat_long[2]
					}) 
		except:
			pass # the address that was used isn't real
		
		return render_template('map.html', postcards=json.dumps({'data': pc}))

@app.route('/map')
def map():
	return render_template('map.html')

if __name__ == "__main__":
    app.run()