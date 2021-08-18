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
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '�������û���������')
            msg_box.exec_()
        elif user != '' and pwd == '':
            msg_box = QMessageBox(QMessageBox.Warning, '��ʾ', '����������')
            msg_box.exec_()
        elif user == '' and pwd != '':
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
        if user != '' and pwd == '':
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
        self.LoginEx = Login()
        self.LoginEx.show()


class TranslateWindow(TranslateUI.TranslateMainWindow, QtWidgets.QPlainTextEdit):
    countFlag = -1  # �����л�λ������ΪĿ���������֣�ż��ΪԴ��������
    currentText = ''  # ����flag������comboboxѡ�������
    isInputFlag = True  # ������λ�������ж��ı������������ֶ����뻹�Ƿ����루�ļ����룬ճ����
    MAXSIZE = 8000  # �������

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
    # ��ȡ�ı�����������
    def isCut(cls, text):
        size = len(text)
        if size > cls.MAXSIZE:
            msg_box = QMessageBox(QMessageBox.Information, '��ʾ', '��������������ƣ����Զ���ȡ�ı�')
            msg_box.exec_()
            text = text[0:cls.MAXSIZE]
            return text
        return text

    # �ϴ��ļ�
    def uploadFile(self):
        meg_box = QMessageBox(QMessageBox.Information, '��ʾ', '���ϴ�.txt��.pdf�ĵ�')
        meg_box.exec_()
        # ָ���ļ���ʽ
        fname = QFileDialog.getOpenFileName(self, 'ѡ���ļ�', '/Users/admin/Desktop', filter="PDF�ļ�(*.pdf)"
                                                                                         ";;Text�ĵ�(*.txt)")
        print(fname)
        if fname[0]:
            f = open(fname[0], 'r', encoding='utf-8')
            with f:
                data = f.read()
                originalText = self.isCut(data)
                self.isInputFlag = False
                self.plainTextEdit.setPlainText(originalText)
                textCursor = self.plainTextEdit.textCursor()  # ��ȡ�ı���ָ�����
                textCursor.movePosition(QTextCursor.End)  # ��ָ���ƶ���ĩβ
                self.plainTextEdit.setTextCursor(textCursor)

    # �жϵ�ǰ�������ֵ,��������ʱ������������µ��߼��ж�
    def getComboText(self):
        if self.comboBox.currentText() == 'Ӣ��':
            self._language = 'en'
        elif self.comboBox.currentText() == '����':
            self._language = 'ja'
        elif self.comboBox.currentText() == '����':
            self._language = 'zh-CN'
        return self._language

    # ��ȡ�ı����ڵ�����
    def Translate(self):
        originalText_ = self.plainTextEdit.toPlainText()
        originalText = self.isCut(originalText_)
        if originalText != '':
            # """����������ʹ�����ż��������429���쳣(���ð汾)"""
            # # print(originalText)
            # """����GoogleTrans�ӿڣ��˽ӿ����ԡ�https://github.com/VictorZhang2014/free-google-translate��,��л.
            # �ӿ�ʹ�ã�query������һ��������ʾҪ��������֣��ڶ���������ʾҪ���������
            # ���ز���˵������һ��ֵԴ���ԣ��ڶ���ΪԴ�������࣬������ΪĿ�����ԣ����ĸ�ΪĿ����������"""
            # transRe = GoogleTrans().query(originalText,lang_to=self._language)
            # target = transRe[2]
            # original = transRe[0]
            # self.translateText.setPlainText(target)
            """�Ż���ʹ�ô˰汾���˷������ԡ�https://github.com/mouuff/mtranslate������л
            ����ʹ�ã���һ������ΪҪ��������֣��ڶ���ΪĿ�����ԣ�������ΪԴ���ԣ�����������Զ�ʶ��
            ���ε�������д��staticĿ¼�µ�languageList�ļ�"""
            language = self.getComboText()
            target = translate(originalText, language)
            self.translateText.setPlainText(target)
            self.currentText = self.comboBox.currentText()
        else:
            self.plainTextEdit.setPlaceholderText('����û����������')

    # ת��Ŀ��������Դ���� �����Ҫת��������Ϊ���ģ����޷�ʵ��Դ������Ŀ�������ڲ��л�ʱ��ת����Ҫʵ����Ҫ��ȡԴ���Ե�currentText
    #
    # ��translate�����У��޷���ȡ���Զ���⵽��Դ���ԣ����Դ˹�����ʱ��������
    def reverse(self):
        self.countFlag += 1
        if self.countFlag % 2 == 0:
            self.comboBox.setCurrentText('����')
        else:
            self.comboBox.setCurrentText(self.currentText)
        original = self.translateText.toPlainText()
        # original = self.isCut(original_)
        self.plainTextEdit.setPlainText(original)
        reverseLanguage = self.getComboText()
        target = translate(original, reverseLanguage)
        self.isInputFlag = False
        self.translateText.setPlainText(target)

    # ��������
    def copyTranslate(self):
        text = self.translateText.toPlainText()
        if text == '':
            msgBox = QMessageBox(QMessageBox.Information, '��ʾ', '�ƺ�û��ʲô����')
            msgBox.exec_()
        else:
            clipBoard = QApplication.clipboard()
            clipBoard.setText(text)
            msgBox = QMessageBox(QMessageBox.Information, '��ʾ', '�����Ѹ���')
            msgBox.exec_()

    # ����ͳ���Լ��ı���̬�߼��ж�
    def countText(self):
        originalText_ = self.plainTextEdit.toPlainText()
        size = len(originalText_)
        countSize = str(size) + '/9999'
        self.countLabel.setText(countSize)
        self.countLabel.setStyleSheet("color:grey")
        if size > self.MAXSIZE:
            # """���ﲻʹ��deleteChar��ԭ������Ϊ��
            # ɾ��ָ����ָλ�õ�ǰһ���ַ�,���ﵽ����ַ�ʱ����ʱ����ָ�����ģ��ٴ������ʹ���ı�����+1,��ʱָ����ƶ���+2��λ��
            # """
            # textCursor.deletePreviousChar()
            originalText = self.isCut(originalText_)
            self.plainTextEdit.setPlainText(originalText)
            textCursor = self.plainTextEdit.textCursor()  # ��ȡ�ı���ָ�����
            textCursor.movePosition(QTextCursor.End)  # ��ָ���ƶ���ĩβ
            self.plainTextEdit.setTextCursor(textCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Login()
    ex = TranslateWindow()
    ex.show()
    # RegEx = Reg()
    # RegEx.show()
    sys.exit(app.exec_())
