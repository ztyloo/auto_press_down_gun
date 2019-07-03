# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_project\auto_press_down_gun\auto_position_label\start_label__.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from auto_position_label.image_qlabel import Image_QLabel
from auto_position_label.crop_position import screen_position


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(3440, 1350)
        Dialog.setMouseTracking(True)
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(10, 1320, 111, 31))
        self.stopButton.setObjectName("stopButton")

        self.label = Image_QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 0, 3311, 1431))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setMouseTracking(True)
        self.label.setImage()
        self.label.res_rect_n_signal[int].connect(self.change_radio_button)

        self.radioButtons = list()
        for i, k in enumerate(screen_position):
            self.radioButtons.append(QtWidgets.QRadioButton(Dialog))
            self.radioButtons[i].setGeometry(QtCore.QRect(5, 80+20*i, 150, 16))
            self.radioButtons[i].setObjectName(k)
        self.change_radio_button(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.startButton.clicked.connect(self.label.openImage)

        for i, k in enumerate(screen_position):
            self.radioButtons[i].toggled.connect(self.change_res_rect_n)

        self.stopButton.clicked.connect(self.label.print_res)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Locate_rectangle"))
        self.startButton.setText(_translate("Dialog", "Choose image"))
        self.stopButton.setText(_translate("Dialog", "Print"))
        for i, k in enumerate(screen_position):
            self.radioButtons[i].setText(_translate("Dialog", k))

    def change_radio_button(self, n):
        self.radioButtons[n].setChecked(True)

    def change_res_rect_n(self):
        for i, k in enumerate(screen_position):
            if self.radioButtons[i].isChecked():
                self.label.res_rect_n = i


if __name__ == "__main__":
    # d = Deep_vs_Wide_Dict('x0')
    # d.d_dict = screen_position
    # d.d_to_w()
    # d.w_to_d()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

