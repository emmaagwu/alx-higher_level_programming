#!/usr/bin/python3
''' Adds a new state to the database '''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__" and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='Louisiana')
    session.add(state)
    new = session.query(State).filter_by(name='Louisiana').first()
    print(new.id)
    session.commit()
