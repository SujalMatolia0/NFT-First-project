import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout

class Mainmenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NFT Selling App')
        self.setGeometry(100, 100, 800, 600)
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

        header_widget.setStyleSheet("background-color: black; ")
        header_widget.setMaximumHeight(80)

        header_label = QLabel('<strong>NFT ADDA</strong>', self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 34px; color: white;")

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
                       '<strong>HERE YOU WILL FIND MOST FAMOUS AND MOST SUITABLE NFT FOR YOU...</strong>', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: white;")

        label_layout.addWidget(label)

        button_layout = QHBoxLayout()
        button1 = QPushButton('TO KNOW INFORMATION ABOUT NFT\'s')
        button2 = QPushButton('TO BUY, SELL or KNOW PRICE OF NFT\'s')

        button1.setStyleSheet(
            "QPushButton { background-color: #336699; color: white; border-radius: 20px; padding: 10px 20px; font-size: 18px; }"
            "QPushButton:hover { background-color: #5588CC; }"
        )
        button2.setStyleSheet(
            "QPushButton { background-color: #336699; color: white; border-radius: 20px; padding: 10px 20px; font-size: 18px; }"
            "QPushButton:hover { background-color: #5588CC; }"
        )

        button1.setFixedSize(500, 50)
        button2.setFixedSize(500, 50)

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        button_container = QWidget()
        button_container.setLayout(button_layout)
        label_layout.addWidget(button_container)

        content_layout.addWidget(label_container, alignment=Qt.AlignTop)

        layout.addWidget(content_widget)


