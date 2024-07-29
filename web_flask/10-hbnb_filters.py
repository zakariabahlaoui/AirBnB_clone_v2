#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, jsonify, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays hbnb filter html page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
        "10-hbnb_filters.html",
        states=states.values(),
        amenities=amenities.values(),
    )


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Sessionn after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
