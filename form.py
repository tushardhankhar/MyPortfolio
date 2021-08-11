from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , TextField
from wtforms.validators import DataRequired, Email

class Info(FlaskForm):
    name = StringField('Full Name  ',validators=[DataRequired()])
    email = StringField('Email Address',validators=[DataRequired()])
    message = TextField('Message')
    submit = SubmitField('Say Hello')