from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/information')
def info():
    return '<h1>My name is siddhant</h1>'

if __name__ == '__main__':
    app.run()