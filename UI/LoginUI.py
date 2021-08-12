# coding:gbk
from PyQt5 import QtGui,QtWidgets,Qt
from Extra.MyQlabel import MyQLabel

class LoginForm(QtWidgets.QWidget):
    def setupUI(self):
        self.setObjectName("loginWindow")
        self.setStyleSheet("#loginWindow{"
                           "background-color:white}")
        self.setFixedSize(650,400)
        self.setWindowTitle('登录')
        self.setWindowIcon(QtGui.QIcon("../ICO/咖啡.png"))

        self.text = '用户登录'

        #顶部logo
        self.topPic = QtGui.QPixmap("../ICO/登录.webp")
        scaredTopPic = self.topPic.scaled(650,140)           # 按照大小切割图片
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(scaredTopPic)                   # 将图片填充到顶部label

        #顶部文字
        self.topMsg = QtWidgets.QLabel(self)
        self.topMsg.setText(self.text)
        self.topMsg.setStyleSheet("QWidget{"
                             "color:white;font-weight:600;background:transparent;font-size:30px;}")
        self.topMsg.setFont(QtGui.QFont('Microsoft YaHei'))
        self.topMsg.move(290,50)
        self.topMsg.setAlignment(Qt.Qt.AlignCenter)             # 调整布局间隙，使得上方label和widget无缝结合
        self.topMsg.raise_()

        # 登录表单整体样式
        self.loginWidget = QtWidgets.QWidget(self)
        self.loginWidget.move(0,140)                         # 登录表单位置
        self.loginWidget.setGeometry(0,140,580,200)              # 登录表单widget大小
        hbox = QtWidgets.QHBoxLayout()                            # 登录表单水平布局，左侧为logo，右侧为表单

        # 登录表单左侧logo
        self.leftLogo = QtWidgets.QLabel(self)
        self.leftLogoPic = QtGui.QPixmap('../ICO/logo.webp')
        scaredLogo = self.leftLogoPic.scaled(160,120)
        self.leftLogo.setPixmap(scaredLogo)
        self.leftLogo.setAlignment(Qt.Qt.AlignCenter)
        hbox.addWidget(self.leftLogo,1)

        #登录表单右侧表单
        self.formLayout = QtWidgets.QFormLayout()
        self.usernameLabel = QtWidgets.QLabel('用户名:')
        self.usernameLabel.setFont(QtGui.QFont('Microsoft YaHei'))
        self.usernameEdit = QtWidgets.QLineEdit()
        self.usernameEdit.setFixedSize(270,38)                   # 限制表单布局右侧文本框的大小
        self.usernameEdit.setPlaceholderText('请输入用户名')
        self.pwdLabel = QtWidgets.QLabel('密码:')
        self.pwdLabel.setFont(QtGui.QFont("Microsoft YaHei"))
        self.pwdEdit = QtWidgets.QLineEdit()
        self.pwdEdit.setFixedSize(270,38)
        self.pwdEdit.setPlaceholderText('请输入密码')
        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)              # 设置文本框输入模式为暗文
        self.btnLogin = QtWidgets.QPushButton('登录')
        self.btnLogin.setFixedSize(270,40)
        self.btnLogin.setFont(QtGui.QFont('Microsoft YaHei'))
        self.btnLogin.setObjectName('loginbtn')
        self.btnLogin.setStyleSheet('#loginbtn{'             
                               'background-color:#2c7adf;color:#fff;border-radius:4px;}')      # 按钮边框圆角


        self.formLayout.addRow(self.usernameLabel,self.usernameEdit)
        self.formLayout.addRow(self.pwdLabel,self.pwdEdit)
        self.formLayout.addWidget(self.btnLogin)                           # 登录按钮添加进表单布局
        # self.formLayout.addWidget(self.regLabel)
        hbox.setAlignment(Qt.Qt.AlignCenter)

        # 调整表单间距
        self.formLayout.setHorizontalSpacing(20)    # 组内标签和文本框的间隔
        self.formLayout.setVerticalSpacing(12)           # 不同组间垂直间隔

        hbox.addLayout(self.formLayout,2)                # 右侧表单添加进整体水平布局中

        self.regLabel = MyQLabel(self)               # 注册标签
        # 富文本，Qlabel使用setTextFormat来指定展示纯文本还是富文本
        regHtml = '''
                    <font color='#8a8a8a' size ='3'>还没账号?去注册</font>
                     <img src = '../ICO/右箭头_new.png' height='22' weight ='12'
                     style="vertical-align:top;">'''
        self.regLabel.setText(regHtml)
        self.regLabel.setTextFormat(Qt.Qt.RichText)
        self.regLabel.setObjectName('regLabel')
        self.regLabel.setStyleSheet('#regLabel{'
                                    'color:grey;font-size:14px;}')
        # self.regLabel.setIndent(66)
        self.regLabel.setFixedSize(130,20)
        self.regLabel.setCursor(Qt.Qt.PointingHandCursor)               # 鼠标悬浮样式
        self.regLabel.move(346,320)

        self.loginWidget.setLayout(hbox)
        self.center()
        self.show()

    def center(self):
        """返回父窗口的几何形状大小，当窗口为顶级窗口，返回屏幕大小,Qwidget继承自QMainWindow，顶级窗口为QMainWindow，LoginFrame
        继承自Qwidget，这里返回父类Qwidget大小，其大小在构造函数中指定为650*400
        实则这里创立了一个和登录窗体一样大小的无形矩形"""
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






























