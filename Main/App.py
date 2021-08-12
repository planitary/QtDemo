# coding:gbk
import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
from PyQt5.QtCore import QCoreApplication
from Controller.DController import LoginController
from UI import LoginUI,Register


class Reg(Register.Reg):
    def __init__(self):
        super(Reg, self).__init__()
        self.setupUI()

    def Register(self):
        print(123)

class App(LoginUI.LoginForm):
    def __init__(self,Widget):
        super(App, self).__init__()
        self.setupUI(Widget)
        self.Action()

    def Action(self):
        self.btnLogin.clicked.connect(self.loginOK)
        # self.regLabel.connectSlot(QCoreApplication.instance().quit)
        self.regLabel.connectSlot(self.Register)


    def loginOK(self):
        user =self.usernameEdit.text()
        pwd = self.pwdEdit.text()
        if user == '' or pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning,'提示','请输入用户名或密码')
            msg_box.exec_()
        if user or pwd != '':
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
                msg = '欢迎%s' % user
                welcomeBox = QMessageBox(QMessageBox.Information,'欢迎',msg)
                welcomeBox.exec()

    def Register(self):
        QCoreApplication.instance().quit()              # 关闭当前窗口
        RegEx = Reg()
        RegEx.setupUI()
        RegEx.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex_ = QWidget()
    # ex = App(ex_)
    # ex_.show()
    RegEx = Reg()
    sys.exit(app.exec_())