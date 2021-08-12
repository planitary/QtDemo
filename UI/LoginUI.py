# coding:gbk
from PyQt5 import QtGui,QtWidgets,Qt
from Extra.MyQlabel import MyQLabel

class LoginForm(QtWidgets.QWidget):
    def setupUI(self):
        self.setObjectName("loginWindow")
        self.setStyleSheet("#loginWindow{"
                           "background-color:white}")
        self.setFixedSize(650,400)
        self.setWindowTitle('��¼')
        self.setWindowIcon(QtGui.QIcon("../ICO/����.png"))

        self.text = '�û���¼'

        #����logo
        self.topPic = QtGui.QPixmap("../ICO/��¼.webp")
        scaredTopPic = self.topPic.scaled(650,140)           # ���մ�С�и�ͼƬ
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(scaredTopPic)                   # ��ͼƬ��䵽����label

        #��������
        self.topMsg = QtWidgets.QLabel(self)
        self.topMsg.setText(self.text)
        self.topMsg.setStyleSheet("QWidget{"
                             "color:white;font-weight:600;background:transparent;font-size:30px;}")
        self.topMsg.setFont(QtGui.QFont('Microsoft YaHei'))
        self.topMsg.move(290,50)
        self.topMsg.setAlignment(Qt.Qt.AlignCenter)             # �������ּ�϶��ʹ���Ϸ�label��widget�޷���
        self.topMsg.raise_()

        # ��¼��������ʽ
        self.loginWidget = QtWidgets.QWidget(self)
        self.loginWidget.move(0,140)                         # ��¼��λ��
        self.loginWidget.setGeometry(0,140,580,200)              # ��¼��widget��С
        hbox = QtWidgets.QHBoxLayout()                            # ��¼��ˮƽ���֣����Ϊlogo���Ҳ�Ϊ��

        # ��¼�����logo
        self.leftLogo = QtWidgets.QLabel(self)
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
        self.usernameEdit.setPlaceholderText('�������û���')
        self.pwdLabel = QtWidgets.QLabel('����:')
        self.pwdLabel.setFont(QtGui.QFont("Microsoft YaHei"))
        self.pwdEdit = QtWidgets.QLineEdit()
        self.pwdEdit.setFixedSize(270,38)
        self.pwdEdit.setPlaceholderText('����������')
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
        # self.formLayout.addWidget(self.regLabel)
        hbox.setAlignment(Qt.Qt.AlignCenter)

        # ���������
        self.formLayout.setHorizontalSpacing(20)    # ���ڱ�ǩ���ı���ļ��
        self.formLayout.setVerticalSpacing(12)           # ��ͬ��䴹ֱ���

        hbox.addLayout(self.formLayout,2)                # �Ҳ����ӽ�����ˮƽ������

        self.regLabel = MyQLabel(self)               # ע���ǩ
        # ���ı���Qlabelʹ��setTextFormat��ָ��չʾ���ı����Ǹ��ı�
        regHtml = '''
                    <font color='#8a8a8a' size ='3'>��û�˺�?ȥע��</font>
                     <img src = '../ICO/�Ҽ�ͷ_new.png' height='22' weight ='12'
                     style="vertical-align:top;">'''
        self.regLabel.setText(regHtml)
        self.regLabel.setTextFormat(Qt.Qt.RichText)
        self.regLabel.setObjectName('regLabel')
        self.regLabel.setStyleSheet('#regLabel{'
                                    'color:grey;font-size:14px;}')
        # self.regLabel.setIndent(66)
        self.regLabel.setFixedSize(130,20)
        self.regLabel.setCursor(Qt.Qt.PointingHandCursor)               # ���������ʽ
        self.regLabel.move(346,320)

        self.loginWidget.setLayout(hbox)
        self.center()
        self.show()

    def center(self):
        """���ظ����ڵļ�����״��С��������Ϊ�������ڣ�������Ļ��С,Qwidget�̳���QMainWindow����������ΪQMainWindow��LoginFrame
        �̳���Qwidget�����ﷵ�ظ���Qwidget��С�����С�ڹ��캯����ָ��Ϊ650*400
        ʵ�����ﴴ����һ���͵�¼����һ����С�����ξ���"""
        qr = self.frameGeometry()
        # print(qr)
        # ���ؿ�����Ļ��С�������������ȣ�center()��������ֵ������,�õ�������Ļ�����ĵ�
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # print(QDesktopWidget().availableGeometry())
        # print(cp)
        # ���ָþ��δ�С���䣬��������(movecenter)�ƶ�����Ļ���ĵ�
        qr.moveCenter(cp)
        # ���ھ�������Ļ���ģ��ʽ�LoginFrame�������Ͻ��ƶ������ξ������ϽǺ��������������Ļ������
        self.move(qr.topLeft())






























