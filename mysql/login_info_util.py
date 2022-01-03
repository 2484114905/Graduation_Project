import pymysql
import socket
import datetime as dt
from util import config_util


def insert_login_info(connection, user_id,):
    device_name = socket.gethostname()
    login_time = dt.datetime.now().strftime('%F %T')

    with connection.cursor() as cursor:
        sql = 'insert into login_info ' \
              'values(%s, %s, %s)'
        cursor.execute(sql, (user_id, device_name, login_time))

    connection.commit()


if __name__ == '__main__':
    connection = config_util.connection
    insert_login_info(connection, 'user_id')
