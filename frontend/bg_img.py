import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Mywidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0,0,800,600)
        self.setWindowTitle("bg IMG")
        Bg_IMG = "NFT ADDA #!.png"
        pixmap = QPixmap(Bg_IMG)
        bg_label = QLabel(self)
        bg_label.setPixmap(pixmap)
        bg_label.setGeometry(0, 0, self.width(), self.height())
        bg_label.setScaledContents(True)
        self.setStyleSheet('background: transparent;')
        self.setFixedSize(800, 600)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mywidget()
    window.show()
    sys.exit(app.exec_())