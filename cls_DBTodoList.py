import sqlite3 as sq


class DbWork:
    def __init__(self, db_location='./todo_base.db'):
        self.__db_location = db_location
        self.__con = sq.connect(db_location)
        # self.__cur = self.__con.cursor()

    def __enter__(self):
        self.__cur = self.__con.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cur.close()
        if isinstance(exc_val, Exception):
            self.__con.rollback()
        else:
            self.__con.commit()
        self.__con.close()

    def create_table(self, name_new_table):
        query = f'CREATE TABLE IF NOT EXISTS {name_new_table} (id_do INTEGER PRIMARY KEY AUTOINCREMENT, name_do TEXT)'
        self.__cur.execute(query)

    def delete_table(self, name_delete_table):
        query = f'DROP TABLE IF EXISTS {name_delete_table}'
        self.__cur.execute(query)

    def clear_table(self, name_table):
        query = f"SELECT * FROM sqlite_master where name='{name_table}'"
        exists_table = self.__cur.execute(query)
        if exists_table:
            query = f'DELETE FROM {name_table}'
            self.__cur.execute(query)
            return True
        return False

    def insert_into_table(self, name_table, data_for_insert: list):
        query = f"SELECT * FROM sqlite_master where name='{name_table}'"
        exists_table = self.__cur.execute(query)
        if exists_table:
            query = f'INSERT INTO {name_table} VALUES (?, ?)'
            self.__cur.executemany(query, data_for_insert)

    def read_all_from_table(self, name_table):
        query = f"SELECT * FROM sqlite_master where name='{name_table}'"
        exists_table = self.__cur.execute(query)
        if exists_table:
            query = f"SELECT * FROM {name_table}"
            return self.__cur.execute(query)
        return []
