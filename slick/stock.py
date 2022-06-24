from flask import Blueprint, render_template, url_for
from . import tableutil as t

bp = Blueprint('stock',__name__)

@bp.route('/stock')
def stock():
    
    df = t.demodata()
    res = t.conv_html(df)
    print(res)
    return render_template('stock.html', res=res)
