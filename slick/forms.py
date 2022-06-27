from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class FilterForm(FlaskForm):
    column1 = SelectField("Column:")
    filter1 = StringField("Filter:")
    column2 = SelectField("Column:")
    filter2 = StringField("Filter:")
    column3 = SelectField("Column:")
    filter3 = StringField("Filter:")
    submit = SubmitField("Filter")
