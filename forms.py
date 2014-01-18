from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class ApiKey(Form):
    name = TextField('ApiKey', validators = [Required()])
