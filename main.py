from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", )


@app.route('/about_page')
def about_page():
    return render_template('about.html')


@app.route('/contact_page')
def contact_page():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)