#!/usr/bin/python3
'''This module executes an SQLAlchemy SQL search'''

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__" and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
