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
        # ��Ӳ˵��¹�����
        exitAction = QAction(QIcon('../ICO/�ر�.png'),'&�˳�',self)         # Ϊ�ӹ���ָ����ʾ���ı���ͼ��
        exitAction.setShortcut('ctrl+Q')                        # Ϊ�ӹ��ܰ󶨿�ݼ�
        exitAction.setStatusTip('�˳�')                       # Ϊ�ӹ�������������tips
        exitAction.triggered.connect(qApp.quit)                 # �ӹ�����Ӵ�������
        self.statusBar()
        # ��Ӳ˵������崰���е�menubar��
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&�ļ�')                   # ָ���˵�����
        fileMenu.addAction(exitAction)                          # ���ӹ��ܰ󶨵��˵���
        # ��ӹ�����(toolbar)
        toolbar = self.addToolBar('�˳�')                # ָ���ù��ߵı���
        toolbar.addAction(exitAction)                      # ���ӹ��ܰ󶨵�������
        videoAction = QAction(QIcon('../ICO/��Ƶ.png'),'&��Ƶ',self)
        videoAction.setStatusTip('��Ƶ')
        toolbar.addAction(videoAction)


        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Welcome')
        self.setWindowIcon(QIcon('../ICO/����.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())