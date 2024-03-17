import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("database"),
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )

        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "update", "delete", "alter", "create", "drop"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return """
                      -----------------------------\n
                          INSERTED SUCCESSFUL
                      -----------------------------\n
                      """

            elif query_type == "update":
                return """
                      -----------------------------\n
                          UPDATED SUCCESSFUL
                      -----------------------------\n
                      """
            elif query_type == "delete":
                return """
                      -----------------------------\n
                          DELETED SUCCESSFUL
                      -----------------------------\n
                      """
            elif query_type == "alter":
                return """
                      -----------------------------\n
                          ALTER SUCCESSFUL
                      -----------------------------\n
                      """
            elif query_type == "create":
                return """
                      -----------------------------\n
                          CREATED SUCCESSFUL
                      -----------------------------\n
                      """

            elif query_type == "drop":
                return """
                      -----------------------------\n
                          DROP SUCCESSFUL
                      -----------------------------\n
                      """
        else:
            return cursor.fetchall()
