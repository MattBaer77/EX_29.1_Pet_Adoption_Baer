from flask import Flask, render_template, flash, redirect
from sneakybeaky import SECRET_GEORGE
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = SECRET_GEORGE
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_list_pets():
    """Render home page - a list of pets"""

    # Get pets from db
    pets = Pet.query.all()

    # Pass into template
    return render_template("home.html", pets=pets)

@app.route('/add')
def add_pet():
    """Render a page with a form to add a pet"""

    form = AddPetForm()

    # if form.validate_on_submit():
    #     name = form.name.data
    #     species = form.species.data
    #     photo_url = form.photo_url.data
    #     age = form.age.data
    #     notes = form.notes.data
    #     available = form.available.data

    #     flash(f"{name} has been added to the list!")

    #     return redirect('/')

    # else:
    #     return render_template("add.html", form=form)

    return render_template("add.html", form=form)

