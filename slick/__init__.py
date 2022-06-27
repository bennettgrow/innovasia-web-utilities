import os
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    app.config.from_mapping(
        SECRET_KEY='reallllllllllllllly long key',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    Bootstrap(app)

    # Pass navbar info to every template
    @app.context_processor
    def inject_dict_for_all():
        nav = [
            {"text":"Home", "url":url_for('index')},
            {"text":"Stock", "url":url_for('stock')},
        ]
        return dict(navbar = nav)


    # Setup pages

    @app.route('/')
    def index():
        return render_template('index.html')

    from . import stock
    app.register_blueprint(stock.bp)
    app.add_url_rule('/stock', endpoint='stock')




    return app