from models import Pet, db
from app import app

# Delete all tables
db.drop_all()
# Create all tables
db.create_all()

Pet.query.delete()

# Add sample pets

Ladybird = Pet(name= 'LadyBird', species='Dog', photo_url='/Ladybird.JPG', age='6', available=False)
Tank = Pet(name= 'Tank', species='Dog', photo_url='/Tank.jpeg', age='7', available=True)
Pepper = Pet(name= 'Pepper', species='Dog', photo_url='/Pepper.JPG', age='6')
Percy = Pet(name= 'Percy', species='Dog', photo_url='/Percy.JPG', age='3')
Wesson = Pet(name= 'Wesson', species='Dog', photo_url='/Wesson.jpeg', age='7')

db.session.add_all([Ladybird, Tank, Pepper, Percy, Wesson])
db.session.commit()
