from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__, static_url_path='/static')
Bootstrap(app)

@app.context_processor
def inject_dict_for_all():
    nav = [
        {"text":"Home", "url":url_for('index')},
        {"text":"Stock", "url":url_for('stock')},
    ]
    return dict(navbar = nav)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

if __name__ == "__main__":
    app.run(debug=True)