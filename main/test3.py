import sys

from PySide2.QtCore import Signal, QThread
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QApplication, QLabel

from template.ui_layout import Ui_Form


class MyThread(QThread):
    def __init__(self, parent=None, argument=None):
        super().__init__(parent)
        self.file_name = argument

    def run(self):
        print(self.file_name)
        print(self.parent())


class MyWidget(QWidget):
    signal = Signal(str)

    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add_item)
        self.ui.pushButton_2.clicked.connect(self.greet)
        self.ui.pushButton_3.clicked.connect(self.remove_item)
        self.ui.pushButton_4.clicked.connect(self.remove_all)
        self.signal.connect(self.greet_slot)



    @Slot()
    def remove_item(self):
        sender = self.sender()
        sender.setParent(None)
        self.ui.verticalLayout.removeWidget(sender)

    @Slot()
    def remove_all(self):
        for i in reversed(range(self.ui.verticalLayout.count())):

            removed_item = self.ui.verticalLayout.takeAt(i)

            removed_item.widget().setParent(None)

    @Slot()
    def add_item(self):
        new_label = QLabel(text='new item')
        self.ui.verticalLayout.addWidget(new_label)

    @Slot()
    def greet(self, text):
        self.signal.emit('hello')

    @Slot()
    def greet_slot(self, text):
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
