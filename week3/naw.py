import sqlite3
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
        """SELECT * FROM naw""")
    except:
        cur.execute(''' 
     CREATE TABLE  naw (
     id integer PRIMARY KEY,
     naam text,
     adres text, 
     woonplaats text
     );
     ''')


def addaddr():
    cur = conn.cursor()
    name=input("naam?")
    adr=input("adres?")
    wp=input("woonplaats?")
    sql = """ INSERT INTO naw (naam, adres, woonplaats) VALUES (?,?,?);"""
    cur.execute(sql, (name, adr, wp))
    conn.commit()

# create a database connection

database = "naw.sqlite"
conn = create_connection(database)
buildDB()
addaddr()
