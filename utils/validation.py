#!/usr/bin/python3
""" create ORM for login page """


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    # Define the database connection
    engine = create_engine('mysql://group1:med-info1@localhost/health_web_service', echo=True)

    # Define a Base class
    Base = declarative_base()

    # Define the User model
    class User(Base):
        __tablename__ = 'uniqueid'
        id = Column(Integer, primary_key=True, autoincrement=True)
        uniqueid = Column(String(6))

    # Create a session
    Session = sessionmaker(bind=engine)

    def insert_user_to_db(uniqueid):
    """ Create a new User instance and add to the session """
        try:
            session = Session()
            new_user = User(uniqueid=uniqueid)
            session.add(new_user)
            session.commit()
            return "User added successfully"
        except Exception as e:
            session.rollback()
            return "Error adding user: " + str(e)
        finally:
            session.close()
