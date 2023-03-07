from flask import Flask, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
# from forms import ###

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# SECRET KEY
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_list_pets():
    """Render home page - a list of pets"""

    # Get pets from db
    all_pets = Pets.query.all()

    # Pass into template
    render_template("home.html", pets=all_pets)
