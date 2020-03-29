#!/usr/bin/python3
""" Write a Python file similar to model_state.py named,
model_city.py that contains the class definition of a City
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)()
    states = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all()
    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
