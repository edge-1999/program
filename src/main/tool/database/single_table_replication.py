import mysql.connector
import threading
import multiprocessing
from mysql.connector.conversion import MySQLConverter

# MySQL数据库连接信息
# db_config = {
#     host: "localhost",
#     user: "root",
#     password: "li19990929..",
#     database: "author",
# }
host = "localhost"
user = "root"
password = "li19990929.."
database = "author"
# 原始数据表名和目标数据表名
src_table_name = "AIC_G0GSDM"
dst_table_name = "AIC_G0GSDM_1"

# 复制数据的批次大小
batch_size = 1000


# 获取MySQL数据库连接
def get_mysql_connection():
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


# 创建目标数据表
def create_dst_table():
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {dst_table_name} LIKE {src_table_name}")
    cursor.close()
    conn.close()


# 获取原始数据表的总记录数
def get_src_table_count():
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {src_table_name}")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count


# 分批复制数据
def copy_data(offset, type_pd):
    conn = get_mysql_connection()
    src_cursor = conn.cursor()
    dst_cursor = conn.cursor()
    src_cursor.execute(f"SELECT * FROM {src_table_name} LIMIT {batch_size} OFFSET {offset}")
    rows = src_cursor.fetchall()
    input(type_pd)
    try:
        if type_pd == 'threads':
            converter = MySQLConverter(conn.charset, True)
        elif type_pd == 'processes':
            conn.start_transaction()
        while rows:
            list_str = ','.join(
                ['({})'.format(
                    ','.join("'{}'".format('' if i is None else i) for i in map(converter.escape, rows.pop())))
                 for _ in range(100)]) if len(rows) >= 100 else ','.join(
                ['({})'.format(
                    ','.join("'{}'".format('' if i is None else i) for i in map(converter.escape, rows.pop())))
                 for _ in range(len(rows))])
            query = f"INSERT INTO {dst_table_name} VALUES {list_str}"
            dst_cursor.execute(query)
        conn.commit()
    except:
        conn.rollback()
    finally:
        dst_cursor.close()
        src_cursor.close()
        conn.close()


# 多线程复制数据
def copy_data_multithread():
    count = get_src_table_count()
    threads = []
    for offset in range(0, count, batch_size):
        thread = threading.Thread(target=copy_data, args=(offset, 'threads'))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


# 多进程复制数据
def copy_data_multiprocess():
    count = get_src_table_count()
    processes = []
    for offset in range(0, count, batch_size):
        process = multiprocessing.Process(target=copy_data, args=(offset, 'processes'))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


# 主函数
def main():
    create_dst_table()
    copy_data_multithread()
    # 或者使用 copy_data_multiprocess() 复制数据
    # copy_data_multiprocess()
    print(f"数据表 author.{src_table_name} 成功复制到数据表 {dst_table_name}")


if __name__ == "__main__":
    main()
