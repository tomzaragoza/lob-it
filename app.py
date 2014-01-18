import lob
from flask import *
from pymongo import MongoClient


app = Flask(__name__)

mongo = MongoClient()
db = mongo['lob']
collection = db['postcards']

@app.route('/')
def hello():
	return render_template('index.html')




if __name__ == "__main__":
    app.run()