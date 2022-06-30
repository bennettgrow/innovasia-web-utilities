from configparser import ConfigParser
import os

def config(section, filename='config.ini'):
    # Configuration file parser

    # Find parent directory
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir = dir.replace('project','')

    # create a parser
    parser = ConfigParser()

    # Read ini file
    parser.read(dir + filename)

    # get section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def get_conn_str():
    section = 'odbc'
    params = config(section)
    conn_str = 'mssql+pyodbc:///?odbc_connect=DSN=' + params['dsn'] + ';UID=' + params['uid'] + ';PWD=' + params['pwd']
    return conn_str


def get_secret_key():
    params = config('flask')
    return params['secret_key']

def get_debug_mode():
    params = config('flask')
    val = params['debug']
    if val.lower() == 'false':
        return False
    else:
        return True
