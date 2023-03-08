from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional
from wtforms.widgets import TextArea

class AddPetForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired(message="Name cannot be blank.")])
    species = StringField("Species", validators=[InputRequired(message="Species cannot be blank.")])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()], widget=TextArea())
    available = BooleanField("Available for adoption?")
