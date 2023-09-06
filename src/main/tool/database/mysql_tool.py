import os
import re

import pandas as pd
import pymysql
from pymysql.cursors import DictCursor
from sqlalchemy import create_engine

from src.config import MYSQL_WRITE_DATA_PD, MYSQL_WRITE_DATA_CSV, file_path_name


# 数据库操作
class OperationMysqlData(object):
    """数据库操作"""

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

    def create_db(self, data_name):
        conn, cursor = self.context()
        sql = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8mb4".format(data_name)
        cursor.execute(sql)
        print('创建{}数据库成功！'.format(data_name))
        # Close the connection
        conn.commit()
        # connect.rollback()
        cursor.close()
        conn.close()
        print('关闭隧道')

    def drop_db(self, data_name):
        # drop database <数据库名>;
        conn, cursor = self.context()
        sql = "drop database {}".format(data_name)
        cursor.execute(sql)
        print('删除{}数据库成功！'.format(data_name))
        # Close the connection
        conn.commit()
        # connect.rollback()
        cursor.close()
        conn.close()
        print('关闭隧道')

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

    def select_db_table_judge(self, tool_name, engine, db_name, tb_name) -> bool:
        """判断数据库表是否存在"""
        print(f"判断表 {db_name}.{tb_name} 是否存在")
        sql = f"select * from information_schema.tables where TABLE_SCHEMA='{db_name}' AND table_name ='{tb_name}'"
        if tool_name == 'pymysql':
            # input(engine.execute(sql).fetchall())
            engine.execute(sql)
            if engine.fetchall():
                return True
        elif tool_name == 'sqlalchemy':
            with engine.connect() as con:
                return con.dialect.has_table(con, table_name=tb_name, schema=db_name)
        return False

    def write_data(self, filepath, chunk_size, table_name, if_exits=None):
        """
        文件写入数据库
        filepath:文件路径
        chunk_size:每次传输大小
        table_name:指定数据库表名

        index：是否将df的index单独写到一列中
        chunk size：设置一次入库的大小
        if_exits三个模式：fail，若表存在则不输出；replace：若表存在覆盖原来表里的数据；append：若表存在将数据写到原表的后面。默认为fail
        """

        for fi in file_path_name["filter_rubbish_file"]:
            if re.match(fi, filepath):
                raise "请输入正确的文件"

        if filepath.lower().split('.')[-1] in MYSQL_WRITE_DATA_PD:
            print('建立MySql数据库连接')
            engine = create_engine(
                self.mysql_url.format(self.USER, self.PASSWORD, self.HOST, self.PORT, self.DATABASE),
                # encodings=self.CHARSET
            )
            print("开始执行数据写入!")
            pd.read_excel(filepath, sheet_name=table_name).to_sql(
                str(table_name), engine, if_exists=if_exits, index=False, chunksize=int(
                    chunk_size)) if if_exits else pd.read_excel(
                filepath, sheet_name=table_name).to_sql(
                str(table_name), engine, if_exists='append', index=False, chunksize=int(chunk_size))
            print("数据写入成功!\n")
        elif filepath.lower().split('.')[-1] in MYSQL_WRITE_DATA_CSV:
            print('建立MySql数据库连接')
            engine = create_engine(self.mysql_url.format(self.USER, self.PASSWORD, self.HOST, self.PORT, self.DATABASE))
            print("开始执行数据写入!")
            pd.read_csv(filepath, encoding='utf-8').to_sql(
                str(table_name), engine, if_exists=if_exits, index=False, chunksize=int(chunk_size)) if if_exits \
                else pd.read_csv(filepath, encoding='utf-8').to_sql(
                str(table_name), engine, if_exists='append', index=False,
                chunksize=int(chunk_size))
            print("数据写入成功!\n")
        else:
            raise "此文件类型不支持"

        return True

    def dow_data(self, db_name, tb_name, file_name):
        print('建立MySql数据库连接')
        engine = create_engine(self.mysql_url.format(self.USER, self.PASSWORD, self.HOST, self.PORT, self.DATABASE))
        print('隧道建立成功')
        print(f'判断文件是否有效')
        for fi in file_path_name["filter_rubbish_file"]:
            if re.match(fi, file_name):
                raise "请输入正确的文件"
        print(f'判断文件类型是否符合 {" ".join([file for file in MYSQL_WRITE_DATA_PD + MYSQL_WRITE_DATA_CSV])} 格式')
        print('判断文件是否存在')
        # pd_file = False
        if os.path.exists(file_name):
            pd_ = input('文件已存在是否覆盖文件，同意请输入 y 或 Y :')
            pd_file = True if pd_ in ['y', 'Y'] and pd_ else False
        else:
            pd_file = True
        if pd_file:
            if file_name.lower().split('.')[-1] in MYSQL_WRITE_DATA_PD + MYSQL_WRITE_DATA_CSV:
                print('文件类型正确，执行数据读取')
                if self.select_db_table_judge('sqlalchemy', engine, db_name, tb_name):
                    sql_select_table = f'select * from {db_name}.{tb_name}'
                    print(f"开始读取 {db_name}.{tb_name} 数据...")
                    db = pd.read_sql(sql=sql_select_table, con=engine)
                    print(f'数据读取成功，开始执行写入到文件->{file_name}')
                    if file_name.lower().split('.')[-1] in MYSQL_WRITE_DATA_PD:
                        db.to_excel(file_name, index=False)
                    elif file_name.lower().split('.')[-1] in MYSQL_WRITE_DATA_CSV:
                        db.to_csv(file_name, index=False)
                    print(f'写入 {file_name} 成功！')
            else:
                raise "此文件类型不支持"

    def rename_db(self, old_name, new_name):
        """
        数据库迁移
        真实想法，传入字典形式并判断传入数据
            table = {"old_db":{"old_table":"new_table"...}}
            db = {"old_db": "new_db"...}
        :param old_name: 原来的数据库名
        :param new_name: 新数据库名
        :return: 成功返回True, 失败返回False
        """
        # 循环获取  数据库  表  字段  字段属性
        if old_name and new_name and isinstance(old_name, str) and isinstance(new_name, str):
            sql_determine_exists_db = "show databases like %s"
            sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=%s"
            conn, cursor = self.context()
            determine_exists_db = [cursor.execute(sql_determine_exists_db, (old_name,)),
                                   cursor.execute(sql_determine_exists_db, (new_name,))]

            try:
                conn.begin()
                if determine_exists_db[0] != determine_exists_db[1] and determine_exists_db[0]:
                    sql_new_db = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8mb4".format(new_name)
                    cursor.execute(sql_new_db)
                    cursor.execute(sql, (old_name,))
                    # results = cursor.fetchall()
                    # for r in results:
                    #     tb = r['TABLE_NAME']
                    #     rename_sql = """RENAME TABLE {}.{} to {}.{}""".format(old_name, tb, new_name, tb)
                    #     cursor.execute(rename_sql)
                    # 需要数据转移
                    # 1.导出（文件）再导入  2.直接执行表直接插入数据
                    # INSERT INTO test.工程组业务对象描述 (宽表, 业务对象, 来源, 描述)
                    # VALUES ('项目结算管理宽表', '项目成本信息', 'ERP', 'ERP 计入项目的成本及凭证信息');

                elif determine_exists_db[0] and determine_exists_db[1]:
                    # 如果数据库存在判断表存不存在，如果存在 备份数据 具体形式之后再论，如果不存在则直接导出旧表数据并导入到新表
                    # 是直接覆盖插入还是后增插入
                    pass

                elif not determine_exists_db[0]:
                    print('旧数据库不存在')
                    pass

                # cursor.execute('drop database {}'.format(old_name))  # 把旧数据库删掉
            except Exception as ex:
                conn.rollback()
                print("rename_db Exception: {},{}".format(sql, ex))
                return False
            else:
                conn.commit()  # 如果没有发生异常，则提交事务
            finally:
                conn.close()
            return True
