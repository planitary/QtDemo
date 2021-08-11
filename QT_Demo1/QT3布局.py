# coding=gbk
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()                        # 定义水平箱布局
        hbox.addStretch(1)                          # 拉伸因子，在两个组件中间添加空隙使得组件推到窗口的右边
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)                    # 将组件添加到布局中

        vbox = QVBoxLayout()                    # 定义垂直布局
        # vbox.addStretch(1)                              # 定义拉伸因子，将水平布局推到窗口底边
        vbox.addLayout(hbox)                # 将水平布局添加到垂直布局中

        self.setLayout(vbox)                # 窗口主布局

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())