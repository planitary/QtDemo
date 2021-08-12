# coding:gbk
from PyQt5 import QtGui,QtWidgets,Qt
from Extra.MyQlabel import MyQLabel

class Reg(QtWidgets.QWidget):
    def setupUI(self):
        self.setObjectName("RegWindow")
        self.setStyleSheet("#RegWindow{"
                           "background-color:white}")
        self.setFixedSize(650,400)
        self.setWindowTitle('注册')
        self.setWindowIcon(QtGui.QIcon("../ICO/注册.png"))

        self.Regtext = '用户注册'

        #顶部logo
        self.RegtopPic = QtGui.QPixmap("../ICO/登录.webp")
        scaredTopPic = self.RegtopPic.scaled(650,140)           # 按照大小切割图片
        self.Reglabel = QtWidgets.QLabel(self)
        self.Reglabel.setPixmap(scaredTopPic)                   # 将图片填充到顶部label

        #顶部文字
        self.RegtopMsg = QtWidgets.QLabel(self)
        self.RegtopMsg.setText(self.Regtext)
        self.RegtopMsg.setStyleSheet("QWidget{"
                             "color:white;font-weight:600;background:transparent;font-size:30px;}")
        self.RegtopMsg.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegtopMsg.move(290,50)
        self.RegtopMsg.setAlignment(Qt.Qt.AlignCenter)             # 调整布局间隙，使得上方label和widget无缝结合
        self.RegtopMsg.raise_()

        # 注册表单整体样式
        self.RegloginWidget = QtWidgets.QWidget(self)
        self.RegloginWidget.move(0,140)                         # 注册表单位置
        self.RegloginWidget.setGeometry(0,140,580,220)              # 注册表达widget大小
        hbox = QtWidgets.QHBoxLayout()                            # 注册表单水平布局，左侧为logo，右侧为表单

        # 注册表单左侧logo
        self.RegleftLogo = QtWidgets.QLabel(self)
        self.RegleftLogoPic = QtGui.QPixmap('../ICO/logo.webp')
        scaredLogo = self.RegleftLogoPic.scaled(160,120)
        self.RegleftLogo.setPixmap(scaredLogo)
        self.RegleftLogo.setAlignment(Qt.Qt.AlignCenter)
        hbox.addWidget(self.RegleftLogo,1)

        #注册表单右侧表单
        self.RegformLayout = QtWidgets.QFormLayout()
        self.RegusernameLabel = QtWidgets.QLabel('用户名:')
        self.RegusernameLabel.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegusernameEdit = QtWidgets.QLineEdit()
        self.RegusernameEdit.setFixedSize(270,38)                   # 限制表单布局右侧文本框的大小
        self.RegpwdLabel = QtWidgets.QLabel('密码:')
        self.RegpwdLabel.setFont(QtGui.QFont("Microsoft YaHei"))
        self.RegpwdEdit = QtWidgets.QLineEdit()
        self.RegpwdEdit.setFixedSize(270,38)
        self.RegpwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)              # 设置文本框输入模式为暗文
        self.RegpwdConfirmLabel = QtWidgets.QLabel('确认密码:')
        self.RegpwdConfirmLabel.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegpwdConfirmEdit = QtWidgets.QLineEdit()
        self.RegpwdConfirmEdit.setFixedSize(270,38)
        self.RegpwdConfirmEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RegbtnLogin = QtWidgets.QPushButton('注册')
        self.RegbtnLogin.setFixedSize(270,40)
        self.RegbtnLogin.setFont(QtGui.QFont('Microsoft YaHei'))
        self.RegbtnLogin.setObjectName('loginbtn')
        self.RegbtnLogin.setStyleSheet('#loginbtn{'             
                               'background-color:#2c7adf;color:#fff;border-radius:4px;}')      # 按钮边框圆角


        self.RegformLayout.addRow(self.RegusernameLabel,self.RegusernameEdit)
        self.RegformLayout.addRow(self.RegpwdLabel,self.RegpwdEdit)
        self.RegformLayout.addRow(self.RegpwdConfirmLabel,self.RegpwdConfirmEdit)
        self.RegformLayout.addWidget(self.RegbtnLogin)                           # 注册按钮添加进表单布局
        # self.RegformLayout.addWidget(self.RegregLabel)
        hbox.setAlignment(Qt.Qt.AlignCenter)

        # 调整表单间距
        self.RegformLayout.setHorizontalSpacing(20)    # 组内标签和文本框的间隔
        self.RegformLayout.setVerticalSpacing(12)           # 不同组间垂直间隔

        hbox.addLayout(self.RegformLayout,2)                # 右侧表单添加进整体水平布局中

        self.RegregLabel = MyQLabel(self)               # 注册标签
        # 富文本，Qlabel使用setTextFormat来指定展示纯文本还是富文本
        regHtml = '''
                    <font color='#8a8a8a' size ='3'>已有账号?去登录</font>
                     <img src = '../ICO/右箭头_new.png' height='22' weight ='12'
                     style="vertical-align:top;">'''
        self.RegregLabel.setText(regHtml)
        self.RegregLabel.setTextFormat(Qt.Qt.RichText)
        self.RegregLabel.setObjectName('regLabel')
        self.RegregLabel.setStyleSheet('#regLabel{'
                                    'color:grey;font-size:14px;}')
        # self.RegregLabel.setIndent(66)
        self.RegregLabel.setFixedSize(130,20)
        self.RegregLabel.setCursor(Qt.Qt.PointingHandCursor)               # 鼠标悬浮样式
        self.RegregLabel.move(366,350)

        self.RegloginWidget.setLayout(hbox)
        self.Regcenter()

    def Regcenter(self):
        """返回父窗口的几何形状大小，当窗口为顶级窗口，返回屏幕大小,Qwidget继承自QMainWindow，顶级窗口为QMainWindow，LoginFrame
        继承自Qwidget，这里返回父类Qwidget大小，其大小在构造函数中指定为650*400
        实则这里创立了一个和注册窗体一样大小的无形矩形"""
        qr = self.frameGeometry()
        # print(qr)
        # 返回可用屏幕大小（不含任务栏等）center()锁定返回值的中心,得到整体屏幕的中心点
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # print(QDesktopWidget().availableGeometry())
        # print(cp)
        # 保持该矩形大小不变，将其中心(movecenter)移动到屏幕中心点
        qr.moveCenter(cp)
        # 由于矩形在屏幕中心，故将LoginFrame窗体左上角移动到无形矩形左上角后，整个窗体就在屏幕中心了
        self.move(qr.topLeft())
