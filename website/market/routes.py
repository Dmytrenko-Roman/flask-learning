from flask import render_template, redirect, url_for, flash, get_flashed_messages

from market import app, db
from market.models import Item, User
from market.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/home')
def home_page() -> str:
    values = {
        'home': 'active',
        'market': '',
        'register': '',
        'login': '',
    }
    return render_template('home.html', **values)


@app.route('/market')
def market_page() -> str:
    values = {
        'home': '',
        'market': 'active',
        'register': '',
        'login': '',
        'items': Item.query.all(),
    }

    return render_template('market.html', **values)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    values = {
        'home': '',
        'market': '',
        'register': 'active',
        'login': '',
        'form': form,
    }

    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data,
        )

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('market_page'))

    if any(form.errors):
        for err_msg in form.errors.values():
            flash(f'There was an error with creating user {err_msg}', category='danger')

    return render_template('register.html', **values)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    values = {
        'home': '',
        'market': '',
        'register': '',
        'login': 'active',
        'form': form,
    }

    return render_template('login.html', **values)
