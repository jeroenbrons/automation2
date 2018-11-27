import sqlite3, random
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def buildDB():
    cur = conn.cursor()
    try:
        query = cur.execute(
        """SELECT * FROM nummers""")
    except:
        cur.execute(''' 
    CREATE TABLE nummers (getal INTEGER);
     ''')
def genrng():
    cur = conn.cursor()
    for i in range(1000):
        rng=int(random.randrange(0, 500))
        strrng=str(rng)
        sql = " INSERT INTO nummers VALUES ("+ strrng+");"

        cur.execute(sql)
    conn.commit()

database = "rng.sqlite"


# create a database connection
conn = create_connection(database)
buildDB()
genrng()
