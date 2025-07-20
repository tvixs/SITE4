from flask import Flask, render_template

app = Flask(__name__)

# Список товаров
products = [
    {"name": "Футболка", "price": 45},
    {"name": "Куртка", "price": 120},
    {"name": "Джинсы", "price": 90}
]

@app.route('/')
def index():
    return render_template("index.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
