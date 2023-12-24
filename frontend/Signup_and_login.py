import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
from db_manager import DBMS

class Sign_Up(QDialog):
   
    def __init__(self, db_manager):
        super(Sign_Up,self).__init__()
        loadUi('D:/PROJECT WITH SUJAL/NFT-First-project-main/frontend/SIGNUP FORM.ui', self)
        
        self.db_manager = db_manager
        
        self.signupbutton.clicked.connect(self.signupstatus)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton.clicked.connect(self.gotologin)
    
    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)  
        
    def signupstatus(self):
        fname = self.fname.text()
        lname = self.lname.text()
        email = self.email.text()
        pswd = self.password.text()
        cpswd = self.conpass.text()
        
        if not(fname and lname and email and pswd and cpswd):
            QMessageBox.warning(None, "Error", "Please fill in all details.")
            return
        if (pswd != cpswd):
            QMessageBox.warning(None, "Error", "Passwords, do not matched.")
            return
        if '@' not in email:
            QMessageBox.warning(None, "Error", "Invalid email.")
            return  
        success = self.db_manager.insert_user(fname, lname, email, pswd)
        
        if success:
            QMessageBox.information(None, "Success", "Successfully Registered. \nPlease log in again.")
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1) 
        else:
            QMessageBox.warning(None, "Error", "Registration was unsuccessfull. \n Please try again later.")


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi('D:/PROJECT WITH SUJAL/NFT-First-project-main/frontend/LGG In FORM.ui', self)
        self.Login.clicked.connect(self.Loggedinstatus)
        self.Loginpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_manager = db_manager
    def Loggedinstatus(self):
        email = self.Loginemail.text()
        passwd = self.Loginpass.text()
        if not(email and passwd):
            QMessageBox.warning(None, "Error", "Please enter both email and password.")
            return
        if self.db_manager.fetch_user(email, passwd):
            QMessageBox.information(None, "Success", "Logged in successfully.")
            return
        else:
            QMessageBox.warning(None, "Error", "Incorrect email or password.")
            return
        
    
app = QApplication(sys.argv)
db_manager= DBMS()
mainwindow = Sign_Up(db_manager)
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedSize(800,605)
widget.show()
app.exec_()