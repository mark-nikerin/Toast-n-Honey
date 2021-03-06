from flask import render_template
from TnH_app import app
from TnH_app.models import *


@app.route("/")
def home():
    return render_template("home.html", title='Toast And Honey')


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html", title='О нас')


@app.route("/cheesecakes/")
def cheesecakes():
    cheesecakes = Products.query.filter(Products.typeId == 2).all()
    return render_template("products.html", title='Чизкейки', products=cheesecakes)


@app.route("/cakes/")
def cakes():
    cakes = Products.query.filter(Products.typeId == 1).all()
    return render_template("products.html", title='Торты', products=cakes)


@app.route("/macarons/")
def macarons():
    macarons = Products.query.filter(Products.typeId == 3).all()
    return render_template("products.html", title='Макарон', products=macarons)


@app.route("/desserts/")
def desserts():
    desserts = Products.query.filter(Products.typeId == 4).all()
    return render_template("products.html", title='Десерты', products=desserts)


@app.route("/delivery/")
def delivery():
    return render_template("delivery.html", title='Как заказать')


@app.route("/details/<int:id>")
def details(id):
    product = Products.query.filter(Products.id == id).first_or_404()
    return render_template("details.html", product=product)


@app.errorhandler(404)
def product_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def product_not_found(e):
    return render_template('404.html'), 500
