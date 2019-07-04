import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from auto_position_label.screen_capture_listener import Key_Listener


# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.listener = Key_Listener()
#         self.listener.temp_qobject.state_str_signal[str].connect(self.change_text)
#         self.initUI()
#
#     def initUI(self):
#         font = QtGui.QFont()
#         font.setFamily("Arial")
#         font.setPointSize(14)
#         self.setFont(font)
#         self.setGeometry(50, 1300, 200, 50)
#         # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
#         # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#
#         self.label = QtWidgets.QLabel()
#         self.label.setGeometry(QtCore.QRect(0, 0, 200, 50))
#         self.label.setObjectName("label")
#
#         self.retranslateUi()
#         self.show()
#
#     def change_text(self, text):
#         self.label.setText("TextLabel")
#
#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.label.setText(_translate("Dialog", "TextLabel"))
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets

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
