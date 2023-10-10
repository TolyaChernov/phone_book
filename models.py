from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# , DateTime, Float, Boolean, Text, LargeBinary
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
sesion = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    government = relationship('Government', secondary='users_governments', back_populates='user')
    department = relationship('Department', secondary='users_departments', back_populates='user')
    position = relationship('Position', secondary='users_positions', back_populates='user')
    phone = relationship('Phone', secondary='users_phones', back_populates='user')
    email = relationship('Email', secondary='users_emails', back_populates='user')

    def __str__(self):
        return self.name
    

class Government(Base):
    __tablename__ = 'governments'
    id = Column(Integer, primary_key=True)
    government = Column(String, nullable=True)
    user = relationship('User', secondary='users_governments', back_populates='government')

    def __str__(self):
        return self.government
    
    @classmethod
    def add_government(cls, government):
        new_government = cls(government=government)
        sesion.add(new_government)
        sesion.commit()
        return new_government
    
class UserGovernment(Base):
    __tablename__ = 'users_governments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    government_id = Column(Integer, ForeignKey('governments.id'), primary_key=True)



class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    department = Column(String, nullable=True)
    user = relationship('User', secondary='users_departments', back_populates='departments')

    def __str__(self):
        return self.department


class UserDepartment(Base):
    __tablename__ = 'users_departments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.id'), primary_key=True)


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    position = Column(String, nullable=True)
    user = relationship('User', back_populates='positions')

    def __str__(self):
        return self.position


class UserPosition(Base):
    __tablename__ = 'users_positions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    position_id = Column(Integer, ForeignKey('positions.id'), primary_key=True)


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=True)
    user = relationship('User', secondary='users_phones', back_populates='phones')

    def __str__(self):
        return self.phone


class UserPhone(Base):
    __tablename__ = 'users_phones'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    phone_id = Column(Integer, ForeignKey('phones.id'), primary_key=True)


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True)
    user = relationship('User', secondary='users_emails', back_populates='emails')

    def __str__(self):
        return self.email


class UserEmail(Base):
    __tablename__ = 'users_emails'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    email_id = Column(Integer, ForeignKey('emails.id'), primary_key=True)


Base.metadata.create_all(engine)
