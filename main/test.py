import csv
import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMessageBox, QWidget, QPushButton, QApplication

from util import config_util


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.button = QPushButton(parent=self, text='click')
        self.button.clicked.connect(self.say_hello)

    @Slot()
    def say_hello(self):
        sender = self.sender()
        print(sender)
        print('hello')


if __name__ == '__main__':
    # QMessageBox.information(parent=None, title='导入数据', text='请稍等', button0=QMessageBox.Ok)
    # app = QApplication(sys.argv)
    # Create and show the form
    # my_widget = MyWidget()
    # my_widget.show()
    # Run the main Qt loop
    # sys.exit(app.exec_())
    csv_path = '../source/error_statistics.csv'
    with open(csv_path, mode='a', newline='') as statistics_file:
        csv_writer = csv.writer(statistics_file, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([1, 2, 3])
