import sys
import time

import cv2
import numpy
from os import path
from PIL import Image
from PySide2.QtCore import QByteArray, QSize, Qt
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QLabel, QPushButton

from util import config_util
import pymysql
from template import main_window


def get_images(connection):
    with connection.cursor() as cursor:
        sql = 'select * from raw_image'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        # print(result)


def delete_images_by_image_id(connection, image_id):
    with connection.cursor() as cursor:
        sql = 'delete from raw_image ' \
              'where image_id = %s '
        cursor.execute(sql, (image_id,))

    connection.commit()


def insert_image(connection, image_id, image_name, image, judge_result, shape, create_time):
    if not connection.open:
        connection.ping()

    with connection.cursor() as cursor:
        sql = 'insert into raw_image(image_id, name, content, judge_result, image_shape, create_time) ' \
              'values(%s, %s, %s, %s, %s, %s)'

        cursor.execute(sql, (image_id, image_name, image, judge_result, shape, create_time))
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    connection = config_util.connection
    image_path = '../images/000002.jpg'

    create_time = path.getctime(image_path)
    create_time = time.localtime(create_time)
    result = time.strftime('%Y-%m-%d %H:%M:%S', create_time)

    with connection.cursor() as cursor:
        sql = 'select * from raw_image'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result[1]['create_time'].isoformat())

    #     sql = 'insert into raw_image(create_time) ' \
    #           'values (%s)'
    #     cursor.execute(sql, (result, ))
    # connection.commit()


