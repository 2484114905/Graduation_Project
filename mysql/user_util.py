import pymysql


def get_user(connection, username):
    with connection.cursor() as cursor:
        sql = "select username, AES_DECRYPT(password, 'key') as password, user_id as id from user where username " \
              "= %s "
        cursor.execute(sql, username)
        result = cursor.fetchone()
        return result


def update_user(connection, new_username, new_password, id):
    with connection.cursor() as cursor:
        sql = "update user " \
              "set username = %s," \
              "password = %s " \
              "where user_id = %s"
        cursor.execute(sql, (new_username, new_password, id))
    connection.commit()
