from PyQt5 import QtCore, QtGui, QtWidgets
from auto_position_label.screen_capture_listener import Key_Listener


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 50)
        Dialog.move(50, 1300)
        Dialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        Dialog.setFont(font)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.label.setObjectName("label")

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.listener = Key_Listener()
        self.listener.temp_qobject.state_str_signal[str].connect(self.retranslateUi)
        self.listener.init_show()
        self.listener.start()

    def retranslateUi(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", text))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
