import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.uic import loadUi

class Sign_Up(QDialog):
   
    def __init__(self):
        super(Sign_Up,self).__init__()
        loadUi('D:/PROJECT WITH SUJAL/NFT-First-project-main/frontend/SIGNUP FORM.ui', self)
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
        print("THe {} {} has entered the chat".format(fname, lname))
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1) 


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi('D:/PROJECT WITH SUJAL/NFT-First-project-main/frontend/LGG In FORM.ui', self)
        self.Login.clicked.connect(self.Loggedinstatus)
        self.Loginpass.setEchoMode(QtWidgets.QLineEdit.Password)
    def Loggedinstatus(self):
        email = self.Loginemail.text()
        passwd = self.Loginpass.text()
        print("THe {} {} has entered the chat".format(email, passwd))
    
app = QApplication(sys.argv)
mainwindow = Sign_Up()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedSize(800,605)
widget.show()
app.exec_()