from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/rules', strict_slashes=False)
def about():
    return render_template("rules.html")


if __name__ == '__main__':
    app.run(debug=True)