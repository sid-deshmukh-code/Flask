# Set up your imports here!
# import ...

from flask import Flask
app = Flask(__name__)



@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Welcome</h1>"

@app.route('/puplatin/<path:name>') # Fill this in!
def puppylatin(name):
    pupname = ""
    if name.endswith("y"):
        pupname = name[:-1]
        return f"<h2>{pupname}iful</h2>"
    else:
        return f"<h3>{name}y</h3>"

if __name__ == '__main__':
   app.run(debug=True)