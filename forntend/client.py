import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSizePolicy

class Mainmenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NFT Selling App')
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800,800)
        self.setStyleSheet("background-color: purple;")
        self.setupLayout()

    def setupLayout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.createHeader(main_layout)
        self.createContent(main_layout)

    def createHeader(self, layout):
        header_widget = QWidget()
        header_layout = QVBoxLayout()
        header_widget.setLayout(header_layout)

        header_widget.setStyleSheet("background-color: rgba(255, 255, 255, 0); ")
        header_widget.setMaximumHeight(80)

        header_label = QLabel('<strong>NFT ADDA</strong>', self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 34px; color: white; font-family: 'Comic Sans MS'; ")
        header_layout.addWidget(header_label)
        header_layout.addStretch()

        layout.addWidget(header_widget)

    def createContent(self, layout):
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_widget.setLayout(content_layout)

        content_widget.setStyleSheet("background-color: rgb(50, 50, 50); ")

        label_container = QWidget()
        label_container.setStyleSheet("background-color: rgb(50, 50, 50); ")  
        label_layout = QVBoxLayout(label_container)
        label_layout.setContentsMargins(200, 200, 200, 200)  

        label = QLabel('<strong>WELCOME TO NFT ADDA !!</strong><br>'
                       '<strong>The Art awaits you</strong>', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: white;")

        label_layout.addWidget(label)

        button_layout = QHBoxLayout() 
        button1 = QPushButton('SIGN UP')
        button2 = QPushButton('LOG IN')
        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        
        button1.setStyleSheet(
            "QPushButton { background-color: #336699; color: white; border-radius: 20px; padding: 10px 20px; font-size: 18px; }"
            "QPushButton:hover { background-color: #5588CC; }"
        )
        button2.setStyleSheet(
            "QPushButton { background-color: #336699; color: white; border-radius: 20px; padding: 10px 20px; font-size: 18px; }"
            "QPushButton:hover { background-color: #5588CC; }"
        )
        
        button1.setFixedSize(300, 50)
        button2.setFixedSize(300, 50)
        v_layout = QVBoxLayout(self)

        btn_up = QPushButton('button1', self)
        btn_down = QPushButton('button2', self)
        v_layout.addWidget(btn_up)
        v_layout.addWidget(btn_down)
        
        
        button_container = QWidget()
        button_container.setLayout(button_layout)
        label_layout.addWidget(button_container)

        content_layout.addWidget(label_container, alignment=Qt.AlignTop)

        layout.addWidget(content_widget)

def main():
    app = QApplication(sys.argv)
    window = Mainmenu()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
