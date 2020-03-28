#!/usr/bin/python3
""" safe from MySQL injection """
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
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(cmd, (argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()