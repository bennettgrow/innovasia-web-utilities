import os
from flask import Flask, render_template, url_for, make_response, session
from flask_bootstrap import Bootstrap
from . import parser

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = parser.get_secret_key()

    Bootstrap(app)
    
    # Pass navbar info to every template
    @app.context_processor
    def inject_dict_for_all():
        nav = [
            {"text":"Home", "url":url_for('index')},
            {"text":"Stock", "url":url_for('stock')},
            {"text":"Lots", "url":url_for('lots')},
        ]
        return dict(navbar = nav)


    # Setup pages
    @app.route('/')
    def index():
        return render_template('index.html')

    from . import stock, lots

    app.register_blueprint(stock.bp)
    app.add_url_rule('/stock', endpoint='stock')

    app.register_blueprint(lots.bp)
    app.add_url_rule('/lots', endpoint='lots')

    @app.route('/download')
    def download():
        dfcsv = session["dfcsv"]
        resp = make_response(dfcsv)
        resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
        resp.headers["Content-Type"] = "text/csv"
        print('Download...')
        return resp


    return app