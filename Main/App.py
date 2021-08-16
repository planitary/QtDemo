# coding:gbk
import sys
from PyQt5.QtWidgets import  QMessageBox, QApplication
from PyQt5.QtCore import QCoreApplication
from Controller.DController import LoginController,RegController
from UI import LoginUI, RegisterUI,TranslateUI
from Extra.GoogleTrans import GoogleTrans

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
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名或密码')
            msg_box.exec_()
        elif user != '' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入密码')
            msg_box.exec_()
        elif user =='' and pwd != '':
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名')
            msg_box.exec_()
        if user != '' and pwd != '':
            loginEx = LoginController(user, pwd)
            loginEx.Login()
            status = loginEx.getStatus()
            if not status[0]:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '用户名不正确或不存在')
                msg_box.exec_()
                self.usernameEdit.clear()
                self.pwdEdit.clear()
            elif not status[1]:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码不正确')
                msg_box.exec_()
                self.pwdEdit.clear()
            else:
                msg = '欢迎%s' % user
                welcomeBox = QMessageBox(QMessageBox.Information, '欢迎', msg)
                welcomeBox.exec()

    def goingToRegisterWindow(self):
        """由于窗口在当前类中循环，所以新窗口需要实例化到当前类中"""
        self.close()  # 关闭登录窗口，打开注册窗口
        self.RegEx = Reg()
        self.RegEx.show()


class Reg(RegisterUI.Reg):
    def __init__(self):
        super(Reg, self).__init__()
        self.setupUI()
        # 手机号目前写死，用于后期增加发送验证码功能
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
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名或密码')
            msg_box.exec_()
        elif user == '' and pwd != '':
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入用户名')
            msg_box.exec_()
        if user !='' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入密码')
            msg_box.exec_()
        # 判断两次密码的一致性
        if user != '' and pwd != '' and coPwd != '':
            if coPwd != pwd:
                msg_box = QMessageBox(QMessageBox.Warning, '提示', '两次密码不一致')
                self.RegpwdConfirmEdit.clear()
                msg_box.exec_()
            else:
                regEx = RegController(user, pwd, self.phone)
                regEx.Register()
                regStatus = regEx.getStatus()
                if not regStatus:
                    msg_box = QMessageBox(QMessageBox.Warning, '提示', '用户名已存在')
                    self.RegpwdConfirmEdit.clear()
                    self.RegpwdEdit.clear()
                    msg_box.exec_()
                else:
                    successMsg = '注册成功，欢迎' + user
                    msg_box = QMessageBox(QMessageBox.Warning, '提示', successMsg)
                    msg_box.exec_()

    def backToLoginWindow(self):
        self.close()
        self.LoginEx = App()
        self.LoginEx.show()

class TranslateWindow(TranslateUI.TranslateMainWindow):
    _language = ''
    def __init__(self):
        super(TranslateWindow, self).__init__()
        self.setupUi()
        self.translateAction()

    def translateAction(self):
        self.button.clicked.connect(self.Translate)

    def Translate(self):
        # 获取文本框内的内容
        originalText = self.plainTextEdit.toPlainText()
        # 判断当前下拉框得值
        if self.comboBox.currentText() == '英语':
            self._language = 'en'
        elif self.comboBox.currentText() == '日语':
            self._language = 'ja'
        elif self.comboBox.currentText() == '中文':
            self._language = 'zh-CN'

        if originalText != '':
            """这个方法访问过慢，偶尔会遇到429的异常"""
            # print(originalText)
            """调用GoogleTrans接口，此接口来自‘https://github.com/VictorZhang2014/free-google-translate’,感谢.
            接口使用：query方法第一个参数表示要翻译的文字，第二个参数表示要翻译的语言
            返回参数说明：第一个值源语言，第二个为源语言种类，第三个为目标语言，第四个为目标语言种类"""
            transRe = GoogleTrans().query(originalText,lang_to=self._language)
            target = transRe[2]
            original = transRe[0]
            self.translateText.setPlainText(target)
            # translator = Translator(service_url=['translate.google.cn',])
            # target = translator.translate(originalText, dest=self._language)
            # print(target)
        else:
            self.plainTextEdit.setPlaceholderText('您还没有输入内容')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = App()
    ex = TranslateWindow()
    ex.show()
    # RegEx = Reg()
    # RegEx.show()
    sys.exit(app.exec_())
