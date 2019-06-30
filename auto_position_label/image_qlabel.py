from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sys
import numpy as np
import cv2
from auto_position_label.find_image_corner import get_image_corner


class Image_QLabel(QtWidgets.QLabel):
    x, c_x, c_x0, c_x1 = 0, 0, 0, 0
    y, c_y, c_y0, c_y1 = 0, 0, 0, 0

    rect_n = 0
    left_up = True

    thr0, thr1 = 30, 300
    c_dist = 1000000000
    corner_br = 3

    corner_rects = [(0, 0, 0, 0)] * 3
    res_rects = [(0, 0, 0, 0)] * 3
    len = 0

    def mousePressEvent(self, event):
        if self.c_dist < self.thr0:
            self.rect_n += 1
            if self.rect_n == self.len:
                self.rect_n = 0
            if self.left_up:
                self.c_x0, self.c_y0 = self.c_x, self.c_y
                self.left_up = False
            else:
                self.c_x1, self.c_y1 = self.c_x, self.c_y
                self.left_up = True
                self.res_rects[self.rect_n] = (self.c_x0, self.c_y0, self.c_x1, self.c_y1)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        self.c_dist = 1000000000
        for a, b, c, d in self.corner_rects:
            temp_x, temp_y = (a, b) if self.left_up else (c, d)
            temp_dist = np.linalg.norm(np.array([self.x, self.y]) - np.array([temp_x, temp_y])) // 1*2
            if temp_dist < self.c_dist:
                self.c_dist = temp_dist
                self.c_x, self.c_y = temp_x, temp_y

        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        abcd_painter = QPainter(self)
        for a, b, c, d in self.corner_rects:
            abcd_painter.setPen(QPen(QtCore.Qt.red,self.corner_br,QtCore.Qt.SolidLine))
            abcd_painter.drawPoint(a, b)
            abcd_painter.setPen(QPen(QtCore.Qt.blue,self.corner_br,QtCore.Qt.SolidLine))
            abcd_painter.drawPoint(c, b)
            abcd_painter.setPen(QPen(QtCore.Qt.green,self.corner_br,QtCore.Qt.SolidLine))
            abcd_painter.drawPoint(c, d)
            abcd_painter.setPen(QPen(QtCore.Qt.yellow,self.corner_br,QtCore.Qt.SolidLine))
            abcd_painter.drawPoint(a, d)

        rect_painter = QPainter(self)
        for a, b, c, d in self.res_rects:
            rect =QtCore.QRect(a, b, c-a, d-b)
            rect_painter.setPen(QPen(QtCore.Qt.cyan,1,QtCore.Qt.SolidLine))
            rect_painter.drawRect(rect)

        circle_painter = QPainter(self)
        circle_painter.setPen(QPen(QtCore.Qt.transparent, 0))
        if self.thr0 < self.c_dist < self.thr1:
            circle_painter.setBrush(QColor(255, 255, 0, 50))
            circle_painter.drawEllipse(self.c_x-self.c_dist//2, self.c_y-self.c_dist//2, self.c_dist, self.c_dist)

        if self.c_dist < self.thr0:
            circle_painter.setBrush(QColor(0, 255, 0, 100))
            circle_painter.drawEllipse(self.c_x-self.thr0//2, self.c_y-self.thr0//2, self.thr0, self.thr0)

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png)") # Ask for file
        if fileName: # If the user gives a file
            img = cv2.imread(fileName)
            corner_rects = get_image_corner(img)
            self.corner_rects = corner_rects
            self.len = len(corner_rects)
            self.res_rects = [(0, 0, 0, 0)] * self.len

            pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
            # pixmap = pixmap.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.setPixmap(pixmap) # Set the pixmap onto the label
            self.setAlignment(QtCore.Qt.AlignLeading) # Align the label to center


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(3000, 1300)
        self.setWindowTitle('在label中绘制矩形')
        self.label = Image_QLabel(self)  #重定义的label
        self.label.setGeometry(QtCore.QRect(30, 30, 2000, 1000))

        self.label.setImage()

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = Example()
    sys.exit(app.exec_())
