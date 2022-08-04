from flask import Blueprint, render_template, session, url_for
import pandas
from . import tableutil as t
from . import forms
from . import queries

bp = Blueprint('lots',__name__)

@bp.route('/lots', methods=('GET','POST'))   
def stock():
    df = pandas.DataFrame()

    # ID and SITE form
    form = forms.IDandSITEForm()
    formparams = {"ID":"9x9x9x9x9x9x9", "SITE":"%"}

    sqlstr = queries.lotcheck(**formparams)
    df = t.runquery(sqlstr)
    form.SITE.choices = [('%','All Locations'), ('HGZ','China'), ('MAIN','Japan'), ('IS','Singapore'), ('MY','Malaysia'), ('HK','Hong Kong'), ('CUSTOMER','Customer'), ('SE','SE'), ('TH','Thailand'), ('US','United States')]

    if form.Query.data:
        if form.ID.data == "" and form.SITE.data != "":
            formparams['ID'] = "%"
        
        if form.ID.data != "":
            formparams['ID'] = form.ID.data

        formparams['SITE'] = form.SITE.data

        sqlstr = queries.lotcheck(**formparams)
        df = t.runquery(sqlstr)

    numrows = df.shape[0]
        
    # dfcsv = df.to_csv(index=False, header=True, sep=",")
    # session["dfcsv"] = dfcsv
        
    res = t.conv_html(df)
    return render_template('lots.html', res=res, form=form, numrows=numrows)
