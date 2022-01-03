from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog, QLineEdit
from util import config_util
from mysql import user_util, login_info_util
from template.ui_login_dialog import Ui_LoginDialog
from template.main_window import MainWindow


class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.reset_button.clicked.connect(self.reset)
        self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.login_message = {
            'error1': '用户名不存在',
            'error2': '密码错误',
        }

        self.main_window = MainWindow()

    @Slot()
    def login(self):
        username = self.ui.username_lineEdit.text().strip()
        password = self.ui.password_lineEdit.text().strip()
        connection = config_util.connection
        result = user_util.get_user(connection, username)
        if result is None:
            self.ui.error_label.setText(self.login_message['error1'])
            print(self.login_message['error1'])
        elif password != result['password'].decode():
            self.ui.error_label.setText(self.login_message['error2'])
            print(self.login_message['error2'])
            print(type(result['password'].decode()))
        else:
            login_info_util.insert_login_info(config_util.connection, result['id'])
            for key in result:
                config_util.login_user[key] = result[key]

            self.close()

            self.main_window.ui.username_lineEdit.setText(config_util.login_user['username'])
            self.main_window.show()
            print('登录成功')

    @Slot()
    def reset(self):
        self.ui.password_lineEdit.setText("")
        self.ui.username_lineEdit.setText("")

