from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    all_posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<num>')
def post(num):
    all_posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("post.html", posts=all_posts, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
