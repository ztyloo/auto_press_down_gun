import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from listener import All_Listener


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.listener = All_Listener()
        self.listener.state_str_signal[str].connect(self.change_text)
        self.initUI()

    def initUI(self):

        self.setGeometry(50, 1300, 200, 50)
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.label.setObjectName("label")
        self.label.setText("TextLabel")
        self.show()

    def change_text(self, text):
        self.label.setText("TextLabel")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
