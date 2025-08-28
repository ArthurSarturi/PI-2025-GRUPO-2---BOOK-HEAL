from flask import Flask, render_template
from routes.bookroutes import book_bp
from routes.postroutes import Post_bp
from db import db

app = Flask(__name__)
app.register_blueprint(book_bp)
app.register_blueprint(Post_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models.bookmodel import BookModel
from models.postmodel import PostModel

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
