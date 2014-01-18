import lob
from flask import *
from pymongo import MongoClient


app = Flask(__name__)

mongo = MongoClient()
db = mongo['lob']
collection = db['postcards']

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/api_key')
def add_api_key():
	return render_template('api_key.html')

@app.route('/map')
def map():
	return render_template('map.html')

if __name__ == "__main__":
	
    app.run()