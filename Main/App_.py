# coding:gbk
import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class App(QWidget):

    # def __init__(self):
    #     super(App, self).__init__()
    #     self.Login()
    #
    # def Login(self):
    #     """ ��QWidget����QDialog���ò��ֵ�ʱ��ʽ�ܼ򵥡�������һ�����֣�mainLayout��
    #     Ȼ��ͣ�ذѸ����ؼ���mainLayout����ţ�������setLayout(mainLayout)�����ˡ�
    #     QMainWindow��ʹ�����������ʱ��ȴ�����ã���ΪQMainWindow��Ĭ����layout�ģ������ٴ�����layout��ʧЧ """
    #
    #     """Ҫ��QMainWidget�������֣�����Ĳ���Ӧ���������ģ�
    #     ��һ������һ��QWidgetʵ����      ����ͼ��ע��A
    #     Ȼ�󴴽�һ������mainLayout����������Ҫ�����пؼ���������ţ����������˵�����״̬������) ����ͼע��B
    #     ��һ�����ǽ�widget�Ĳ�������ΪmainLayout������ӵ�centralWidget��            ����ͼע��C"""
    #     newWidget = QWidget()                   # A
    #
    #     horiLayout = QHBoxLayout()
    #     nameLabel = QLabel('�û���:')
    #     nameLineEdit = QLineEdit('')
    #     pwdLabel = QLabel('����:')
    #     pwdLineEdit = QLineEdit('')
    #     horiLayout.addWidget(nameLabel)
    #     horiLayout.addWidget(nameLineEdit,1)
    #     horiLayout.addWidget(pwdLabel)
    #     horiLayout.addWidget(pwdLineEdit,1)
    #     newWidget.setLayout(horiLayout)         # B
    #     self.setCentralWidget(newWidget)        # C
    #
    #     # ����˳��˵�
    #     exitAciton= QAction(QIcon("../ICO/�ر�.png"),'&�˳�',self)     # Ϊ�ӹ���ָ����ʾ���ı���ͼ��
    #     exitAciton.setShortcut('ctrl+Q')            # Ϊ�ӹ��ܰ󶨿�ݼ�
    #     exitAciton.setToolTip('ѡ��')            # Ϊ�ӹ�������������tips
    #     exitAciton.triggered.connect(qApp.quit)      # �ӹ�����Ӵ�������
    #     # frame.HLine = 1
    #     # frame.setFrameShape(QFrame.HLine)
    #     # ���menubar�����˳�����
    #     menubar = self.menuBar()
    #     menubar.setNativeMenuBar(False)
    #     exit = menubar.addMenu('&�˳�')                   # ָ���˵�����
    #     exit.addAction(exitAciton)                  # ��exitAction���˵�
    #     self.statusBar()
    #
    #     # ���ô������
    #     # self.setFixedSize(self.width(),self.height())
    #     self.setGeometry(300,360,300,200)
    #     self.setWindowTitle('��¼')
    #     self.show()

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setObjectName('LoginWindow')
        self.setStyleSheet("#LoginWindow{"
                           "background-color:white}")
        self.setFixedSize(650,400)
        self.setWindowTitle('��¼')
        self.setWindowIcon(QIcon('../ICO/����.png'))
        self.TopDisplay = '�û���¼'

        #����logo
        topPic = QPixmap('../ICO/��¼.webp')
        scaredPixmap = topPic.scaled(650,140)           # ���մ�С�и�ͼƬ
        topLabel = QLabel(self)
        topLabel.setPixmap(scaredPixmap)                # ��ͼƬ��䵽����label
        # ��������
        topText = QLabel(self)
        topText.setText(self.TopDisplay)
        topText.setStyleSheet("QWidget{"
                              "color:white;font-weight:600;background:transparent;font-size:30px;}")
        topText.setFont(QFont("Microsoft YaHei"))
        topText.move(150,50)
        topText.setAlignment(Qt.Qt.AlignCenter)             # �������ּ�϶��ʹ���Ϸ�label��widget�޷���
        topText.raise_()
        # ��¼��
        login = QWidget(self)
        login.move(0,140)                           # ��¼��λ��
        login.setGeometry(0,140,650,260)                # ��¼���widget��С
        hbox = QHBoxLayout()                        # ��¼��ˮƽ���֣����Ϊlogo���Ҳ�Ϊ��
        # ��¼�����logo
        loginLogo = QLabel(self)
        logoPic = QPixmap("../ICO/logo.webp")
        scaredLogoPic = logoPic.scaled(100,100)
        loginLogo.setPixmap(scaredLogoPic)
        loginLogo.setAlignment(Qt.Qt.AlignCenter)           # ���logo����widget�ھ���
        # �Ҳ��
        formLayout = QFormLayout()                      # �Ҳ��Ϊ������
        loginUsername = QLabel('�û���:')
        loginUsername.setFont(QFont("Microsoft YaHei"))
        loginUsernameEdit = QLineEdit()
        loginUsernameEdit.setFixedSize(270,38)          # ���Ʊ������Ҳ��ı���Ĵ�С

        loginPwd = QLabel('����:')
        loginPwd.setFont(QFont("Microsoft YaHei"))
        loginPwdEdit = QLineEdit()
        loginPwdEdit.setEchoMode(QLineEdit.Password)        # �����ı�������ģʽΪ����
        loginPwdEdit.setFixedSize(270,38)

        loginbtn = QPushButton('��¼')
        loginbtn.setFixedSize(270,40)
        loginbtn.setFont(QFont('Microsoft YaHei'))
        loginbtn.setObjectName("loginbtn")
        loginbtn.setStyleSheet("#loginbtn{"
                               "background-color:#2c7adf;color:#fff;border:none;border-radius:4px;}")        # ��ť��ʽ
        formLayout.addRow(loginUsername,loginUsernameEdit)
        formLayout.addRow(loginPwd,loginPwdEdit)
        formLayout.addWidget(loginbtn)
        hbox.setAlignment(Qt.Qt.AlignCenter)
        # �������
        formLayout.setHorizontalSpacing(20)
        formLayout.setVerticalSpacing(12)

        hbox.addLayout(formLayout,2)                # ��¼�Ҳ��ˮƽ����
        login.setLayout(hbox)                       # �����¼��
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = App()
    sys.exit(app.exec_())