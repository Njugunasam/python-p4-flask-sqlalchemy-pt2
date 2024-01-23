#!/usr/bin/env python3

#!/usr/bin/env python3

#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import create_app, db  # Import create_app function from app module
from models import Owner, Pet

fake = Faker()

# Create the Flask application using the create_app function
app = create_app()

# Use the app context to interact with the database
with app.app_context():
    # Clear existing data
    Pet.query.delete()
    Owner.query.delete()

    # Create owners
    owners = [Owner(name=fake.name()) for _ in range(50)]
    db.session.add_all(owners)

    # Create pets
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = [Pet(name=fake.first_name(), species=rc(species), owner=rc(owners)) for _ in range(100)]
    db.session.add_all(pets)

    # Commit changes
    db.session.commit()
