# coding:gbk
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog
from PyQt5 import QtGui, QtCore
from Controller.DController import LoginController, RegController
from UI import LoginUI, RegisterUI, TranslateUI
from Extra.core import translate


class Login(LoginUI.LoginForm):
    def __init__(self):
        super(Login, self).__init__()
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
        elif user == '' and pwd != '':
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
        if user != '' and pwd == '':
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
        self.LoginEx = Login()
        self.LoginEx.show()


class TranslateWindow(TranslateUI.TranslateMainWindow, QtWidgets.QPlainTextEdit):
    countFlag = -1  # 语种切换位，奇数为目标语言语种，偶数为源语言语种
    currentText = ''  # 翻译flag，保存combobox选择的语言
    isInputFlag = True  # 输入标记位，用于判断文本框内容来自手动输入还是非输入（文件导入，粘贴）
    MAXSIZE = 8000  # 最大字数

    def __init__(self):
        super(TranslateWindow, self).__init__()
        self.setupUi()
        self.translateAction()

    def translateAction(self):
        self.button.clicked.connect(self.Translate)
        self.label.connectSlot(self.reverse)
        self.copybtn.connectSlot(self.copyTranslate)
        self.plainTextEdit.textChanged.connect(self.countText)
        self.uploadFileLabel.connectSlot(self.uploadFile)

    @classmethod
    # 截取文本，限制字数
    def isCut(cls, text):
        size = len(text)
        if size > cls.MAXSIZE:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '超出最大字数限制，将自动截取文本')
            msg_box.exec_()
            text = text[0:cls.MAXSIZE]
            return text
        return text

    # 上传文件
    def uploadFile(self):
        meg_box = QMessageBox(QMessageBox.Information, '提示', '请上传.txt、.pdf文档')
        meg_box.exec_()
        # 指定文件格式
        fname = QFileDialog.getOpenFileName(self, '选择文件', '/Users/admin/Desktop', filter="PDF文件(*.pdf)"
                                                                                         ";;Text文档(*.txt)")
        print(fname)
        if fname[0]:
            f = open(fname[0], 'r', encoding='utf-8')
            with f:
                data = f.read()
                originalText = self.isCut(data)
                self.isInputFlag = False
                self.plainTextEdit.setPlainText(originalText)
                textCursor = self.plainTextEdit.textCursor()  # 获取文本框指针对象
                textCursor.movePosition(QTextCursor.End)  # 将指针移动到末尾
                self.plainTextEdit.setTextCursor(textCursor)

    # 判断当前下拉框的值,新增语言时请在这里添加新的逻辑判断
    def getComboText(self):
        if self.comboBox.currentText() == '英语':
            self._language = 'en'
        elif self.comboBox.currentText() == '日语':
            self._language = 'ja'
        elif self.comboBox.currentText() == '中文':
            self._language = 'zh-CN'
        return self._language

    # 获取文本框内的内容
    def Translate(self):
        originalText_ = self.plainTextEdit.toPlainText()
        originalText = self.isCut(originalText_)
        if originalText != '':
            # """这个方法访问过慢，偶尔会遇到429的异常(备用版本)"""
            # # print(originalText)
            # """调用GoogleTrans接口，此接口来自‘https://github.com/VictorZhang2014/free-google-translate’,感谢.
            # 接口使用：query方法第一个参数表示要翻译的文字，第二个参数表示要翻译的语言
            # 返回参数说明：第一个值源语言，第二个为源语言种类，第三个为目标语言，第四个为目标语言种类"""
            # transRe = GoogleTrans().query(originalText,lang_to=self._language)
            # target = transRe[2]
            # original = transRe[0]
            # self.translateText.setPlainText(target)
            """优化后使用此版本，此方法来自‘https://github.com/mouuff/mtranslate’，感谢
            方法使用：第一个参数为要翻译的文字，第二个为目标语言，第三个为源语言，不输入则会自动识别
            传参的语言缩写见static目录下的languageList文件"""
            language = self.getComboText()
            target = translate(originalText, language)
            self.translateText.setPlainText(target)
            self.currentText = self.comboBox.currentText()
        else:
            self.plainTextEdit.setPlaceholderText('您还没有输入内容')

    # 转换目标语言与源语言 （如果要转换的文字为中文，则无法实现源语言与目标语言在不切换时的转换，要实现需要获取源语言的currentText
    #
    # 在translate方法中，无法获取到自动检测到的源语言，所以此功能暂时还不完善
    def reverse(self):
        self.countFlag += 1
        if self.countFlag % 2 == 0:
            self.comboBox.setCurrentText('中文')
        else:
            self.comboBox.setCurrentText(self.currentText)
        original = self.translateText.toPlainText()
        # original = self.isCut(original_)
        self.plainTextEdit.setPlainText(original)
        reverseLanguage = self.getComboText()
        target = translate(original, reverseLanguage)
        self.isInputFlag = False
        self.translateText.setPlainText(target)

    # 复制译文
    def copyTranslate(self):
        text = self.translateText.toPlainText()
        if text == '':
            msgBox = QMessageBox(QMessageBox.Information, '提示', '似乎没有什么内容')
            msgBox.exec_()
        else:
            clipBoard = QApplication.clipboard()
            clipBoard.setText(text)
            msgBox = QMessageBox(QMessageBox.Information, '提示', '译文已复制')
            msgBox.exec_()

    # 字数统计以及文本框动态逻辑判断
    def countText(self):
        originalText_ = self.plainTextEdit.toPlainText()
        size = len(originalText_)
        countSize = str(size) + '/9999'
        self.countLabel.setText(countSize)
        self.countLabel.setStyleSheet("color:grey")
        if size > self.MAXSIZE:
            # """这里不使用deleteChar的原因是因为：
            # 删除指针所指位置的前一个字符,当达到最大字符时，此时无论指针在哪，再次输入会使得文本长度+1,此时指针会移动到+2的位置
            # """
            # textCursor.deletePreviousChar()
            originalText = self.isCut(originalText_)
            self.plainTextEdit.setPlainText(originalText)
            textCursor = self.plainTextEdit.textCursor()  # 获取文本框指针对象
            textCursor.movePosition(QTextCursor.End)  # 将指针移动到末尾
            self.plainTextEdit.setTextCursor(textCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Login()
    ex = TranslateWindow()
    ex.show()
    # RegEx = Reg()
    # RegEx.show()
    sys.exit(app.exec_())
