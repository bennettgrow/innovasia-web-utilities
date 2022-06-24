from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__, static_url_path='/static')
Bootstrap(app)

@app.context_processor
def inject_dict_for_all():
    nav = [
        {"text":"Home", "url":url_for('index')},
        {"text":"Stock", "url":url_for('stock')},
        {"text":"About", "url":url_for('about')},
    ]
    return dict(navbar = nav)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)