import sqlite3

DB_NAME = 'database.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute(
    '''
        CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
    '''
)
conn.cursor().execute(
    '''
        CREATE TABLE IF NOT EXISTS task_status
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT UNIQUE NOT NULL
            )
    '''
)
conn.cursor().execute(
    '''
        INSERT INTO task_status
        VALUES (1, 'TO DO')
    '''
)
conn.cursor().execute(
    '''
        INSERT INTO task_status
        VALUES (2, 'DOING')
    '''
)
conn.cursor().execute(
    '''
        INSERT INTO task_status
        VALUES (3, 'DONE')
    '''
)
conn.cursor().execute(
    '''
        CREATE TABLE IF NOT EXISTS task_type
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL
            )
    '''
)
conn.cursor().execute(
    '''
        CREATE TABLE IF NOT EXISTS tasks
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                content TEXT NOT NULL,
                task_status_id INTEGER NOT NULL,
                task_type_id INTEGER NOT NULL,
                FOREIGN KEY(task_status_id) REFERENCES task_status(id),
                FOREIGN KEY(task_type_id) REFERENCES task_type(id)
            )
    '''
)
conn.commit()


class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
