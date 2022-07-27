import pandas as pd
from . import parser
from sqlalchemy import create_engine
from flask import make_response

def conv_html(df):
    # Given a DataFrame, returns a html bootstrap table 
    return df.to_html(classes=['table', 'table-hover', 'table-bordered', 'border-secondary', 'table-sm'], justify='center', index=False)

def demodata():
    # Returns 'demo.csv' as a DataFrame
    return pd.read_csv('demo.csv')

def runquery(sqlstr):
    # Returns a DataFrame with the result of the sqlstr query
    connectstring = parser.get_conn_str()
    engine = create_engine(connectstring)
    df = pd.read_sql_query(sql=sqlstr, con=engine)
    return df

def download_csv(df, filename):
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    resp.headers["Content-Type"] = "text/csv"
    return resp
