import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Check if the script is being run directly, not imported
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python script_name.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connection to the MySQL server
    DATABASE_URL = f"mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"
    engine = create_engine(DATABASE_URL)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
