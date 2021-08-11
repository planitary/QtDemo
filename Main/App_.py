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
    #     """ 给QWidget或者QDialog设置布局的时候方式很简单。创建好一个布局：mainLayout，
    #     然后不停地把各个控件往mainLayout里面放，最后调用setLayout(mainLayout)就行了。
    #     QMainWindow中使用这个方法的时候却不管用，因为QMainWindow是默认有layout的，所以再次设置layout会失效 """
    #
    #     """要想QMainWidget创建布局，合理的步骤应该是这样的：
    #     第一步创建一个QWidget实例，      见下图中注释A
    #     然后创建一个布局mainLayout，并把所需要的所有控件都往里面放（工具栏、菜单栏、状态栏除外) 见下图注释B
    #     最一步就是将widget的布局设置为mainLayout，并添加到centralWidget中            见下图注释C"""
    #     newWidget = QWidget()                   # A
    #
    #     horiLayout = QHBoxLayout()
    #     nameLabel = QLabel('用户名:')
    #     nameLineEdit = QLineEdit('')
    #     pwdLabel = QLabel('密码:')
    #     pwdLineEdit = QLineEdit('')
    #     horiLayout.addWidget(nameLabel)
    #     horiLayout.addWidget(nameLineEdit,1)
    #     horiLayout.addWidget(pwdLabel)
    #     horiLayout.addWidget(pwdLineEdit,1)
    #     newWidget.setLayout(horiLayout)         # B
    #     self.setCentralWidget(newWidget)        # C
    #
    #     # 添加退出菜单
    #     exitAciton= QAction(QIcon("../ICO/关闭.png"),'&退出',self)     # 为子功能指定显示的文本和图标
    #     exitAciton.setShortcut('ctrl+Q')            # 为子功能绑定快捷键
    #     exitAciton.setToolTip('选项')            # 为子功能添加鼠标悬浮tips
    #     exitAciton.triggered.connect(qApp.quit)      # 子功能添加触发动作
    #     # frame.HLine = 1
    #     # frame.setFrameShape(QFrame.HLine)
    #     # 添加menubar并绑定退出功能
    #     menubar = self.menuBar()
    #     menubar.setNativeMenuBar(False)
    #     exit = menubar.addMenu('&退出')                   # 指定菜单标题
    #     exit.addAction(exitAciton)                  # 绑定exitAction到菜单
    #     self.statusBar()
    #
    #     # 禁用窗口最大化
    #     # self.setFixedSize(self.width(),self.height())
    #     self.setGeometry(300,360,300,200)
    #     self.setWindowTitle('登录')
    #     self.show()

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setObjectName('LoginWindow')
        self.setStyleSheet("#LoginWindow{"
                           "background-color:white}")
        self.setFixedSize(650,400)
        self.setWindowTitle('登录')
        self.setWindowIcon(QIcon('../ICO/咖啡.png'))
        self.TopDisplay = '用户登录'

        #顶部logo
        topPic = QPixmap('../ICO/登录.webp')
        scaredPixmap = topPic.scaled(650,140)           # 按照大小切割图片
        topLabel = QLabel(self)
        topLabel.setPixmap(scaredPixmap)                # 将图片填充到顶部label
        # 顶部文字
        topText = QLabel(self)
        topText.setText(self.TopDisplay)
        topText.setStyleSheet("QWidget{"
                              "color:white;font-weight:600;background:transparent;font-size:30px;}")
        topText.setFont(QFont("Microsoft YaHei"))
        topText.move(150,50)
        topText.setAlignment(Qt.Qt.AlignCenter)             # 调整布局间隙，使得上方label和widget无缝结合
        topText.raise_()
        # 登录表单
        login = QWidget(self)
        login.move(0,140)                           # 登录表单位置
        login.setGeometry(0,140,650,260)                # 登录表达widget大小
        hbox = QHBoxLayout()                        # 登录表单水平布局，左侧为logo，右侧为表单
        # 登录表单左侧logo
        loginLogo = QLabel(self)
        logoPic = QPixmap("../ICO/logo.webp")
        scaredLogoPic = logoPic.scaled(100,100)
        loginLogo.setPixmap(scaredLogoPic)
        loginLogo.setAlignment(Qt.Qt.AlignCenter)           # 左侧logo在其widget内居中
        # 右侧表单
        formLayout = QFormLayout()                      # 右侧表单为表单布局
        loginUsername = QLabel('用户名:')
        loginUsername.setFont(QFont("Microsoft YaHei"))
        loginUsernameEdit = QLineEdit()
        loginUsernameEdit.setFixedSize(270,38)          # 限制表单布局右侧文本框的大小

        loginPwd = QLabel('密码:')
        loginPwd.setFont(QFont("Microsoft YaHei"))
        loginPwdEdit = QLineEdit()
        loginPwdEdit.setEchoMode(QLineEdit.Password)        # 设置文本框输入模式为暗文
        loginPwdEdit.setFixedSize(270,38)

        loginbtn = QPushButton('登录')
        loginbtn.setFixedSize(270,40)
        loginbtn.setFont(QFont('Microsoft YaHei'))
        loginbtn.setObjectName("loginbtn")
        loginbtn.setStyleSheet("#loginbtn{"
                               "background-color:#2c7adf;color:#fff;border:none;border-radius:4px;}")        # 按钮样式
        formLayout.addRow(loginUsername,loginUsernameEdit)
        formLayout.addRow(loginPwd,loginPwdEdit)
        formLayout.addWidget(loginbtn)
        hbox.setAlignment(Qt.Qt.AlignCenter)
        # 调整间距
        formLayout.setHorizontalSpacing(20)
        formLayout.setVerticalSpacing(12)

        hbox.addLayout(formLayout,2)                # 登录右侧表单水平布局
        login.setLayout(hbox)                       # 整体登录表单
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