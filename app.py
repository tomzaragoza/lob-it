# import lob
# from forms import *
# from forms import ApiKey
# import forms
from forms import ApiKey
from flask import *
from pymongo import MongoClient


app = Flask(__name__)
app.debug = True
app.config.from_object('config')


mongo = MongoClient()
db = mongo['lob']
collection = db['postcards']

@app.route('/', methods=['POST', 'GET'])
def home():
	# print "whatatlialkntlkna"
	if request.method == 'GET':

		# form = ApiKey(csrf_enabled=True)
		# form = ApiKey()
		form = ApiKey(request.form)
		return render_template('index.html', form=form)#, form = form)#, form=form)#, form=form)#, form=form)

@app.route('/api_key', methods=['POST'])
def add_api_key():
	if request.method == 'POST':

		return render_template('map.html', hi='hi')
		# return url_for('map', hi='hi')
		# return redirect('/map', hi='hi')

@app.route('/map')
def map():
	return render_template('map.html')

if __name__ == "__main__":
    app.run()