import flask
from db import db
from models.postmodel import PostModel

def createPost():
    data = flask.request.json

    newPost = PostModel(
        title = data.get("title"),    
        userName = data.get("userName"),
        content = data.get("content"),
        bookId = data.get("bookId")
    )

    db.session.add(newPost)
    db.session.commit()
    return flask.jsonify({"Message":newPost.title}), 200 ### significa que deu certo

def createPostForm():
    data = flask.request.form
    
    newPost = PostModel(
        title = data.get("title"),    
        userName = data.get("userName"),
        content = data.get("content"),
        bookId = data.get("bookId") if data.get("bookId") else None
    )

    db.session.add(newPost)
    db.session.commit()
    return flask.redirect('/forum')

def viewAllPosts():
    data = PostModel.query.all()
    return flask.jsonify([
        {
        
        "id":u.id,
        "userName":u.userName,
        "title":u.title,
        "content":u.content,
        "bookId":u.bookId

        } for u in data
    ])