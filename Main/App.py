# coding:gbk
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import QCoreApplication
from Controller.DController import LoginController,RegController
from UI import LoginUI, RegisterUI


class App(LoginUI.LoginForm):
    def __init__(self):
        super(App, self).__init__()
        self.setupUI()
        self.Action()

    def Action(self):
        self.btnLogin.clicked.connect(self.loginOK)
        # self.regLabel.connectSlot(QCoreApplication.instance().quit)
        self.regLabel.connectSlot(self.goingToRegisterWindow)

    def loginOK(self):
        user = self.usernameEdit.text()
        pwd = self.pwdEdit.text()
        if user == '' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�������û���������')
            msg_box.exec_()
        elif user != '' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '����������')
            msg_box.exec_()
        elif user =='' and pwd != '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�������û���')
            msg_box.exec_()
        if user != '' and pwd != '':
            loginEx = LoginController(user, pwd)
            loginEx.Login()
            status = loginEx.getStatus()
            if not status[0]:
                msg_box = QMessageBox(QMessageBox.Warning, '����', '�û�������ȷ�򲻴���')
                msg_box.exec_()
                self.usernameEdit.clear()
                self.pwdEdit.clear()
            elif not status[1]:
                msg_box = QMessageBox(QMessageBox.Warning, '����', '���벻��ȷ')
                msg_box.exec_()
                self.pwdEdit.clear()
            else:
                msg = '��ӭ%s' % user
                welcomeBox = QMessageBox(QMessageBox.Information, '��ӭ', msg)
                welcomeBox.exec()

    def goingToRegisterWindow(self):
        """���ڴ����ڵ�ǰ����ѭ���������´�����Ҫʵ��������ǰ����"""
        self.close()  # �رյ�¼���ڣ���ע�ᴰ��
        self.RegEx = Reg()
        self.RegEx.show()


class Reg(RegisterUI.Reg):
    def __init__(self):
        super(Reg, self).__init__()
        self.setupUI()
        # �ֻ���Ŀǰд�������ں������ӷ�����֤�빦��
        self.phone = '18800000000'
        self.RegAction()

    def RegAction(self):
        self.RegbtnLogin.clicked.connect(self.Register)
        self.RegregLabel.connectSlot(self.backToLoginWindow)

    def Register(self):
        user = self.RegusernameEdit.text()
        pwd = self.RegpwdEdit.text()
        coPwd = self.RegpwdConfirmEdit.text()
        if user == '' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�������û���������')
            msg_box.exec_()
        elif user == '' and pwd != '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�������û���')
            msg_box.exec_()
        if user !='' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '����������')
            msg_box.exec_()
        # �ж����������һ����
        if user != '' and pwd != '' and coPwd != '':
            if coPwd != pwd:
                msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�������벻һ��')
                self.RegpwdConfirmEdit.clear()
                msg_box.exec_()
            else:
                regEx = RegController(user, pwd, self.phone)
                regEx.Register()
                regStatus = regEx.getStatus()
                if not regStatus:
                    msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�û����Ѵ���')
                    self.RegpwdConfirmEdit.clear()
                    self.RegpwdEdit.clear()
                    msg_box.exec_()
                else:
                    successMsg = 'ע��ɹ�����ӭ' + user
                    msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', successMsg)
                    msg_box.exec_()

    def backToLoginWindow(self):
        self.close()
        self.LoginEx = App()
        self.LoginEx.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    # RegEx = Reg()
    # RegEx.show()
    sys.exit(app.exec_())
