from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"},
    {"name": "Отзывы", "url": "reviews"},
    {"name": "FAQ", "url": "FAQ"}
]


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О нас", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


@app.route("/reviews")
def reviews():
    return render_template('reviews.html', title="Отзывы", menu=menu)


@app.route("/FAQ")
def faq():
    return render_template('FAQ.html', title="FAQ", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
