# -*- coding: utf-8 -*-
from configparser import ConfigParser

config = ConfigParser()


config['MySql_query'] = {
    'all_db' : "SELECT TABLE_SCHEMA FROM information_schema.tables where" \
              " TABLE_SCHEMA NOT IN ('sys', 'information_schema', 'performance_schema', 'mysql')"\
              " GROUP BY TABLE_SCHEMA;",
    'all_table' : "SELECT TABLE_NAME FROM information_schema.tables where" \
                  " TABLE_SCHEMA NOT IN ('sys', 'information_schema', 'performance_schema', 'mysql')"\
                  " AND TABLE_SCHEMA = '##DB_NAME##';",
    'table_field' : "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '##DB_NAME##' " \
                    " AND TABLE_NAME = '##TABLE_NAME##';",
}


with open('config.ini', 'w+') as file:
    config.write(file)