# coding=gbk

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon



class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('�Ի���', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)  # ��ť����¼��󶨵�showDialog�ۺ���

        self.le = QLineEdit(self)
        self.le.setEnabled(False)  # �������ñ༭��ֻ����չʾ
        self.le.move(130, 52)
        label = QLabel('welcome:', self)
        label.move(80, 55)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('����Ի���')
        self.show()

    # �ۺ��������ܵ���ť����¼��󵯳�һ���Ի�����������
    def showDialog(self):
        # ��ʾһ������Ի��򣬵�һ������ʱ���⣬�ڶ���Ϊ��Ϣ�ı�������һ��boolֵ���Դ�������ť��һ��ok��һ��cancel��
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))


# �ļ��Ի���
class Example2(QMainWindow,QWidget):

    def __init__(self):
        super(Example2, self).__init__()
        self.textEdit = QTextEdit()
        self.InitUI2()

    def InitUI2(self):
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openfile = QAction(QIcon('../ICO/����.png'), 'Open', self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('�����ļ�')
        openfile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&�ļ�')
        fileMenu.addAction(openfile)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('�ļ��Ի���')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'ѡ���ļ�', '/Users/admin/Desktop')
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
