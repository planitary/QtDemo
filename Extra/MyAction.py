# coding:gbk
from PyQt5 import QtWidgets, QtCore

"""QLabel����û��clicked()�źţ���Ҫ���ж��壬
�鿴QLabel���֪�䶨�����¼�����û�о���д�¼������ݣ���PyQt5֧���Զ����źţ�
��˿�ͨ����дQLabel���¼������������Զ�����źţ��Դ˴ﵽ��QLabel����¼���Ŀ"""


# ��дQlabel���壬�̳���Qlabel�����Qlabel�¼���Ӧ
class MyActionLabel(QtWidgets.QLabel):
    buttonClicked = QtCore.pyqtSignal()

    def __init__(self, *__args):
        super(MyActionLabel, self).__init__(*__args)

    def mouseReleaseEvent(self, QMouseEvent) -> None:
        self.buttonClicked.emit()

    # ���Ӳۺ���
    def connectSlot(self, func):
        self.buttonClicked.connect(func)


"""��дQPlainText��focusOutEcent���������ı���ʧȥ����ʱ�����¼�"""
class MyActionLineEdit(QtWidgets.QPlainTextEdit):
    textFocusedOut = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(MyActionLineEdit, self).__init__(parent)

    def focusOutEvent(self, et) -> None:
        self.textFocusedOut.emit()

    # �󶨲ۺ���
    def connetSlot(self, func):
        self.textFocusedOut.connect(func)
