from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class ApiKey(Form):
    apikey = TextField('apikey', validators = [Required()])
