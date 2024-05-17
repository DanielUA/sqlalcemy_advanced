import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from session import get_db
from models import Teacher, Student, TeacherStudent

fake = Faker()
session = next(get_db())

def insert_students():
    
    for _ in range(10):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)

def insert_teachers():
    for _ in range(6):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-5y')
        )
        session.add(teacher)

def insert_rel():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        rel = TeacherStudent(
            teacher_id=random.choice(teachers).id,
            student_id=student.id
        )
        session.add(rel)

if __name__ == '__main__':
    insert_students()
    insert_teachers()
    session.commit()
    insert_rel()
    session.commit()
    session.close()
