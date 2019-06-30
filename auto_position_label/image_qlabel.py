from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import cv2
import sys


class Image_QLabel(QtWidgets.QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    _pressed = False
    corner_points = [(150, 150, 200, 200)]

    def mousePressEvent(self, event):
        self._pressed = True
        self.x0 = event.x()
        self.y0 = event.y()

    def mouseReleaseEvent(self, event):
        self._pressed = False

    def mouseMoveEvent(self, event):
        if self._pressed:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect =QtCore.QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.red,2,QtCore.Qt.SolidLine))
        painter.drawRect(rect)
        painter.drawEllipse(150,150,100,100)

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png)") # Ask for file
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
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

        # height, width, bytesPerComponent = img.shape
        # bytesPerLine = 3 * width
        # cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        # QImg = QtGui.QImage(img.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888)
        # pixmap = QtGui.QPixmap.fromImage(QImg)
        # self.label.setPixmap(pixmap)
        # self.label.setCursor(QtCore.Qt.CrossCursor)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = Example()
    sys.exit(app.exec_())
