from typing import NoReturn

from flask_login import UserMixin

from market import db, bcrypt, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=0)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password(self) -> str:
        return self.password


    @property
    def prettier_budget(self) -> str:
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{self.budget}$' 


    @password.setter
    def password(self, plain_text_password: str) -> NoReturn:
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode(
            'utf-8'
        )


    def check_password(self, attempted_password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Item {self.name}'


@login_manager.user_loader
def load_user(user_id: int) -> User:
    return User.query.get(int(user_id))
