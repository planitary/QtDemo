# coding=gbk

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon



class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('对话框', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)  # 按钮点击事件绑定到showDialog槽函数

        self.le = QLineEdit(self)
        self.le.setEnabled(False)  # 输入框禁用编辑，只用于展示
        self.le.move(130, 52)
        label = QLabel('welcome:', self)
        label.move(80, 55)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('输入对话框')
        self.show()

    # 槽函数，接受到按钮点击事件后弹出一个对话框用于输入
    def showDialog(self):
        # 显示一个输入对话框，第一个参数时标题，第二个为消息文本，返回一个bool值（自带两个按钮，一个ok，一个cancel）
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))


# 文件对话框
class Example2(QMainWindow,QWidget):

    def __init__(self):
        super(Example2, self).__init__()
        self.textEdit = QTextEdit()
        self.InitUI2()

    def InitUI2(self):
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openfile = QAction(QIcon('../ICO/咖啡.png'), 'Open', self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('打开新文件')
        openfile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(openfile)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('文件对话框')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, '选择文件', '/Users/admin/Desktop')
        if fname[0]:
            f = open(fname[0], 'r',encoding='utf-8')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Example()
    ex = Example2()
    sys.exit(app.exec_())
