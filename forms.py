from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Optional, URL, AnyOf

class PetForm(FlaskForm):
    """Pet form."""

    name=StringField("Pet Name", validators=[InputRequired(message="Pet name can't be blank.")])
    species=StringField("Species", validators=[InputRequired(message="Species is required."), AnyOf(values=["cat", "porcupine", "dog"], message="This must be either cat, porcupine or dog.")])
    photo_url=StringField("Photo URL", validators=[Optional(), URL(message="This must be a URL.")])
    age=IntegerField("Age (in years)", validators=[
        Optional(),
        NumberRange(min=1, max=30, message="Value must be between 1 and 100.")])
    notes=StringField("Notes")
    available=BooleanField("Available")
