#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Fetch cities in passed in state id if provided, all if not """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states,
                            cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """ close SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
