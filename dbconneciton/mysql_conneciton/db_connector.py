# -*- coding: utf-8 -*-
import logging
import mysql.connector
from typing import Any
from mysql.connector.errors import Error
from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read('../PYENTITY/config.ini')

QUERY = CONFIG['MySql_query']

def not_null(x: Any):
    assert isinstance(x, str)
    x = x.strip()
    assert len(x) > 0
    return x


class MysqlTableInfo:
    def __init__(self, user_host: str, user_name: str, user_password: str) -> None:
        try:
            with mysql.connector.connect(
                host=not_null(user_host),
                user=not_null(user_name),
                password=not_null(user_password),
            ) as connection:
                print(connection)
        except Error as e:
            logging.exception(f'Error, {e}')
            raise e

    
    def get_all_database_name(self):
        query = QUERY["all_db"]
        with self.mydb.cursor() as mycursor:
            mycursor.execute(query)
            database_name = mycursor.fetchall()
        return MysqlTableInfo.to_list(database_name)

    def get_table_name(self, db_name: str):
        db_name = not_null(db_name)
        query = QUERY['all_table'].replace('##DB_NAME##', db_name)
        with self.mydb.cursor() as mycursor:
            mycursor.execute(query)
            table_names = mycursor.fetchall()
        return MysqlTableInfo.to_list(table_names)

    def get_field_name(self, db_name: str, table_name: str):
        db_name = not_null(db_name)
        table_name = not_null(table_name)
        query = QUERY['table_filed'].replace('##DB_NAME##', db_name).replace('##TABLE_NAME##', table_name)
        with self.mydb.cursor() as mycursor:
            mycursor.execute(query)
            table_field = mycursor.fetchall()
        return table_field

    @staticmethod
    def to_list(db_list: list):
        db_list = [item[0] for item in db_list]
        return db_list 


