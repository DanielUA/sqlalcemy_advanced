from datetime import datetime
from sqlalchemy import and_, between
from sqlalchemy.orm import joinedload, subqueryload

from conf.session import get_db
from conf.models import Student, Teacher, TeacherStudent

session = next(get_db())

# def get_student_joinloaded():
#     # students = session.query(Student).options(joinedload(Student.teachers)).all()
#     students = session.query(Student).options(subqueryload(Student.teachers)).limit(5).offset(3).all()
#     for s in students:
#         columns = ['id', 'fullname', 'teachers']
#         r = {'id': s.id, 'fullname': s.fullname, 'teachers': []}
#         for t in s.teachers:
#             r['teachers'].append({'id': t.id, 'fullname': t.fullname})
#         print(r)

# def get_student_join():
#     students = session.query(Student).join(Student.teachers).all()
#     for s in students:
#         columns = ['id', 'fullname', 'teachers']
#         r = {'id': s.id, 'fullname': s.fullname, 'teachers': []}
#         for t in s.teachers:
#             r['teachers'].append({'id': t.id, 'fullname': t.fullname})
#         print(r)

# def get_techers():
#     teachers = session.query(Teacher).options(joinedload(Teacher.students, innerjoin=True)).all()
#     for t in teachers:
#         r = {'id': t.id, 'fullname': t.fullname, 'students': []}
#         for s in t.students:
#             r['students'].append({'id': s.id, 'fullname': s.fullname})
#         print(r)

# def get_techers_outerjoin():
#     # teachers = session.query(Teacher).outerjoin(Teacher.students).all()
#     teachers = session.query(Teacher).join(Teacher.students).all()
#     for t in teachers:
#         r = {'id': t.id, 'fullname': t.fullname, 'students': []}
#         for s in t.students:
#             r['students'].append({'id': s.id, 'fullname': s.fullname})
#         print(r)

def get_techers_by_data():
    # teachers = session.query(Teacher).options(
    #     joinedload(Teacher.students, innerjoin=True)
    #     ).filter(
    #         and_(
    #             Teacher.start_work >= datetime(year=2020, month=1, day=1),
    #              Teacher.start_work <= datetime(year=2021, month=12, day=31)
    #              )
                #   ).all()
    # teachers = session.query(Teacher).options(
    #     joinedload(Teacher.students, innerjoin=True)
    #     ).filter(
    #             Teacher.start_work.between(
    #                    datetime(year=2020, month=1, day=1),
    #                    datetime(year=2021, month=12, day=31)
    #              )
    #              ).all()

    # for t in teachers:
    #     r = {'id': t.id, 'fullname': t.fullname, 'start':t.start_work, 'students': []}
    #     for s in t.students:
    #         r['students'].append({'id': s.id, 'fullname': s.fullname})
    #     print(r)

def get_student_join():
    students = session.query(Student).join(Student.teachers).all()
    for s in students:
        columns = ['id', 'fullname', 'teachers']
        r = {'id': s.id, 'fullname': s.fullname, 'teachers': []}
        for t in s.teachers:
            r['teachers'].append({'id': t.id, 'fullname': t.fullname})
        print(r)


if __name__ == "__main__":
    # get_student_join()
    # get_student_joinloaded()
    # get_techers()
    # get_techers_outerjoin()
    # get_techers_by_data()