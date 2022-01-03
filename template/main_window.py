import csv
import sys
import threading
import uuid
import os
import time
from datetime import datetime
import cv2
import numpy
import pymysql
from PIL import Image
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Slot, QSize, Qt, QObject, QThread, Signal
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QAction, QFileDialog, QMessageBox, QLabel, \
    QPushButton, QVBoxLayout, QSizePolicy, QGridLayout, QWidget, QHBoxLayout

from template.ui_mainwindow import Ui_MainWindow
from template.detail_widget import DetailWidget
from util import config_util
from mysql import user_util
from mysql import result_image_util, raw_image_util
from util import yolo
from util import deeplab
from util import judge


class MainWindow(QMainWindow):
    import_signal = Signal(str, int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.file_menu = self.ui.menubar.addMenu("文件")

        import_action = self.ui.file_menu.addAction("导入")
        import_action.setShortcut("Ctrl+I")
        import_action.triggered.connect(self.import_data)

        exit_action = self.ui.file_menu.addAction("退出")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.ui.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # self.message_box = QMessageBox(QMessageBox.Information, '导入数据', '')
        self.detail = DetailWidget()

        self.ui.submit_button.clicked.connect(self.update_user)

        self.message = {
            'error': '原密码错误',
            'correct': '修改成功'
        }

        self.data = raw_image_util.get_images(config_util.connection)
        self.load_data()
        self.statusBar().showMessage('hello, wy')

        self.import_signal.connect(self.statusBar().showMessage)
        self.import_signal.connect(self.refresh)

    def load_data(self):
        # data = raw_image_util.get_images(config_util.connection)
        if self.data is not None:
            for i in range(len(self.data)):
                item = QWidget(parent=self.ui.scrollAreaWidgetContents)
                item_size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                item.setSizePolicy(item_size_policy)

                image_buffer = numpy.frombuffer(self.data[i]['content'], dtype=numpy.uint8)
                shape = eval(self.data[i]['image_shape'])
                image_buffer = image_buffer.reshape(shape)
                small_image = cv2.resize(image_buffer, dsize=(400, 300), interpolation=cv2.INTER_AREA)
                image = QImage(small_image.data, small_image.shape[1], small_image.shape[0], QImage.Format_RGB888)
                image_label = QLabel()
                image_label.setPixmap(QPixmap.fromImage(image))
                # image_label.setSizePolicy(item_size_policy)

                size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, QSizePolicy.PushButton)
                view_button = QPushButton(text='查看')
                view_button.setSizePolicy(size_policy)
                view_button.clicked.connect(self.view_detail)
                delete_button = QPushButton(text='删除')
                delete_button.setSizePolicy(size_policy)
                delete_button.clicked.connect(self.delete_image)
                vlayout = QVBoxLayout()
                vlayout.addWidget(view_button)
                vlayout.addWidget(delete_button)
                # vlayout.setStretch(0, 0.1)

                message_text = self.data[i]['name'] + '\n' + '判别结果：'
                if bool(self.data[i]['judge_result']):
                    message_text += '完好'
                else:
                    message_text += '破损'
                message_text += '\n'
                if self.data[i]['create_time'] is not None:
                    message_text += self.data[i]['create_time'].isoformat(sep=' ')
                message_label = QLabel(text=message_text)
                vlayout.addWidget(message_label)

                hlayout = QHBoxLayout()
                hlayout.addWidget(image_label)
                hlayout.addLayout(vlayout)
                # layout_sizepolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                item.setLayout(hlayout)
                self.ui.verticalLayout.addWidget(item)

    def clear_layout(self):
        for i in reversed(range(self.ui.verticalLayout.count())):

            removed_item = self.ui.verticalLayout.takeAt(i)

            removed_item.widget().setParent(None)

    @Slot()
    def update_user(self):
        if self.ui.old_lineEdit.text().strip() != config_util.login_user['password'].decode():
            self.ui.message_label.setText(self.message['error'])
            return
        else:
            user_util.update_user(config_util.connection,
                                 self.ui.username_lineEdit.text().strip(),
                                 self.ui.new_lineEdit.text().strip(),
                                 config_util.login_user['id'])
            self.ui.message_label.setText(self.message['correct'])

    @Slot()
    def exit_app(self):
        QApplication.quit()

    @Slot()
    def refresh(self):
        self.clear_layout()
        self.data = raw_image_util.get_images(config_util.connection)
        self.load_data()

    @Slot()
    def import_data(self):
        (file_names, filters) = QFileDialog.getOpenFileNames(self,
                                                             caption='导入图片',
                                                             filter='Images (*.png *.jpg)')

        self.statusBar().showMessage('正在导入，可能需要花费一些时间 ')
        new_thread = threading.Thread(target=self.import_all_images, args=(file_names,))
        new_thread.start()

    @Slot()
    def delete_image(self):
        sender = self.sender()
        print(sender)
        parent_widget = sender.parentWidget()

        index = self.ui.verticalLayout.indexOf(parent_widget)
        print(index)
        image_id = self.data[index]['image_id']
        parent_widget.setParent(None)
        self.ui.verticalLayout.removeWidget(parent_widget)
        self.data.pop(index)

        result_image_util.delete_images_by_parent_id(config_util.connection, image_id)
        raw_image_util.delete_images_by_image_id(config_util.connection, image_id)

    @Slot()
    def view_detail(self):
        sender = self.sender()
        print(sender)
        parent_widget = sender.parentWidget()
        index = self.ui.verticalLayout.indexOf(parent_widget)
        print(index)
        # image_id = self.data[index]['image_id']
        self.detail.load_data(self.data[index])
        self.detail.show()

    def import_all_images(self, image_paths):
        # pretrained_weights = '../model/frozen_inference_graph.pb'
        deeplab_model = config_util.deeplab_model  # 加载模型

        with open(config_util.properties.get('statistics_file'), mode='a', newline='') as statistics_file:
            csv_writer = csv.writer(statistics_file, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for path in image_paths:
                image_id = uuid.uuid1()
                import_image(path, image_id, deeplab_model, csv_writer)

        self.import_signal.emit('导入完成', 60000)


def import_image(parent_path, parent_id, deeplab_model, csv_writer):
    detect_result, crop_list = yolo.detect_object(parent_path)
    parent_name = os.path.basename(parent_path)
    create_time = get_create_time(parent_path)
    judge_result = 1

    for i in range(len(crop_list)):
        image_id = uuid.uuid1()
        image = Image.fromarray(crop_list[i])
        resized_image, seg_map = deeplab_model.run(image)  # 获取结果
        is_intact, statistics = judge.get_result(seg_map)
        if not is_intact:
            judge_result = 0

        parent_name_part = parent_name.split('.')
        image_name = parent_name_part[0] + '-' + str(i) + '.' + parent_name_part[1]
        result_image_util.insert_image(config_util.connection,
                                       image_id, parent_id, image_name,
                                       crop_list[i].tobytes(),
                                       seg_map.tobytes(),
                                       int(is_intact),
                                       str(crop_list[i].shape),
                                       str(seg_map.shape))
        csv_writer.writerow([image_name, statistics[0], statistics[1]])

    raw_image_util.insert_image(config_util.connection,
                                parent_id, parent_name,
                                detect_result.tobytes(), judge_result,
                                str(detect_result.shape), create_time)


def get_create_time(file_path):
    create_time = os.path.getctime(file_path)
    create_time = time.localtime(create_time)
    result = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
    return result


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
