import sqlite3

class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, db_name) -> None:
        self.db_name = db_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    
    def init_table(self):
        self.open()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS question (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            question TEXT, max_score INTEGER, correct_answer TEXT, incorrect_answer TEXT)''')
        self.close()
    
    def init_data(self):
        self.open()
        data = [
            ("В якому році Україна стала незалежна?", 1, "Денис", "Мікаель"),
            ("Який зараз рік?", 2, "2024", "1924"),
            ("Скільки у людини хромосом?", 3, "46", "47"),
            ("На якій планеті ви знаходитесь?", 4, "Денис", "Мікаель"),
            ("Який зараз час?", 5, "2024", "1924"),
            ("Скільки мені років?", 6, "46", "47")
        ]
        self.cursor.executemany(
            '''INSERT INTO question (question, max_score, correct_answer, 
            incorrect_answer) VALUES (?, ?, ?, ?)''', data
            )
        self.conn.commit()
        self.close()
    def get_data(self, max_score = 1):
        self.open()
        self.cursor.execute(
            '''SELECT * FROM question WHERE max_score == ?''', str(max_score)
            )
        data = self.cursor.fetchall()
        self.close()
        return data

    def close(self):
        self.cursor.close()
        self.conn.close()

db = DB_Controller('question.db')
# db.init_table()
# db.init_data()
# db.get_data()
# db.close()