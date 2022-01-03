from PySide2 import QtCore, QtWidgets
from functools import partial


class Test:
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.mainWidget = QtWidgets.QWidget()
        self.lights = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.window.setCentralWidget(self.mainWidget)

    def light_label_event(self, name, checked):
        print(name,checked)

    def populate_lights(self):
        self.light_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        for light in self.lights:
            light_label = QtWidgets.QPushButton(light)
            light_label.setCheckable(True)
            light_label.toggled.connect(partial(self.light_label_event,light))
            self.light_layout.addWidget(light_label)
        self.light_layout.addStretch()

    def light_palette_ui(self):
        self.vertical_layout_main = QtWidgets.QVBoxLayout(self.mainWidget)
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.vertical_layout_main.addWidget(self.scroll)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll_widget = QtWidgets.QWidget()
        self.scroll.setWidget(self.scroll_widget)

        self.populate_lights()
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.window.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    t = Test()
    t.light_palette_ui()
    sys.exit(app.exec_())