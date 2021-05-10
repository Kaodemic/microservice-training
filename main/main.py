# save this as app.py
from flask import Flask, escape, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.sql.schema import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "mysql://root:root@db/main"
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Interger)

    UniqueConstraint('user_id', "product_id", name='user_product_unique')


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
