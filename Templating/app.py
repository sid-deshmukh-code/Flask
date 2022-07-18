from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    puppies = ['Fluffy', 'Rufus', 'Spike', 'p','r','o','g','r','a','m','i','z']
    return render_template('index.html',
                           puppies=puppies)



if __name__ == '__main__':
    app.run(debug=True)