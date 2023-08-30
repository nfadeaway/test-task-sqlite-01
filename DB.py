import sqlite3


class DB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create_summary_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS summary (
                 timestamp TEXT,
                 player_id INT,
                 event_id INT,
                 error_id INT,
                 json_server TEXT,
                 json_client TEXT
               );
            '''
        )
        self.conn.commit()

    def get_cheaters_rows(self):
        self.cur.execute('SELECT * FROM cheaters;')
        return self.cur.fetchall()

    def insert_rows_to_summary(self, args):
        self.cur.executemany('INSERT INTO summary VALUES(?, ?, ?, ?, ?, ?);', args)
        self.conn.commit()
