from flask import Blueprint, render_template, session, url_for
import pandas
from . import tableutil as t
from . import forms
from . import queries

bp = Blueprint('stock',__name__)

@bp.route('/stock', methods=('GET','POST'))   
def stock():
    df = pandas.DataFrame()

    # ID and SITE form
    form = forms.IDandSITEForm()
    formparams = {"ID":"9x9x9x9x9x9x9", "SITE":"%", "DESC":"%", "EQUALITY":"LIKE", "QTY":"QtyOnHand", "FILTER":"%" } # Random data to return an empty initial query

    sqlstr = queries.stockcheck(**formparams)
    df = t.runquery(sqlstr)
    form.SITE.choices = [('%','All Locations'), ('HGZ','China'), ('MAIN','Japan'), ('IS','Singapore'), ('MY','Malaysia'), ('HK','Hong Kong'), ('CUSTOMER','Customer'), ('SE','SE'), ('TH','Thailand'), ('US','United States')]
    form.EQUALITY.choices = [('LIKE','Any'), ('>','>'), ('=','='), ('<','<')]
    form.QTY.choices = ["QtyAvail", "QtyOnHand", "QtyOnPO", "QtyCustOrd"]

    if form.Query.data:
        if form.ID.data == "" and form.SITE.data != "":
            formparams['ID'] = "%"
        
        if form.ID.data != "":
            formparams['ID'] = form.ID.data

        if form.DESC.data != "":
            formparams['DESC'] = form.DESC.data

        if form.ADD.data != "":
            formparams['FILTER'] = form.ADD.data
            formparams['EQUALITY'] = form.EQUALITY.data

        if form.ADD.data == "" or form.EQUALITY.data == 'LIKE':
            formparams['EQUALITY'] = 'LIKE'
            formparams['FILTER'] = "%"

        formparams['SITE'] = form.SITE.data
        formparams['QTY'] = form.QTY.data

        sqlstr = queries.stockcheck(**formparams)
        df = t.runquery(sqlstr)

    numrows = df.shape[0]

    # dfcsv = df.to_csv(index=False, header=True, sep=",")
    # session["dfcsv"] = dfcsv

    res = t.conv_html(df)
    return render_template('stock.html', res=res, form=form, numrows=numrows)
