import flask
from db import db
from models.bookmodel import BookModel

def createBook():
    data = flask.request.json
    newbook = BookModel(name = data.get("name"))
    db.session.add(newbook)
    db.session.commit()
    return flask.jsonify({"Message":newbook.name}), 200 ### significa que deu certo

