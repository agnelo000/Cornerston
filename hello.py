from flask import Flask, render_template, url_for


posts = [
    {
        'author': 'Agnelo',
        'title': 'how to alienate people',
        'content': 'shitpost',
        'date_published': 'jan 30'
    },
    {
        'author': 'Vikram singh',
        'title': 'bobs and vagena',
        'content': 'shitpost',
        'date_published': 'feb 30'

    }
]
app = Flask(__name__)

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About Page')

if (__name__ == "__main__"):
    app.run(debug=True)