# app.py
from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_object(__name__)

flatpages = FlatPages(app)
freezer = Freezer(app)


from routes import register_routes

if __name__ == "__main__":
    register_routes()
    app.run(host='0.0.0.0', debug=True)
