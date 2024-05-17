from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    students = relationship(
        'Student', 
        secondary='teacher_to_students', 
        back_populates='teachers'
        )
    
    @hybrid_property
    def fullname(self):
        return self.first_name + ' ' + self.last_name


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    teachers = relationship(
        'Teacher', 
        secondary='teacher_to_students', 
        back_populates='students'
        )
    
    @hybrid_property
    def fullname(self):
        return self.first_name + ' ' + self.last_name

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    student_id = Column(ForeignKey(
        'students.id', 
        ondelete='CASCADE', 
        onupdate='CASCADE'
            ))
    student = relationship('Student', backref='contacts') 

    @hybrid_property
    def fullname(self):
        return self.first_name + ' ' + self.last_name


class TeacherStudent(Base):
    __tablename__ = 'teacher_to_students'
    id = Column(Integer, primary_key=True)
    
    teacher_id = Column(
        Integer, 
        ForeignKey(
            'teachers.id', 
            ondelete='CASCADE', 
            onupdate='CASCADE'
            ))
    student_id = Column(
        Integer, 
        ForeignKey(
            'students.id', 
            ondelete='CASCADE', 
            onupdate='CASCADE'
            ))
