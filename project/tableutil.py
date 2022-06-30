import pandas as pd
from . import parser
from sqlalchemy import create_engine

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
