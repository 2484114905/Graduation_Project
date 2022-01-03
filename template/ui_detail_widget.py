# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DetailWidget(object):
    def setupUi(self, DetailWidget):
        if not DetailWidget.objectName():
            DetailWidget.setObjectName(u"DetailWidget")
        DetailWidget.resize(1216, 892)
        self.image_label = QLabel(DetailWidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(11, 4, 800, 600))
        self.scrollArea = QScrollArea(DetailWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 610, 1211, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1209, 269))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        # self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        # self.gridLayoutWidget.setGeometry(QRect(0, 10, 1091, 411))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(DetailWidget)

        QMetaObject.connectSlotsByName(DetailWidget)
    # setupUi

    def retranslateUi(self, DetailWidget):
        DetailWidget.setWindowTitle(QCoreApplication.translate("DetailWidget", u"\u8be6\u7ec6\u4fe1\u606f", None))
        self.image_label.setText("")
    # retranslateUi

