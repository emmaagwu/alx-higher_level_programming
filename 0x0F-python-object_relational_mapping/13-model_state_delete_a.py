#!/usr/bin/python3
''' Deletes states in the database containing the letter a '''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__" and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in to_delete:
        session.delete(state)

    session.commit()
