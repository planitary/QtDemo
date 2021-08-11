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
        '''将滑块的valuechanged信号和lcd的display槽绑定
        sld的valuechanged发出信号，display槽接收发出的信号对值做出显示'''
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('信号槽')
        self.show()

    # 重写事件处理函数，用户点击键盘的esc，应用被终止
    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())