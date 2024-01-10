from random import choice as rc

from faker import Faker

from app import app
from models import db, Animal, Zookeeper, Enclosure

db.init_app(app)

fake = Faker()

with app.app_context():

    Animal.query.delete()
    Zookeeper.query.delete()
    Enclosure.query.delete()

    enclosures = []
    for n in range(3):
        enclosure = Enclosure(environment=rc(['grass', 'sand', 'water']), open_to_visitors=rc([True, False]))
        enclosures.append(enclosure)

    db.session.add_all(enclosures)

    zookeepers = []
    for n in range(5):
        zookeeper = Zookeeper(name=fake.name(), birthday=fake.date_of_birth())
        zookeepers.append(zookeeper)

    db.session.add_all(zookeepers)

    animals = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    for n in range(20):
        animal = Animal(name=fake.first_name(), species=rc(species), zookeeper_id=rc(zookeepers).id, enclosure_id=rc(enclosures).id)
        animals.append(animal)

    db.session.add_all(animals)

    db.session.commit()