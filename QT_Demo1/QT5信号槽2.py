# coding=gbk
import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication
from PyQt5.QtCore import pyqtSignal,QObject


'''QT���źŲۻ��ƣ�ĳ������������ᷢ��һ���źţ��������������ť�������Щ����������źŻᱻ��Ӧ��Ŀ�꣨�ۣ�������
�۽��ܵ��źź����ݲ��ڵ��߼�ʵ�ֲ�ͬ����Ӧ��ʽ������رմ��ڡ�������Ϣ��
#####�ٸ����ӣ���һ����ť�����֮�󵯳�ע�����
����İ�ť����һ���¼������壬��ť�����һ���¼����������ť�󣬷���һ����ť������¼������¼��󶨵�һ��ע�ắ���У��ۺ�����
�ú������ܵ��¼����ڲ��߼����һ��ע�����'''

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button1',self)
        btn1.move(30,50)

        btn2 = QPushButton('Button2',self)
        btn2.move(150,50)
        # ������ť�󶨵�ͬһ���ۺ�����
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        # ����״̬������ʾ�ı�
        self.statusBar()

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Event sender')
        self.show()

    # �ۺ��������ڽ��ܰ�ť����¼����ۺ�����sender����������ʾ�ĸ���ť�����£����ܵ���ť����źţ�
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
'''��QObject�����ɵĶ�������Է����Զ����źţ������Զ���һ���źţ�closeApp,�����������ʱ���źű����䣬���շ�ΪQMainWindow��
������close()�������رմ���'''
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
        self.setWindowTitle('�ر��ź�')
        self.show()

    def mousePressEvent(self, event) -> None:
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # ex = Example2()
    sys.exit(app.exec_())