from flask import Blueprint, render_template, url_for
import pandas
from requests import session
from . import tableutil as t
from . import forms
from . import queries

bp = Blueprint('lots',__name__)

@bp.route('/lots', methods=('GET','POST'))   
def stock():
    df = pandas.DataFrame()

    # ID and SITE form
    form = forms.IDandSITEForm()
    formparams = {"ID":"%", "SITE":"%"}

    sqlstr = queries.lotcheck(**formparams)
    df = t.runquery(sqlstr)
    form.SITE.choices = [('%','All Locations'), ('HGZ','China'), ('MAIN','Japan'), ('IS','Singapore'), ('MY','Malaysia'), ('HK','Hong Kong'), ('CUSTOMER','Customer'), ('SE','SE'), ('TH','Thailand'), ('US','United States')]
    
    if form.data == None:
        form.SITE.data = '%'

    if form.Query.data:
        if form.ID.data != "":
            formparams['ID'] = form.ID.data
        formparams['SITE'] = form.SITE.data

        sqlstr = queries.lotcheck(**formparams)
        df = t.runquery(sqlstr)
        # col = list(df)

        
    #print("++++   ID: " + formparams['ID'] + "     SITE: " + formparams['SITE'] + "   ++++")

    res = t.conv_html(df.head(100))
    return render_template('lots.html', res=res, form=form)
