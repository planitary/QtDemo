# coding:gbk
import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
from Controller.LoginController import LoginController
from UI import LoginUI


class LoginApp(LoginUI.LoginForm):
    def __init__(self,Widget):
        super(LoginApp, self).__init__()
        self.setupUI(Widget)
        self.initUI()

    def initUI(self):
        self.btnLogin.clicked.connect(self.loginOK)

    def loginOK(self):
        user = self.usernameEdit.text()
        pwd = self.pwdEdit.text()
        loginEx = LoginController(user,pwd)
        loginEx.Login()
        status = loginEx.getStatus()
        if not status[0]:
            msg_box = QMessageBox(QMessageBox.Warning,'警告','用户名不正确')
            msg_box.exec_()
            self.usernameEdit.clear()
            self.pwdEdit.clear()
        elif not status[1]:
            msg_box = QMessageBox(QMessageBox.Warning,'警告','密码不正确')
            msg_box.exec_()
            self.pwdEdit.clear()
        else:
            print('登录成功')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex_ = QWidget()
    ex = LoginApp(ex_)
    ex_.show()
    sys.exit(app.exec_())
