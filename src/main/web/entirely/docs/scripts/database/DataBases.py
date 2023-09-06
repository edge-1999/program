import re

import pandas as pd
import pymysql
from pymysql.cursors import DictCursor
from sqlalchemy import create_engine


class OperationMysqlData(object):
    """采用视图传递数据，需要预先处理视图数据，此过程包括数据清洗"""

    def __init__(self, engine):
        self.engine = engine
        if self.engine['DATABASE'] == 'MYSQL':
            self.HOST = self.engine["MYSQL_HOST"]
            self.PORT = self.engine["MYSQL_PORT"]
            self.USER = self.engine["MYSQL_USER"]
            self.PASSWORD = self.engine["MYSQL_PASSWORD"]
            self.DATABASE = self.engine["MYSQL_DATABASE"]
            self.CHARSET = self.engine["MYSQL_CHARSET"]
            self.mysql_url = 'mysql+pymysql://{}:{}@{}:{}/{}'
            self.config = {
                'host': self.HOST,
                'port': self.PORT,
                'user': self.USER,
                'password': self.PASSWORD,
                'database': self.DATABASE,
                'charset': self.CHARSET,
            }

    def context(self, is_dict_cursor=True):
        """
        创建数据库连接， 数据以字典结构返回
        :param is_dict_cursor: 是否返回字典结构的数据
        :param database: 默认连接的数据库
        :return: 返回一个连接和一个浮标
        """
        try:
            conn = pymysql.connect(**self.config)
            cursor = conn.cursor(cursor=DictCursor) if is_dict_cursor else conn.cursor()

            return conn, cursor
        except Exception as ex:
            print("connect database failed, {},{}".format(400, ex))
            raise Exception({'code': 400, 'msg': ex})

    def select_db(self):
        conn, cursor = self.context()
        sql = "SHOW DATABASES"
        cursor.execute(sql)
        db_name = cursor.fetchall()
        print('所有的数据库名称：', db_name)
        # Close the connection
        conn.commit()
        # connect.rollback()
        cursor.close()
        conn.close()
        print('关闭隧道')
        return db_name
