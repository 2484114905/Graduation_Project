# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 854)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1131, 801))
        self.tabWidget.setIconSize(QSize(20, 20))
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.scrollArea = QScrollArea(self.data_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1131, 771))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1129, 769))
        # self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        # self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        # self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1121, 761))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.data_tab, "")
        self.user_tab = QWidget()
        self.user_tab.setObjectName(u"user_tab")
        self.label = QLabel(self.user_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 60, 131, 41))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.username_lineEdit = QLineEdit(self.user_tab)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(230, 60, 321, 41))
        self.label_2 = QLabel(self.user_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 190, 131, 41))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.user_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 320, 131, 41))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.old_lineEdit = QLineEdit(self.user_tab)
        self.old_lineEdit.setObjectName(u"old_lineEdit")
        self.old_lineEdit.setGeometry(QRect(230, 190, 321, 41))
        self.new_lineEdit = QLineEdit(self.user_tab)
        self.new_lineEdit.setObjectName(u"new_lineEdit")
        self.new_lineEdit.setGeometry(QRect(230, 320, 321, 41))
        self.message_label = QLabel(self.user_tab)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setGeometry(QRect(230, 380, 321, 31))
        self.message_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.submit_button = QPushButton(self.user_tab)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(460, 470, 93, 28))
        self.tabWidget.addTab(self.user_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1128, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7535\u529b\u5de1\u68c0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65e7\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5bc6\u7801", None))
        self.message_label.setText("")
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_tab), QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
    # retranslateUi

