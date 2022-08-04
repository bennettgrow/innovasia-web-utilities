from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class IDandSITEForm(FlaskForm):
    ID = StringField("ID")
    SITE = SelectField('Site')
    EQUALITY = SelectField('Equality')
    DESC = StringField('Description')
    ADD = StringField("Filter")
    QTY = SelectField("Quantity Type")
    Query = SubmitField("Query")

