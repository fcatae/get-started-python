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
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)