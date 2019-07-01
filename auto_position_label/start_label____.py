# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_project\auto_press_down_gun\auto_position_label\start_label.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from auto_position_label.image_qlabel import Image_QLabel
from auto_position_label.crop_position import screen_position


class Deep_vs_Wide_Dict:
    def __init__(self, stop_key_sign, escape_c='-'):
        self.stop_key_sign = stop_key_sign
        self.escape_c = escape_c

        self.w_dict = dict()
        self.d_dict = dict()
        self.mid_dict = dict()

    def is_leaf(self, diction):
        if self.stop_key_sign in diction:
            return True
        return False

    def d_to_w(self):
        self.encode_dict(self.d_dict)
        return self.w_dict

    def encode_dict(self, dic, path_str=""):
        if self.is_leaf(dic):
            self.w_dict[path_str[1:]] = dic
            return
        for k in dic:
            self.encode_dict(dic[k], path_str + self.escape_c + k)

    def w_to_d(self):
        for k, v in self.w_dict.items():
            path_sep = k.split(self.escape_c)
            temp_dict = self.mid_dict
            for path in path_sep:
                if not path in temp_dict:
                    temp_dict[path] = dict()
                temp_dict = temp_dict[path]
            temp_dict[path_sep[-1]] = v


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(3440, 1370)
        Dialog.setMouseTracking(True)

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 80, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 120, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 160, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")

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
    d = Deep_vs_Wide_Dict('x0')
    d.d_dict = screen_position
    d.d_to_w()
    d.w_to_d()

    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())

