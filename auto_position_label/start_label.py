# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_project\auto_press_down_gun\auto_position_label\start_label__.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from auto_position_label.q_control import Image_QLabel
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

        dvw_dict = Deep_vs_Wide_Dict('x0')
        dvw_dict.d_dict = screen_position
        dvw_dict.d_to_w()
        self.w_dict = dvw_dict.w_dict

        self.radioButtons = list()
        for i, k in enumerate(self.w_dict):
            self.radioButtons.append(QtWidgets.QRadioButton(Dialog))
            self.radioButtons[i].setGeometry(QtCore.QRect(5, 80+20*i, 150, 16))
            self.radioButtons[i].setObjectName(k)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.startButton.clicked.connect(self.label.openImage)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Locate_rectangle"))
        self.startButton.setText(_translate("Dialog", "Choose image"))
        self.stopButton.setText(_translate("Dialog", "Done"))
        for i, k in enumerate(self.w_dict):
            self.radioButtons[i].setText(_translate("Dialog", k))


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

