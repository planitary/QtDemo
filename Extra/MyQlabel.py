# coding:gbk
from PyQt5 import QtWidgets, QtCore

"""QLabel����û��clicked()�źţ���Ҫ���ж��壬
�鿴QLabel���֪�䶨�����¼�����û�о���д�¼������ݣ���PyQt5֧���Զ����źţ�
��˿�ͨ����дQLabel���¼������������Զ�����źţ��Դ˴ﵽ��QLabel����¼���Ŀ"""

# ��дQlabel���壬�̳���Qlabel�����Qlabel�¼���Ӧ
class MyQLabel(QtWidgets.QLabel):
    buttonClicked = QtCore.pyqtSignal()

    def __init__(self,*__args):
        super(MyQLabel, self).__init__(*__args)

    def mouseReleaseEvent(self, QMouseEvent) -> None:
        self.buttonClicked.emit()

    # ���Ӳۺ���
    def connectSlot(self,func):
        self.buttonClicked.connect(func)