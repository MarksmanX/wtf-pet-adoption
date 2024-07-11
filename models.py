"""Models for WTF-Pet-Adoption."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models for pets
class Pet(db.Model):
    """Pet model."""

    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f"<Pet>"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(25),
                     nullable=False)
    
    species = db.Column(db.String(25),
                        nullable=False)
    
    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    