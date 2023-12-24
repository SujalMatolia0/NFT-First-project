import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from Signup_and_login import Sign_Up


def main():
    app = QApplication(sys.argv)
    window = Sign_Up()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
