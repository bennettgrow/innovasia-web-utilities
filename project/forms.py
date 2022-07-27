from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class IDandSITEForm(FlaskForm):
    ID = StringField("ID")
    SITE = SelectField('Site')
    Query = SubmitField("Query")

