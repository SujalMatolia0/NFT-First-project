import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Mywidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("bg IMG")
        Bg_IMG = "NFT ADDA #!.png"
        pixmap = QPixmap(Bg_IMG)
        bg_label = QLabel(self)
        bg_label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(bg_label)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        bg_label.setScaledContents(True)
        self.setStyleSheet('background: transparent;')
        widget_width = int(self.width() * 1.3)
        print(self.width())
        widget_height = int(self.height() * 1.3)
        print(self.height())
        self.setFixedSize(widget_width, widget_height)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mywidget()
    window.show()
    sys.exit(app.exec_())