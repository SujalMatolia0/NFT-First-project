import sys
import mysql.connector as sql
con = sql.connect(host = "localhost",user = 'root',passwd = 'pass',database = 'nft_project')
c1 = con.cursor()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from Signup_and_login import Sign_Up
from db_manager import DBMS


def main():
    app = QApplication(sys.argv)
    window = Sign_Up()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
