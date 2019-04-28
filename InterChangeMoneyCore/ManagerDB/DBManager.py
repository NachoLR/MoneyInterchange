# coding=utf-8

#Default imports
import os
import sys
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DBManager(object):
    """
    This class manage all operations over DB
    """

    _sql_create_table = """ CREATE TABLE `MoneyInterchange` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            `name`	TEXT NOT NULL,
                            `amount_money` INTEGER NOT NULL
                                        
                        );"""


    # ========================================
    #               Constructor
    # ========================================

    def __init__(self):
        """
        In the beginning, it is checked if the database exists

        """
        self.db_path = os.path.join(os.getcwd(), "InterChangeMoneyCore/DB/interchangeDB.db")
        print(os.getcwd())
        if not os.path.exists(self.db_path):
            #If the database does not exist, we proceed to create it and create the necessary tables
            self._createTable()

    # ========================================
    #           Private Methods
    # ========================================

    def _connectDB(self):
        return sqlite3.connect(self.db_path)

    def _createTable(self):
        """
        If Local Db was created on runtime
        create tables needed

        :return: None
        """
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(self._sql_create_table)



    # ========================================
    #           Public Methods
    # ========================================

    def InsertData(self, user_name):
        """
        Try to insert data into a DB and return id primary key
        :return:
        """
        sql = '''INSERT INTO MoneyInterchange(name,amount_money) VALUES(?,?)'''
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(sql, (str(user_name), 0))
        conn.commit()
        return int(c.lastrowid)


    def UpdateData(self, id, amount_money):
        """Try update data into DB"""
        sql = '''UPDATE MoneyInterchange set amount_money = ? where id = ?'''
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(sql, (amount_money, id))
        conn.commit()



    def GetData(self, id):
        """
        Try to get data from DB

        :return:
        """
        sql = '''SELECT * from MoneyInterchange where id = ?'''
        conn = self._connectDB()
        conn.row_factory = dict_factory
        c = conn.cursor()
        query_result = c.execute(sql, (id,))
        for result in query_result.fetchall():
            return result
        else:
            return None




