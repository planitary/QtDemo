# coding:gbk
from PyQt5 import QtCore,QtGui,QtWidgets,Qt

class LoginForm(object):
    def setupUI(self,Widget):
        Widget.setObjectName("loginWindow")
        Widget.setStyleSheet("#loginWindow{"
                           "background-color:white}")
        Widget.setFixedSize(650,400)
        Widget.setWindowTitle('��¼')
        Widget.setWindowIcon(QtGui.QIcon("../ICO/����.png"))

        self.text = '�û���¼'

        #����logo
        self.topPic = QtGui.QPixmap("../ICO/��¼.webp")
        scaredTopPic = self.topPic.scaled(650,140)           # ���մ�С�и�ͼƬ
        self.label = QtWidgets.QLabel(Widget)
        self.label.setPixmap(scaredTopPic)                   # ��ͼƬ��䵽����label

        #��������
        self.topMsg = QtWidgets.QLabel(Widget)
        self.topMsg.setText(self.text)
        self.topMsg.setStyleSheet("QWidget{"
                             "color:white;font-weight:600;background:transparent;font-size:30px;}")
        self.topMsg.setFont(QtGui.QFont('Microsoft YaHei'))
        self.topMsg.move(290,50)
        self.topMsg.setAlignment(Qt.Qt.AlignCenter)             # �������ּ�϶��ʹ���Ϸ�label��widget�޷���
        self.topMsg.raise_()

        # ��¼��������ʽ
        self.loginWidget = QtWidgets.QWidget(Widget)
        self.loginWidget.move(0,140)                         # ��¼��λ��
        self.loginWidget.setGeometry(0,140,650,260)              # ��¼���widget��С
        hbox = QtWidgets.QHBoxLayout()                            # ��¼��ˮƽ���֣����Ϊlogo���Ҳ�Ϊ��

        # ��¼�����logo
        self.leftLogo = QtWidgets.QLabel(Widget)
        self.leftLogoPic = QtGui.QPixmap('../ICO/logo.webp')
        scaredLogo = self.leftLogoPic.scaled(160,120)
        self.leftLogo.setPixmap(scaredLogo)
        self.leftLogo.setAlignment(Qt.Qt.AlignCenter)
        hbox.addWidget(self.leftLogo,1)

        #��¼���Ҳ��
        self.formLayout = QtWidgets.QFormLayout()
        self.usernameLabel = QtWidgets.QLabel('�û���:')
        self.usernameLabel.setFont(QtGui.QFont('Microsoft YaHei'))
        self.usernameEdit = QtWidgets.QLineEdit()
        self.usernameEdit.setFixedSize(270,38)                   # ���Ʊ������Ҳ��ı���Ĵ�С
        self.pwdLabel = QtWidgets.QLabel('����:')
        self.pwdLabel.setFont(QtGui.QFont("Microsoft YaHei"))
        self.pwdEdit = QtWidgets.QLineEdit()
        self.pwdEdit.setFixedSize(270,38)
        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)              # �����ı�������ģʽΪ����
        self.btnLogin = QtWidgets.QPushButton('��¼')
        self.btnLogin.setFixedSize(270,40)
        self.btnLogin.setFont(QtGui.QFont('Microsoft YaHei'))
        self.btnLogin.setObjectName('loginbtn')
        self.btnLogin.setStyleSheet('#loginbtn{'             
                               'background-color:#2c7adf;color:#fff;border-radius:4px;}')      # ��ť�߿�Բ��

        self.formLayout.addRow(self.usernameLabel,self.usernameEdit)
        self.formLayout.addRow(self.pwdLabel,self.pwdEdit)
        self.formLayout.addWidget(self.btnLogin)                           # ��¼��ť��ӽ�������
        hbox.setAlignment(Qt.Qt.AlignCenter)

        # ���������
        self.formLayout.setHorizontalSpacing(20)    # ���ڱ�ǩ���ı���ļ��
        self.formLayout.setVerticalSpacing(12)           # ��ͬ��䴹ֱ���

        hbox.addLayout(self.formLayout,2)                # �Ҳ����ӽ�����ˮƽ������
        self.loginWidget.setLayout(hbox)

        self.center(Widget)

    def center(self,Widget):
        """���ظ����ڵļ�����״��С��������Ϊ�������ڣ�������Ļ��С,Qwidget�̳���QMainWindow����������ΪQMainWindow��LoginFrame
        �̳���Qwidget�����ﷵ�ظ���Qwidget��С�����С�ڹ��캯����ָ��Ϊ650*400
        ʵ�����ﴴ����һ���͵�¼����һ����С�����ξ���"""
        qr = Widget.frameGeometry()
        # print(qr)
        # ���ؿ�����Ļ��С�������������ȣ�center()��������ֵ������,�õ�������Ļ�����ĵ�
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # print(QDesktopWidget().availableGeometry())
        # print(cp)
        # ���ָþ��δ�С���䣬��������(movecenter)�ƶ�����Ļ���ĵ�
        qr.moveCenter(cp)
        # ���ھ�������Ļ���ģ��ʽ�LoginFrame�������Ͻ��ƶ������ξ������ϽǺ��������������Ļ������
        Widget.move(qr.topLeft())






























