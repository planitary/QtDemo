# coding=gbk
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        '''�������valuechanged�źź�lcd��display�۰�
        sld��valuechanged�����źţ�display�۽��շ������źŶ�ֵ������ʾ'''
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('�źŲ�')
        self.show()

    # ��д�¼����������û�������̵�esc��Ӧ�ñ���ֹ
    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())