from flask import Blueprint, render_template, session, url_for
import pandas
from . import tableutil as t
from . import forms
from . import queries

bp = Blueprint('vendorpo',__name__)

@bp.route('/vendorpo', methods=('GET','POST'))   
def itemsales():
    df = pandas.DataFrame()

    # ID and SITE form
    form = forms.IDandSITEForm()
    formparams = {"SITE":"%", "EQUALITY":"LIKE", "YEAR":"%", "DESC":"%"}

    sqlstr = queries.vendorpoquery(**formparams)
    df = t.runquery(sqlstr)
    form.SITE.choices = [('%','All Locations'), ('INNOCN','INNOCN'), ('INNOINC','INNOINC'), ('INNOKK','INNOKK'), ('INNOTH','INNOTH')]
    form.EQUALITY.choices = [('LIKE','Any'), ('>','>'), ('=','='), ('<','<')]


    if form.Query.data:

        if form.DESC.data != "":
            formparams['DESC'] = form.DESC.data

        if form.ADD.data != "":
            formparams['YEAR'] = form.ADD.data
            formparams['EQUALITY'] = form.EQUALITY.data

        if form.ADD.data == "" or form.EQUALITY.data == 'LIKE':
            formparams['EQUALITY'] = 'LIKE'
            formparams['YEAR'] = "%"

        formparams['SITE'] = form.SITE.data

        sqlstr = queries.vendorpoquery(**formparams)
        df = t.runquery(sqlstr)

    numrows = df.shape[0]

    # dfcsv = df.to_csv(index=False, header=True, sep=",")
    # session["dfcsv"] = dfcsv
        
    res = t.conv_html(df)
    return render_template('vendorpo.html', res=res, form=form, numrows=numrows)






