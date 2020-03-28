#!/usr/bin/python3
""" Write a script that prints the first State object,
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)
    Session = session().query(State).first()
    if Session:
        print("{}: {}".format(Session.id, Session.name))
    else:
        print("Nothing")
    session().close()
