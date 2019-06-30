# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_project\auto_press_down_gun\auto_position_label\start_label.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from auto_position_label.image_qlabel import Image_QLabel


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(3440, 1370)
        Dialog.setMouseTracking(True)

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(10, 90, 89, 16))
        self.radioButton.setObjectName("radioButton")

        self.label = Image_QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 3311, 1421))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setMouseTracking(True)

        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(10, 10, 111, 51))
        self.startButton.setObjectName("pushButton")
        self.endButten = QtWidgets.QPushButton(Dialog)
        self.endButten.setEnabled(True)
        self.endButten.setGeometry(QtCore.QRect(10, 1380, 111, 51))
        self.endButten.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.startButton.clicked.connect(self.label.setImage)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Locate_rectangle"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.startButton.setText(_translate("Dialog", "Start"))
        self.endButten.setText(_translate("Dialog", "finish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

