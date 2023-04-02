from flask import Flask, render_template
import requests
app = Flask(__name__)


response = requests.get("https://api.npoint.io/6a763fd44db522817a35")
all_posts = response.json()

@app.route('/')
def index():
    return render_template("index.html", posts=all_posts)


@app.route('/about_page')
def about_page():
    return render_template('about.html')


@app.route('/contact_page')
def contact_page():
    return render_template('contact.html')

@app.route("/post/<int:id>")
def post_page(id):
    for blog_post in all_posts:
        if blog_post['id'] == id:
            post = blog_post

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)