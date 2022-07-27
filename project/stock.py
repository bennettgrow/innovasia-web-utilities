from flask import Blueprint, render_template, url_for, Response
import pandas
from requests import session
from . import tableutil as t
from . import forms
from . import queries

bp = Blueprint('stock',__name__)

@bp.route('/stock', methods=('GET','POST'))   
def stock():
    df = pandas.DataFrame()

    # ID and SITE form
    form = forms.IDandSITEForm()
    formparams = {"ID":"9x9x9x9", "SITE":"%"} # Random data to return an empty initial query

    sqlstr = queries.stockcheck(**formparams)
    df = t.runquery(sqlstr)
    form.SITE.choices = [('%','All Locations'), ('HGZ','China'), ('MAIN','Japan'), ('IS','Singapore'), ('MY','Malaysia'), ('HK','Hong Kong'), ('CUSTOMER','Customer'), ('SE','SE'), ('TH','Thailand'), ('US','United States')]
    
    if form.data == None:
        form.SITE.data = '%'

    if form.Query.data:
        if form.ID.data == "" and form.SITE.data != "":
            formparams['ID'] = "%"
            formparams['SITE'] = form.SITE.data
        
        if form.ID.data != "":
            formparams['ID'] = form.ID.data

        formparams['SITE'] = form.SITE.data

        sqlstr = queries.stockcheck(**formparams)
        df = t.runquery(sqlstr)

    
    
    numrows = df.shape[0]

    res = t.conv_html(df)
    return render_template('stock.html', res=res, form=form)
