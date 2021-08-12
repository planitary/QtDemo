# coding:gbk
from PyQt5 import QtGui,QtWidgets,Qt
from Extra.MyQlabel import MyQLabel

class Reg(QtWidgets.QWidget):
    def setupUI(self):
        self.setObjectName("RegWindow")
        self.setStyleSheet("#RegWindow{"
                           "background-color:white}")
        self.setFixedSize(650,400)
        self.setWindowTitle('ע��')
        self.setWindowIcon(QtGui.QIcon("../ICO/ע��.png"))

        self.Regtext = '�û�ע��'

        #����logo
        self.RegtopPic = QtGui.QPixmap("../ICO/��¼.webp")
        scaredTopPic = self.RegtopPic.scaled(650,140)           # ���մ�С�и�ͼƬ
        self.Reglabel = QtWidgets.QLabel(self)
        self.Reglabel.setPixmap(scaredTopPic)                   # ��ͼƬ��䵽����label

        #��������
        self.RegtopMsg = QtWidgets.QLabel(self)
        self.RegtopMsg.setText(self.Regtext)
        self.RegtopMsg.setStyleSheet("QWidget{"
                             "color:white;font-weight:600;background:transparent;font-size:30px;}")
        self.RegtopMsg.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegtopMsg.move(290,50)
        self.RegtopMsg.setAlignment(Qt.Qt.AlignCenter)             # �������ּ�϶��ʹ���Ϸ�label��widget�޷���
        self.RegtopMsg.raise_()

        # ע���������ʽ
        self.RegloginWidget = QtWidgets.QWidget(self)
        self.RegloginWidget.move(0,140)                         # ע���λ��
        self.RegloginWidget.setGeometry(0,140,580,220)              # ע����widget��С
        hbox = QtWidgets.QHBoxLayout()                            # ע���ˮƽ���֣����Ϊlogo���Ҳ�Ϊ��

        # ע������logo
        self.RegleftLogo = QtWidgets.QLabel(self)
        self.RegleftLogoPic = QtGui.QPixmap('../ICO/logo.webp')
        scaredLogo = self.RegleftLogoPic.scaled(160,120)
        self.RegleftLogo.setPixmap(scaredLogo)
        self.RegleftLogo.setAlignment(Qt.Qt.AlignCenter)
        hbox.addWidget(self.RegleftLogo,1)

        #ע����Ҳ��
        self.RegformLayout = QtWidgets.QFormLayout()
        self.RegusernameLabel = QtWidgets.QLabel('�û���:')
        self.RegusernameLabel.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegusernameEdit = QtWidgets.QLineEdit()
        self.RegusernameEdit.setFixedSize(270,38)                   # ���Ʊ������Ҳ��ı���Ĵ�С
        self.RegpwdLabel = QtWidgets.QLabel('����:')
        self.RegpwdLabel.setFont(QtGui.QFont("Microsoft YaHei"))
        self.RegpwdEdit = QtWidgets.QLineEdit()
        self.RegpwdEdit.setFixedSize(270,38)
        self.RegpwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)              # �����ı�������ģʽΪ����
        self.RegpwdConfirmLabel = QtWidgets.QLabel('ȷ������:')
        self.RegpwdConfirmLabel.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegpwdConfirmEdit = QtWidgets.QLineEdit()
        self.RegpwdConfirmEdit.setFixedSize(270,38)
        self.RegpwdConfirmEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RegbtnLogin = QtWidgets.QPushButton('ע��')
        self.RegbtnLogin.setFixedSize(270,40)
        self.RegbtnLogin.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegbtnLogin.setObjectName('loginbtn')
        self.RegbtnLogin.setStyleSheet('#loginbtn{'             
                               'background-color:#2c7adf;color:#fff;border-radius:4px;}')      # ��ť�߿�Բ��


        self.RegformLayout.addRow(self.RegusernameLabel,self.RegusernameEdit)
        self.RegformLayout.addRow(self.RegpwdLabel,self.RegpwdEdit)
        self.RegformLayout.addRow(self.RegpwdConfirmLabel,self.RegpwdConfirmEdit)
        self.RegformLayout.addWidget(self.RegbtnLogin)                           # ע�ᰴť��ӽ�������
        # self.RegformLayout.addWidget(self.RegregLabel)
        hbox.setAlignment(Qt.Qt.AlignCenter)

        # ���������
        self.RegformLayout.setHorizontalSpacing(20)    # ���ڱ�ǩ���ı���ļ��
        self.RegformLayout.setVerticalSpacing(12)           # ��ͬ��䴹ֱ���

        hbox.addLayout(self.RegformLayout,2)                # �Ҳ����ӽ�����ˮƽ������

        self.RegregLabel = MyQLabel(self)               # ע���ǩ
        # ���ı���Qlabelʹ��setTextFormat��ָ��չʾ���ı����Ǹ��ı�
        regHtml = '''
                    <font color='#8a8a8a' size ='3'>�����˺�?ȥ��¼</font>
                     <img src = '../ICO/�Ҽ�ͷ_new.png' height='22' weight ='12'
                     style="vertical-align:top;">'''
        self.RegregLabel.setText(regHtml)
        self.RegregLabel.setTextFormat(Qt.Qt.RichText)
        self.RegregLabel.setObjectName('regLabel')
        self.RegregLabel.setStyleSheet('#regLabel{'
                                    'color:grey;font-size:14px;}')
        # self.RegregLabel.setIndent(66)
        self.RegregLabel.setFixedSize(130,20)
        self.RegregLabel.setCursor(Qt.Qt.PointingHandCursor)               # ���������ʽ
        self.RegregLabel.move(366,350)

        self.RegloginWidget.setLayout(hbox)
        self.Regcenter()

    def Regcenter(self):
        """���ظ����ڵļ�����״��С��������Ϊ�������ڣ�������Ļ��С,Qwidget�̳���QMainWindow����������ΪQMainWindow��LoginFrame
        �̳���Qwidget�����ﷵ�ظ���Qwidget��С�����С�ڹ��캯����ָ��Ϊ650*400
        ʵ�����ﴴ����һ����ע�ᴰ��һ����С�����ξ���"""
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
