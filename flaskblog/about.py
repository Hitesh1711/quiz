from flask import  Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "<h2>Hellogggg World</h2>"


@app.route("/about")
def about():
    return "<h2>About This project is in starting stage</h2>"

if __name__ == '__main__':
    app.run(debug=True) 