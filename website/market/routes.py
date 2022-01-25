from flask import render_template

from market import app
from market.models import Item


@app.route('/')
@app.route('/home')
def home_page() -> str:
    values = {
        'home': 'active',
        'market': '',
    }
    return render_template('home.html', **values)


@app.route('/market')
def market_page() -> str:
    values = {
        'home': '',
        'market': 'active',
        'items': Item.query.all(),
    }

    return render_template('market.html', **values)
