import time
import random
import os

from sqlalchemy import create_engine
from sqlalchemy import text

# default
db_name = os.environ.get('DATABASE')
db_user = os.environ.get('DBUSERNAME')
db_pass = os.environ.get('DBPASSWORD')
db_host = os.environ.get('DBHOST')
db_port = os.environ.get('DBPORT')

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
engine = create_engine(db_string, echo=True)
print(db_string)

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    print(n)
    query = "INSERT INTO numbers (number,timestamp) VALUES (:number, :time)"

    with engine.connect() as conn:
        conn.execute(text(query), {"number": n, "time": n})
        conn.commit()

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT number " + \
            "FROM numbers " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" +\
            "LIMIT 1"

    with engine.connect() as conn:
        result_set = conn.execute(text(query))
        for (r) in result_set:
            return r[0]

if __name__ == '__main__':
    print('Application started')

    while True:
        add_new_row(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))
        time.sleep(50)

