from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPixmap
import sys
import numpy as np
import cv2
from auto_position_label.find_image_corner import get_image_corner


class Image_QLabel(QtWidgets.QLabel):
    x, c_x, c_x0, c_x1 = 0, 0, 0, 0
    y, c_y, c_y0, c_y1 = 0, 0, 0, 0

    rect_n = 0
    before_choose_one = True
    shift_mode = False

    corner_rects = [(0, 0, 0, 0)] * 3
    res_rects = [(0, 0, 0, 0)] * 3
    len = 0
    c_dist = 1000000000
    corner_br = 3
    circle_thr0, circle_thr1 = 17, 100


    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.c_dist < self.circle_thr0:
                if self.before_choose_one:
                    self.rect_n += 1
                    if self.rect_n == self.len:
                        self.rect_n = 0
                    self.c_x0, self.c_y0 = self.c_x, self.c_y
                    self.before_choose_one = False
                else:
                    self.c_x1, self.c_y1 = self.c_x, self.c_y
                    self.before_choose_one = True
                    self.res_rects[self.rect_n] = (self.c_x0, self.c_y0, self.c_x1, self.c_y1)
        if event.buttons() == Qt.RightButton:
            self.before_choose_one = True

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        self.c_dist = 1000000000
        for a, b, c, d in self.corner_rects:
            temp_x, temp_y = (a, b) if self.before_choose_one else (c, d)
            temp_dist = np.linalg.norm(np.array([self.x, self.y]) - np.array([temp_x, temp_y])) // 1*2
            if temp_dist < self.c_dist:
                self.c_dist = temp_dist
                self.c_x, self.c_y = temp_x, temp_y

        self.update()

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png)") # Ask for file
        if fileName: # If the user gives a file
            img = cv2.imread(fileName)
            corner_rects = get_image_corner(img)
            self.corner_rects = corner_rects
            self.len = len(corner_rects)
            self.res_rects = [(0, 0, 0, 0)] * self.len

            pixmap = QPixmap(fileName)  # Setup pixmap with the provided image
            # pixmap = pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio) # Scale pixmap
            self.setPixmap(pixmap) # Set the pixmap onto the label
            self.setAlignment(Qt.AlignLeading) # Align the label to center

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)

        if not self.before_choose_one:
            self.draw_rect(qp, (self.c_x0, self.c_y0, self.c_x, self.c_y), (0,255,255))
        for rect in self.corner_rects:
            self.draw_rect_corner(qp, rect)
        for rect in self.res_rects:
            self.draw_rect(qp, rect, (0,255,0))
            self.draw_coordinate(qp, (rect[0], rect[1]), (rect[0], rect[1]), (255, 0, 255))
            self.draw_coordinate(qp, (rect[2], rect[3]), (rect[2], rect[3]), (255, 0, 255))

        if self.circle_thr1 < self.c_dist:
            self.draw_cross(qp, (self.x, self.y))
            self.draw_coordinate(qp, (self.x, self.y), (self.x, self.y), (255, 0, 255))
        if self.circle_thr0 < self.c_dist < self.circle_thr1:
            self.draw_circle(qp, (self.c_x, self.c_y), self.c_dist, (255, 255, 0, 100))
            self.draw_cross(qp, (self.x, self.y))
            self.draw_coordinate(qp, (self.x, self.y), (self.x, self.y), (255, 0, 255))
        if self.c_dist < self.circle_thr0:
            self.draw_circle(qp, (self.c_x, self.c_y), self.circle_thr0, (0, 255, 0, 100))
            self.draw_cross(qp, (self.c_x, self.c_y))
            self.draw_coordinate(qp, (self.c_x, self.c_y), (self.c_x, self.c_y), (255, 0, 255))

    def draw_circle(self, qp, xy, r, color=(255, 0, 255, 100)):
        qp.setPen(QPen(Qt.transparent, 0))
        qp.setBrush(QColor(*color))
        qp.drawEllipse(QPoint(*xy), r, r)

    def draw_cross(self, qp, xy, color=(255, 0, 255, 100)):
        x, y = xy
        lenth = 1000
        pen = QPen(QColor(*color), 1, Qt.SolidLine)
        qp.setPen(pen)

        qp.drawLine(x-lenth, y, x+lenth, y)
        qp.drawLine(x, y-lenth, x, y+lenth)

    def draw_coordinate(self, qp, xy, xy_num, color=(255, 0, 255)):
        x, y = xy
        x_num, y_num = xy_num
        qp.setPen(QColor(*color))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(QRect(x-50, y-20, 100, 15), 10, '('+str(x_num)+','+str(y_num)+')')

    def draw_rect(self, qp, rect, color=(255, 0, 255)):
        x0, y0, x1, y1 = rect
        rect = QtCore.QRect(x0, y0, x1 - x0, y1 - y0)
        qp.setPen(QPen(QColor(*color), 1, Qt.SolidLine))
        qp.drawRect(rect)

    def draw_rect_corner(self, qp, rect):
        x0, y0, x1, y1 = rect
        qp.setPen(QPen(Qt.red, self.corner_br, Qt.SolidLine))
        qp.drawPoint(x0, y0)
        qp.setPen(QPen(Qt.blue, self.corner_br, Qt.SolidLine))
        qp.drawPoint(x1, y0)
        qp.setPen(QPen(Qt.green, self.corner_br, Qt.SolidLine))
        qp.drawPoint(x1, y1)
        qp.setPen(QPen(Qt.yellow, self.corner_br, Qt.SolidLine))
        qp.drawPoint(x0, y1)
