from datetime import datetime

from sqlalchemy import create_engine, desc, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(255))

    def __repr__(self) -> str:
        return f"<Student {self.id}: {self.name}>"