from flask import Blueprint, render_template, url_for
from . import tableutil as t
from . import forms

bp = Blueprint('stock',__name__)

@bp.route('/stock', methods=('GET','POST'))   
def stock():
    
    # Load data
    df = t.demodata()
    col = list(df)
    newdf = df

    # Collect filter params from form
    form = forms.FilterForm()
    form.column1.choices = col
    form.column2.choices = col
    form.column3.choices = col

    if form.column1.data == None:
        form.column1.data = col[0]

    if form.column2.data == None:
        form.column2.data = col[1]

    if form.column3.data == None:
        form.column3.data = col[2]

    if form.filter1.data != "":
        temp = newdf[form.column1.data]
        newdf = newdf[temp.astype(str).str.contains(str(form.filter1.data))]

    if form.filter2.data != "":
        temp = newdf[form.column2.data]
        newdf = newdf[temp.astype(str).str.contains(str(form.filter2.data))]

    if form.filter3.data != "":
        temp = newdf[form.column3.data]
        newdf = newdf[temp.astype(str).str.contains(str(form.filter3.data))]


    res = t.conv_html(newdf.head(100))
    return render_template('stock.html', res=res, form=form)
