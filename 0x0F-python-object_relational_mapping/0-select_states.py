#!/usr/bin/python3
""" Config Sql 3 Argv connect, list user and id """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)