from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)


class My_Dialog(QtWidgets.QDialog):
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        pass


class Ui_Dialog(QThread):
    def __init__(self, app):
        super().__init__()
        self.dialog = My_Dialog()
        self.app = app

    def setupUi(self, text):
        self.text = text

        self.dialog.setObjectName("Dialog")
        self.dialog.resize(200, 100)
        self.dialog.move(50, 1300)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.dialog.setFont(font)
        self.dialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.label = QtWidgets.QLabel(self.dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 100))
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", self.text))



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(app)
    ui.setupUi("555")
    Dialog.show()
    sys.exit(app.exec_())

