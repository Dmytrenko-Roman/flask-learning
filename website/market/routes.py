from flask import render_template, redirect, url_for, flash, get_flashed_messages

from market import app, db
from market.models import Item, User
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page() -> str:
    values = {
        'home': 'active',
        'market': '',
        'register': '',
    }
    return render_template('home.html', **values)


@app.route('/market')
def market_page() -> str:
    values = {
        'home': '',
        'market': 'active',
        'register': '',
        'items': Item.query.all(),
    }

    return render_template('market.html', **values)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    # values = {
    #     'home': '',
    #     'market': '',
    #     'register': 'active',
    # }

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email=form.email.data, password_hash=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('market_page'))


    if any(form.errors):
        for err_msg in form.errors.values():
            flash(f'There was an error with creating user {err_msg}')
        

    return render_template('register.html', form=form)
