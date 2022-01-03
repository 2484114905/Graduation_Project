import pymysql
from PySide2.QtWidgets import QApplication


def get_images(connection):
    with connection.cursor() as cursor:
        sql = 'select * from result_image'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


def get_images_by_parent_id(connecton, parent_id):
    with connecton.cursor() as cursor:
        sql = 'select * from result_image ' \
              'where parent_id = %s'
        cursor.execute(sql, (parent_id,))
        result = cursor.fetchall()
        return result


def delete_images_by_parent_id(connection, parent_id):
    with connection.cursor() as cursor:
        sql = 'delete from result_image ' \
              'where parent_id = %s '
        cursor.execute(sql, (parent_id,))

    connection.commit()


def insert_image(connection, image_id, parent_id, image_name, raw_image,
                 image, judge_result, raw_shape, segment_shape):

    # if not connection.open:
    #     connection.ping()
    #
    # insert_dict = {
    #     'image_id': image_id,
    #     'parent_id': parent_id,
    #     'image_name': image_name,
    #     'raw_image': raw_image,
    #     'image': image,
    #     'judge_result': judge_result
    # }
    with connection.cursor() as cursor:

        sql = 'insert into result_image ' \
              'values(%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (image_id, parent_id, image_name, raw_image,
                             image, judge_result, raw_shape, segment_shape))

        # sql = 'insert into raw_image ' \
        #       'values(%image_id, %parent_id, %image_name, %raw_image, %image, %judge_result)'
        #
        # cursor.execute(sql, insert_dict)
    connection.commit()
    cursor.close()


