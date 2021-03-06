from flask import (
    Flask,
    render_template,
    json,
    request
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


@app.route('/json')
def getjson():
    return json.dumps({'a':'123'})


@app.route('/show2')
def show2():
    return json.dumps({'a':1})

@app.route('/show', methods=['POST'])
def show():
    print (request.get_json())

    return json.dumps( request.json['name'] )

if __name__ == '__main__':
    app.run(debug=True)