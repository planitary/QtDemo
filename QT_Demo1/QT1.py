# coding=gbk
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox,QTextEdit
from PyQt5.QtGui import QIcon,QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('����һ������<b>QPushButton</b>')
        btn = QPushButton('Quit',self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('����һ����ť<b>QPushButton</b>')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setWindowTitle('Welcome')
        self.setWindowIcon(QIcon('../ICO/����.png'))
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'��ʾ',"���Ҫ�˳�ô?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())