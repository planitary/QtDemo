from PyQt5 import QtWidgets,QtGui
import sys

class NoteText(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super (NoteText, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.matches(QtGui.QKeySequence.Paste):
            self.setText("Bye")

class Test(QtWidgets.QWidget):
  def __init__( self, parent=None):
      super(Test, self).__init__(parent)

      le = QtWidgets.QLineEdit()
      nt = NoteText(le)

      layout = QtWidgets.QHBoxLayout()
      layout.addWidget(nt)
      self.setLayout(layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWidget = Test()
    myWidget.show()
    app.exec_()