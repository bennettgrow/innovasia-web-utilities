from flask import url_for
import pandas as pd


def table_init():
    df = pd.DataFrame()

    return df

def filter():
    pass

def conv_html(df):
    return df.to_html(classes=['table','table-striped', 'table-hover', 'table-bordered'], justify='center', index=False)

def demodata():
    return pd.read_csv('demo.csv')

