from src.database import database_connection
from src.entities.tip import Tip

def get_tip_by_row(row):
    return Tip(row['title'], row['url'], row['description'], row['user_id'], row['visible']) if row else None

class TipRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_tip(self, title, url, description, user_id, visible=1):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tip (url, description, user_id, title, visible)" \
            " VALUES (?, ?, ?, ?, ?)", (url, description, user_id, title, visible))
        self.connection.commit()

    def get_tips(self):
        """Palauttaa kaikki lukuvinkit listana"""

        cursor = self.connection.cursor()
        sql = """SELECT title, url, description, user_id, visible FROM Tip"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        return list(map(get_tip_by_row, rows))

tip_repository = TipRepository(database_connection)