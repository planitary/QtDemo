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

        hbox = QHBoxLayout()                        # ����ˮƽ�䲼��
        hbox.addStretch(1)                          # �������ӣ�����������м���ӿ�϶ʹ������Ƶ����ڵ��ұ�
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)                    # �������ӵ�������

        vbox = QVBoxLayout()                    # ���崹ֱ����
        # vbox.addStretch(1)                              # �����������ӣ���ˮƽ�����Ƶ����ڵױ�
        vbox.addLayout(hbox)                # ��ˮƽ������ӵ���ֱ������

        self.setLayout(vbox)                # ����������

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())