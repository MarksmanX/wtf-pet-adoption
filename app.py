from flask import Flask, render_template, redirect, flash, session, request
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'NOTsoSecRET'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def show_home_page():
    """Shows a home page with list of all pets."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add' , methods=['GET', 'POST'])
def show_add_form():
    """Shows the form to add a new pet."""
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data,
                  species=form.species.data,
                  age=form.age.data,
                  photo_url=form.photo_url.data,
                  notes=form.notes.data)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('/add_pet_form.html', form=form)
    

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Shows the detail for a specific pet."""
    pet = Pet.query.get_or_404(pet_id)
    form=PetForm(obj=pet)

    # Pre-populate the name and species so that they stay the same.
    if request.method == 'POST':
        # Explicitly set the name and species to their current values if not provided
        if not form.name.data:
            form.name.data = pet.name
        if not form.species.data:
            form.species.data = pet.species
            
    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        return redirect(f'/')
    else:
        print(form.errors)  # Print form errors to console
        if form.errors:
            flash('Form validation failed. Please correct the errors and try again.', 'danger')
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
        return render_template('pet_details.html', pet=pet, form=form)