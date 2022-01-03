import cv2
import numpy
from PySide2 import QtCore
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QWidget, QLabel
from template.ui_detail_widget import Ui_DetailWidget

from mysql import result_image_util
from util import config_util


class DetailWidget(QWidget):
    def __init__(self):
        super(DetailWidget, self).__init__()
        self.ui = Ui_DetailWidget()
        self.ui.setupUi(self)
        self.ui.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def load_data(self, image_data):
        image_id = image_data['image_id']
        image_buffer = numpy.frombuffer(image_data['content'], dtype=numpy.uint8)
        shape = eval(image_data['image_shape'])
        image_buffer = image_buffer.reshape(shape)
        small_image_buffer = cv2.resize(image_buffer, dsize=(800, 600), interpolation=cv2.INTER_AREA)
        shape = small_image_buffer.shape
        image = QImage(small_image_buffer.data,
                       shape[1], shape[0],
                       QImage.Format_RGB888)
        self.ui.image_label.setPixmap(QPixmap.fromImage(image))

        result = result_image_util.get_images_by_parent_id(config_util.connection, image_id)
        if result is not None:
            for i in range(len(result)):
                raw_shape = eval(result[i]['raw_image_shape'])
                object_image_label = self.get_image_label(result[i]['raw_content'], raw_shape)
                segment_shape = eval(result[i]['segment_image_shape'])
                segment_image_label = self.get_image_label(result[i]['segment_content'], segment_shape)
                message_text = result[i]['name'] + '\n' + '判别结果：'
                if bool(result[i]['judge_result']):
                    message_text += '完好'
                else:
                    message_text += '破损'
                message_label = QLabel(text=message_text)
                
                self.ui.gridLayout.addWidget(object_image_label, i, 0)
                self.ui.gridLayout.addWidget(segment_image_label, i, 1)
                self.ui.gridLayout.addWidget(message_label, i, 2)

    @staticmethod
    def get_image_label(image_data, image_shape):
        image_buffer = numpy.frombuffer(image_data, dtype=numpy.uint8)
        image_buffer = image_buffer.reshape(image_shape)
        image_buffer = cv2.resize(image_buffer, dsize=(200, 150), interpolation=cv2.INTER_AREA)
        if len(image_shape) < 3:
            image = QImage(image_buffer.data, image_buffer.shape[1], image_buffer.shape[0], QImage.Format_Indexed8)
        else:
            image = QImage(image_buffer.data, image_buffer.shape[1], image_buffer.shape[0], QImage.Format_RGB888)
        image_label = QLabel()
        image_label.setPixmap(QPixmap.fromImage(image))
        return image_label

