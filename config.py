"""Configuration file
    """
from sqlalchemy import create_engine, Column, ForeignKey, Integer, Table
from sqlalchemy.ext.declarative import declarative_base

MY_USER, MY_PWD, MY_HOST, MY_DB = \
    'orm_learning_user', 'orm_learning_pwd', 'localhost', 'orm_learning_db'

engine = create_engine(
    f'mysql+mysqldb://{MY_USER}:{MY_PWD}@{MY_HOST}/{MY_DB}',
    pool_pre_ping=True
)
Base = declarative_base()

event_campus = Table('event_campus', Base.metadata,
                     Column('event_id', Integer, ForeignKey(
                         'event.id'), primary_key=True),
                     Column('campus_id', Integer, ForeignKey(
                         'campus.id'), primary_key=True)
                     )

event_cohort = Table(
    'event_cohort', Base.metadata,
    Column('event_id', Integer, ForeignKey('event.id'), primary_key=True),
    Column('cohort_id', Integer, ForeignKey('cohort.id'), primary_key=True)
)
