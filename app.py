from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hero():
    return render_template('Hero.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login') 
def login():
    return render_template('entrar.html')

@app.route('/forum')
def forum():
    return render_template('Forum.html')

if __name__ == '__main__':
    app.run()
