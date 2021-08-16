# coding:gbk
from PyQt5 import QtWidgets, QtCore

"""QLabel对象没有clicked()信号，需要自行定义，
查看QLabel类可知其定义了事件，但没有具体写事件的内容，而PyQt5支持自定义信号，
因此可通过重写QLabel的事件函数，连接自定义的信号，以此达到给QLabel添加事件的目"""


# 重写Qlabel定义，继承自Qlabel，添加Qlabel事件响应
class MyActionLabel(QtWidgets.QLabel):
    buttonClicked = QtCore.pyqtSignal()

    def __init__(self, *__args):
        super(MyActionLabel, self).__init__(*__args)

    def mouseReleaseEvent(self, QMouseEvent) -> None:
        self.buttonClicked.emit()

    # 链接槽函数
    def connectSlot(self, func):
        self.buttonClicked.connect(func)


"""重写QPlainText的focusOutEcent方法，在文本框失去焦点时触发事件"""
class MyActionLineEdit(QtWidgets.QPlainTextEdit):
    textFocusedOut = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(MyActionLineEdit, self).__init__(parent)

    def focusOutEvent(self, et) -> None:
        self.textFocusedOut.emit()

    # 绑定槽函数
    def connetSlot(self, func):
        self.textFocusedOut.connect(func)
