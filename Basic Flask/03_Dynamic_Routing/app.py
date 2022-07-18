
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/information')
def info():
    return '<h1>My name is siddhant</h1>'

@app.route('/your_name/<path:name>')
def puppy(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name)

if __name__ == '__main__':
    app.run()