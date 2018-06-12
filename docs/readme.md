Install Python
https://www.python.org/downloads/

Install Pipenv
https://docs.pipenv.org/basics/#general-recommendations-version-control

Create the web server

```
from flask import (
    Flask,
    render_template
)

app = Flask(__name__, template_folder="static")

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

```
