# coding=gbk

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp,QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        # 添加菜单下功能项
        exitAction = QAction(QIcon('../ICO/关闭.png'),'&退出',self)         # 为子功能指定显示的文本和图标
        exitAction.setShortcut('ctrl+Q')                        # 为子功能绑定快捷键
        exitAction.setStatusTip('退出')                       # 为子功能添加鼠标悬浮tips
        exitAction.triggered.connect(qApp.quit)                 # 子功能添加触发动作
        self.statusBar()
        # 添加菜单（整体窗口中的menubar）
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&文件')                   # 指定菜单标题
        fileMenu.addAction(exitAction)                          # 将子功能绑定到菜单上
        # 添加工具栏(toolbar)
        toolbar = self.addToolBar('退出')                # 指定该工具的标题
        toolbar.addAction(exitAction)                      # 将子功能绑定到工具栏
        videoAction = QAction(QIcon('../ICO/视频.png'),'&视频',self)
        videoAction.setStatusTip('视频')
        toolbar.addAction(videoAction)


        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Welcome')
        self.setWindowIcon(QIcon('../ICO/咖啡.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())