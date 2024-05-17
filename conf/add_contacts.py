import random
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from session import get_db
from models import Contact, Student

fake = Faker()
session = next(get_db())

def insert_contacts():
    students = session.query(Student).all()

    for _ in range(len(list(students)) + 7):
        contact = Contact(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        email = fake.email(),
        phone = fake.phone_number(),
        student_id = random.choice(students).id
        )
        session.add(contact)

if __name__=="__main__":
    try: 
        insert_contacts()
        session.commit()
    except SQLAlchemyError as er:
        print(er)
        session.rollback()
    finally:
        session.close()