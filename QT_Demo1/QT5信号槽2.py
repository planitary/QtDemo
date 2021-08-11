# coding=gbk
import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication
from PyQt5.QtCore import pyqtSignal,QObject


'''QT的信号槽机制，某个动作触发后会发射一个信号，例如鼠标点击，按钮点击，这些动作发射的信号会被对应的目标（槽）来接收
槽接受到信号后会根据槽内的逻辑实现不同的响应方式，例如关闭窗口、发送信息等
#####举个例子：有一个按钮，点击之后弹出注册界面
这里的按钮就是一个事件的载体，按钮点击是一个事件，当点击按钮后，发送一个按钮点击的事件，该事件绑定到一个注册函数中（槽函数）
该函数接受到事件后，内部逻辑会打开一个注册界面'''

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button1',self)
        btn1.move(30,50)

        btn2 = QPushButton('Button2',self)
        btn2.move(150,50)
        # 两个按钮绑定到同一个槽函数中
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        # 设置状态栏，显示文本
        self.statusBar()

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Event sender')
        self.show()

    # 槽函数，用于接受按钮点击事件，槽函数的sender方法用于显示哪个按钮被按下（接受到按钮点击信号）
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
'''从QObject类生成的独对象可以发送自定义信号，这里自定义一个信号：closeApp,当触发鼠标点击时，信号被发射，接收方为QMainWindow，
调用了close()方法来关闭窗口'''
class Communicate(QObject):
    closeApp = pyqtSignal()

class Example2(QMainWindow):

    def __init__(self):
        super(Example2, self).__init__()
        self.initUI2()

    def initUI2(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('关闭信号')
        self.show()

    def mousePressEvent(self, event) -> None:
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # ex = Example2()
    sys.exit(app.exec_())