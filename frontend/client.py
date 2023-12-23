import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from menu import Mainmenu


def main():
    app = QApplication(sys.argv)
    window = Mainmenu()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
