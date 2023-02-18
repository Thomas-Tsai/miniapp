# main.py
 
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import text
import os

db = SQLAlchemy()
 
app = Flask(__name__)
# default
db_name = os.environ.get('DATABASE') 
db_user = os.environ.get('DBUSERNAME')
db_pass = os.environ.get('DBPASSWORD')
db_host = os.environ.get('DBHOST')
db_port = os.environ.get('DBPORT')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db.init_app(app)
 
@app.route('/')
def index():
 
    sql_cmd = "select number from numbers order by number DESC limit 5"
    engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    with engine.connect() as connection:
        query_data = connection.execute(text(sql_cmd)).fetchall()
        x = 'ok'
        for row in query_data:
            number = row[0]
            x = "{}, {}".format(x, number)

        return x
    return "nodata"
 
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
