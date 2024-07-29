#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def get_states():
    """Displays a html page that contains all states"""
    states = storage.all(State)
    return render_template("9-states.html", states=states, display="list")


@app.route("/states/<id>", strict_slashes=False)
def get_state(id):
    """Displays a html page that contains all cities of the given state"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template(
                "9-states.html", state=state, display="single"
            )

    # Not Found!
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Sessionn after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
