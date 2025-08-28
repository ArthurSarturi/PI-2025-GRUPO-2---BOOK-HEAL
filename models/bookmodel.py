from db import db

class BookModel(db.Model):
    __tablename__ = "Books"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(99))

    posts = db.relationship("PostModel", back_populates="book", cascade="all, delete-orphan")