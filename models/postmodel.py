from db import db

class PostModel(db.Model):
    __tablename__ = "Posts"

    id = db.Column(db.Integer, primary_key = True) 
    userName = db.Column(db.String(99))
    title = db.Column(db.String(99))
    content = db.Column(db.Text)

    bookId = db.Column(db.Integer, db.ForeignKey("Books.id"), nullable=True)

    book = db.relationship("BookModel", back_populates="posts") ## facilita o referenciamento no codigo. 