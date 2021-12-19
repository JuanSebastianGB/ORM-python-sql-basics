#!/usr/bin/env python3
"""Orm learning
    """
from config import Base, engine
from sqlalchemy.orm import sessionmaker
from models.user import User

if __name__ == '__main__':
    """Main function
    """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(
        User(name='Name Test', email='Something@gmail.com', company='Only test'))
    session.commit()
    users = session.query(User).all()
    [print(f'Id: {user.id}, {user.name}')for user in users]
    session.close()
