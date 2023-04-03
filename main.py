from flask import Flask, render_template, request
import requests, smtplib
app = Flask(__name__)


response = requests.get("https://api.npoint.io/6a763fd44db522817a35")
all_posts = response.json()

my_email = "beknazar.ulanbekuuluu@mail.ru"
password = "DGjDj2QjrUDdxnGDabg3"

@app.route('/')
def index():
    return render_template("index.html", posts=all_posts)


@app.route('/about_page')
def about_page():
    return render_template('about.html')


@app.route('/contact_page', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        for key, value in request.form.items():
            print(f"{key}: {value}")

        with smtplib.SMTP("smtp.mail.ru") as connection:
            # secure our connection to email server
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data['email'],
                msg=f"Subject:Conversation\n\n {data['message']}"
            )

        return render_template('contact.html', data=data)
    return render_template('contact.html')

@app.route("/post/<int:id>")
def post_page(id):
    for blog_post in all_posts:
        if blog_post['id'] == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)