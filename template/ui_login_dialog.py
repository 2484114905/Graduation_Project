# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(573, 383)
        self.login_button = QPushButton(LoginDialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(260, 290, 93, 28))
        self.reset_button = QPushButton(LoginDialog)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(390, 290, 93, 28))
        self.label = QLabel(LoginDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 111, 41))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.username_lineEdit = QLineEdit(LoginDialog)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(230, 50, 251, 41))
        self.password_lineEdit = QLineEdit(LoginDialog)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(230, 120, 251, 41))
        self.label_2 = QLabel(LoginDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 120, 111, 41))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.error_label = QLabel(LoginDialog)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(230, 220, 251, 31))
        self.error_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"\u767b\u5f55", None))
        self.login_button.setText(QCoreApplication.translate("LoginDialog", u"\u767b\u5f55", None))
        self.reset_button.setText(QCoreApplication.translate("LoginDialog", u"\u91cd\u7f6e", None))
        self.label.setText(QCoreApplication.translate("LoginDialog", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("LoginDialog", u"\u5bc6\u7801", None))
        self.error_label.setText("")
    # retranslateUi

