import psycopg2 as db
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def connect(query, type):
       database = db.connect(
           database = os.getenv("DB_NAME"),
           host = os.getenv("DB_HOST"),
           user = os.getenv("DB_USER"),
           password = os.getenv("DB_PASSWORD")
       )
       cursor = database.cursor()
       cursor.execute(query)
       data_type = ["insert", "create", "update", "delete", "drop"]
       if type in data_type:
           database.commit()
        #    print("dhjashs")
           if type == "create":
                return "Created Successfull"
       else:
        #    print("dadsss")
           return cursor.fetchall()
