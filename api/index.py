# index.py
from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_object(__name__)

flatpages = FlatPages(app)
freezer = Freezer(app)

# Import routes from a separate file
from routes import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
