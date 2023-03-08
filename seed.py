from models import Pet, db
from app import app

# Delete all tables
db.drop_all()
# Create all tables
db.create_all()

Pet.query.delete()

# Add sample pets

Ladybird = Pet(name= 'LadyBird', species='Dog', photo_url='/static/Ladybird.JPG', age='6', available=False)
Tank = Pet(name= 'Tank', species='Dog', photo_url='/static/Tank.jpeg', age='7', available=True, notes="A very good boy!")
Pepper = Pet(name= 'Pepper', species='Dog', photo_url='/static/Pepper.JPG', age='6')
Percy = Pet(name= 'Percy', species='Dog', photo_url='/static/Percy.JPG', age='3')
Wesson = Pet(name= 'Wesson', species='Dog', photo_url='/static/Wesson.jpeg', age='7')

db.session.add_all([Ladybird, Tank, Pepper, Percy, Wesson])
db.session.commit()
