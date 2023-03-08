from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange
from wtforms.widgets import TextArea

class AddPetForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired(message="Name cannot be blank.")])
    species = SelectField("Species", choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Porcupine', 'Porcupine')], validators=[InputRequired(message="Choose a species."), AnyOf(['Cat','Dog','Porcupine'], 'Must be either a Cat, Dog, Or Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(False,"Must be a valid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(0, 30, "Must be a number between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()], widget=TextArea())
    available = BooleanField("Available for adoption?")

class EditPetForm(FlaskForm):

    notes = StringField("Notes", validators=[Optional()], widget=TextArea())
    available = BooleanField("Available for adoption?")
