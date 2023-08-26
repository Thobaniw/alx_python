from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a connection to the MySQL server
DATABASE_URL = 'mysql://username:password@localhost:3306/database_name'
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define the State class


class State(Base):
    """
    Represents a state in the application.

    Attributes:
        id (int): An auto-generated, unique integer identifying the state.
        name (str): The name of the state, with a maximum length of 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Create the table in the database
Base.metadata.create_all(engine)

# Close the session
session.close()
