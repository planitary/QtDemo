# coding:gbk
import sys
from PyQt5.QtWidgets import  QMessageBox, QApplication
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QCoreApplication
from Controller.DController import LoginController,RegController
from UI import LoginUI, RegisterUI,TranslateUI
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
        self.LoginEx = Login()
        self.LoginEx.show()

class TranslateWindow(TranslateUI.TranslateMainWindow):
    countFlag = -1  # �����л�λ������ΪĿ���������֣�ż��ΪԴ��������
    currentText = ''                # ����flag������comboboxѡ�������

    def __init__(self):
        super(TranslateWindow, self).__init__()
        self.setupUi()
        self.translateAction()


    def translateAction(self):
        self.button.clicked.connect(self.Translate)
        self.label.connectSlot(self.reverse)
        self.copybtn.connectSlot(self.copyTranslate)
        self.plainTextEdit.textChanged.connect(self.countText)


    def getComboText(self):
        # �жϵ�ǰ�������ֵ
        if self.comboBox.currentText() == 'Ӣ��':
            self._language = 'en'
        elif self.comboBox.currentText() == '����':
            self._language = 'ja'
        elif self.comboBox.currentText() == '����':
            self._language = 'zh-CN'
        return self._language

    def Translate(self):
        # ��ȡ�ı����ڵ�����
        originalText = self.plainTextEdit.toPlainText()

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
            target = translate(originalText,language)
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
        self.plainTextEdit.setPlainText(original)
        reverseLanguage = self.getComboText()
        target = translate(original,reverseLanguage)
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
            msgBox = QMessageBox(QMessageBox.Information,'��ʾ','�����Ѹ���')
            msgBox.exec_()

    # ����ͳ��
    def countText(self):
        originalText = self.plainTextEdit.toPlainText()
        size = len(originalText)
        if size == 0:
            self.countLabel.setVisible(False)
        else:
            self.countLabel.setVisible(True)
            countSize = str(size) + '/5000'
            self.countLabel.setText(countSize)
            self.countLabel.setStyleSheet("color:grey")
            if size > 5000:
                textCursor = self.plainTextEdit.textCursor()    # ��ȡ�ı���ָ�����
                # textCursor.movePosition(QTextCursor.End)                # ��ָ���ƶ���ĩβ
                """���ﲻʹ��deleteChar��ԭ������Ϊ��
                ɾ��ָ����ָλ�õ�ǰһ���ַ�,���ﵽ����ַ�ʱ����ʱ����ָ�����ģ��ٴ������ʹ���ı�����+1,��ʱָ����ƶ���+2��λ��
                """
                textCursor.deletePreviousChar()
                msgBox = QMessageBox(QMessageBox.Warning,'��ʾ','���������������!')
                msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Login()
    ex = TranslateWindow()
    ex.show()
    # RegEx = Reg()
    # RegEx.show()
    sys.exit(app.exec_())
