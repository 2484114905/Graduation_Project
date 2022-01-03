import sys
from template.login_dialog import LoginDialog
from PySide2.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication([])
    dialog = LoginDialog()
    dialog.show()

    sys.exit(app.exec_())



