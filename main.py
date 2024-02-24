# import psycopg2 as psql
# import os
# from dotenv import load_dotenv

# class Database:
#     @staticmethod
#     def connect(query):
#         db = psql.connect(
#             database = os.getenv("db_name"),
#             host = os.getenv("db_host"),
#             user = os.getenv("db_user"),
#             password = os.getenv("db_password")
#         )
#         cursor = db.cursor()
#         cursor.execute(query)
#         db.commit()
#         return "create"
    
# if __name__ == "__main__":
#     query = """DROP TABLE kasalxona"""
#     data = Database.connect(query)
#     print(data)
