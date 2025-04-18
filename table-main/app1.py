from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


@app.route("/")
def home():
    return render_template('index1.html', users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)