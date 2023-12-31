import sys
import mysql.connector as sql

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from GUI import Sign_Up
from bg_img import Mywidget
from db_manager import DBMS

def main():
    app = QApplication(sys.argv)
    db_manager = DBMS()
    bg_img = Mywidget()
    window = Sign_Up(db_manager, bg_img)    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
