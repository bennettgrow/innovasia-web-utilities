from tkinter import E
from flask import Blueprint, render_template, session, url_for
import pandas
from . import tableutil as t
from . import forms
from . import queries

bp = Blueprint('itemsales',__name__)

@bp.route('/itemsales', methods=('GET','POST'))   
def itemsales():
    df = pandas.DataFrame()

    # ID and SITE form
    form = forms.IDandSITEForm()
    formparams = {"ID":"9x9x9x9x9x9x9", "SITE":"%", "EQUALITY":"LIKE", "YEAR":"%", "DESC":"%"}

    sqlstr = queries.itemsalescheck(**formparams)
    df = t.runquery(sqlstr)
    form.SITE.choices = [('%','All Locations'), ('HGZ','China'), ('MAIN','Japan'), ('IS','Singapore'), ('MY','Malaysia'), ('HK','Hong Kong'), ('CUSTOMER','Customer'), ('SE','SE'), ('TH','Thailand'), ('US','United States')]
    form.EQUALITY.choices = [('LIKE','Any'), ('>','>'), ('=','='), ('<','<')]


    if form.Query.data:
        if form.ID.data == "":
            formparams['ID'] = "%"
        
        if form.ID.data != "":
            formparams['ID'] = form.ID.data

        if form.DESC.data != "":
            formparams['DESC'] = form.DESC.data

        if form.ADD.data != "":
            formparams['YEAR'] = form.ADD.data
            formparams['EQUALITY'] = form.EQUALITY.data

        if form.ADD.data == "" or form.EQUALITY.data == 'LIKE':
            formparams['EQUALITY'] = 'LIKE'
            formparams['YEAR'] = "%"

        formparams['SITE'] = form.SITE.data

        sqlstr = queries.itemsalescheck(**formparams)
        df = t.runquery(sqlstr)

    numrows = df.shape[0]

    # dfcsv = df.to_csv(index=False, header=True, sep=",")
    # session["dfcsv"] = dfcsv
        
    res = t.conv_html(df)
    return render_template('itemsales.html', res=res, form=form, numrows=numrows)
