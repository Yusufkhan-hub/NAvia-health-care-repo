import os
import pandas
import pymysql
from pymysql import cursors
from sqlalchemy import create_engine
import logging
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
try:
    data = pandas.read_csv(os.path.join(BASE_DIR, "meddata.csv"))
    print(data)
except Exception as e:
    print(e)

password=''
db_data = "mysql+mysqldb://root:"+password+"@localhost:3306/navia_health_care_db"
print("after db_data")
db_uri = os.environ.get(db_data)
engine = create_engine(db_data)
print("connected succes..")
# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="navia_health_care_db"
# )

# cursor =connection.cursor()

data.to_sql(name='primary_medicine_details',con=engine,if_exists='append',index=False)
print("connected")