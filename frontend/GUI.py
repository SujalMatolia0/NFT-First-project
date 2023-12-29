import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QDialogButtonBox
from PyQt5.uic import loadUi
from db_manager import DBMS
from bg_img import Mywidget



class Sign_Up(QDialog):
   
    def __init__(self, db_manager, bg_img):
        super(Sign_Up,self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('signup.ui', self)
        self.db_manager = db_manager
        self.signupbutton.clicked.connect(self.signupstatus)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton.clicked.connect(self.gotologin)
    
    def gotologin(self):
        login = Login(self.db_manager, self.bg_img)
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
            login = Login(self.db_manager, self.bg_img)
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1) 
        else:
            QMessageBox.warning(None, "Error", "Registration was unsuccessfull. \n Please try again later.")

class Login(QDialog):
    def __init__(self, db_manager, bg_img):
        super(Login,self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('login.ui', self)
        self.Login.clicked.connect(self.Loggedinstatus)
        self.Loginpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_manager = db_manager
        
    def Loggedinstatus(self):
        Login.email = self.Loginemail.text()
        passwd = self.Loginpass.text()
        if not(Login.email and passwd):
            QMessageBox.warning(None, "Error", "Please enter both email and password.")
            return
        if self.db_manager.fetch_user(Login.email, passwd):
            QMessageBox.information(None, "Success", "Logged in successfully.")
            bankauth = Bankdetails(self.db_manager, self.bg_img)
            widget.addWidget(bankauth)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            QMessageBox.warning(None, "Error", "Incorrect email or password.")
            return
        
class Bankdetails(QDialog):
    def __init__(self, db_manager, bg_img):
        super(Bankdetails, self).__init__()
        self.email = Login.email
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('bankdetails.ui', self)
        self.db_manager = db_manager
        self.addbank.clicked.connect(self.bankauth)
        
    def bankauth(self):
        cardno = self.creditcardno.text()
        cvv = self.cvv.text()
        if not(cardno and cvv):
            QMessageBox.warning(None,"Error", "Please fill the bank details properly.")
            return
        if (len(cardno) != 16):
            QMessageBox.warning(None,"Error", "Please enter correct 16 digit code.")
            return
        if (len(cvv) != 3):
            QMessageBox.warning(None,"Error", "Please enter correct cvv code.")
            return
        success = self.db_manager.insert_bank(cardno, cvv, email = self.email)
        if success:
            QMessageBox.information(None, "Success", "Bank account added successfully.")
            mainmenu = Mainmenu(self.db_manager, self.bg_img)
            widget.addWidget(mainmenu)
            widget.setCurrentIndex(widget.currentIndex() + 1)  
        else:
            QMessageBox.warning(None, "Error", "Something went wrong.")

class Mainmenu(QDialog):
    def __init__(self, db_manager, bg_img):
        super(Mainmenu, self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('Main menu.ui', self)
        
        self.db_manager = db_manager
        self.info.clicked.connect(self.infomenu)
        self.buyorsell.clicked.connect(self.buyorsellmenu)
        self.exit.clicked.connect(QApplication.quit)
    def infomenu(self):
        info_menu = infomenu(self.db_manager, self.bg_img)
        widget.addWidget(info_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def buyorsellmenu(self):
        buyorsellmenu = buyorsell(db_manager, bg_img)
        widget.addWidget(buyorsellmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
        
class infomenu(QDialog):
    def __init__(self, db_manager, bg_img):
        super(infomenu , self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('infomenu.ui', self)
        self.db_manager = db_manager
        nft_names = ""
        names = self.db_manager.nftnames_for_nftdetails(nft_names)
        for name in names:
            self.nftname.addItem(name[0])
        self.nftname.currentIndexChanged[int].connect(self.show_nft_details)
        self.backbutton.clicked.connect(self.gotoMainmenu)
        self.buybutton.clicked.connect(self.gotoBuymenu)
            
    def gotoMainmenu(self):
        mainmenu = Mainmenu(db_manager, bg_img)
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def gotoBuymenu(self):
        mainmenu = buyorsell(db_manager, bg_img)
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def show_nft_details(self, index): #PROBLEMATIC
        selected_nft = self.nftname.itemText(index)
        nftdetails = self.db_manager.show_nft_details(selected_nft)
        if nftdetails:
                self.nftdetails.setText(nftdetails[0])
                print("Nft details: ", nftdetails[0])
        else:
            self.nftdetails.setText("No details available for this NFT")
            
class buyorsell(QDialog):
    def __init__(self, db_manager, bg_img):
        super(buyorsell, self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('buysell.ui', self)
        self.db_manager = db_manager
        nft_names = ""
        names = self.db_manager.nftnames_for_nftdetails(nft_names)
        for name in names:
            self.nftname.addItem(name[0])
        self.backbutton.clicked.connect(self.gotoMainmenu)
        self.quantity.valueChanged.connect(self.showresult)
        self.buybutton.clicked.connect(self.gotoBuy)
        self.sellbutton.clicked.connect(self.gotosell)
            
    def gotoMainmenu(self):
        mainmenu = Mainmenu(db_manager, bg_img)
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoBuy(self):
        value = self.quantity.value()
        if value == 0:
            QMessageBox.warning(None, "Error", "The value of NFT should be greater than 0")
        else:
            reply = QMessageBox.question(self, 'Confirmation', f'Do you really want to buy {value} NFT?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                QMessageBox.information(None, "Success", "NFT bought successfully.")
    def gotosell(self):
        value = self.quantity.value()
        if value == 0:
            QMessageBox.warning(None, "Error", "The value of NFT should be greater than 0")
        else:
            reply = QMessageBox.question(self, 'Confirmation', f'Do you really want to Sell {value} NFT?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                QMessageBox.information(None, "Success", "NFT sold successfully.")
            else: 
                    QMessageBox.warning(None, "Error", "Failed to sell NFT. Please try again.")


    def showresult(self):
        global value
        value = self.quantity.value()
           
app = QApplication(sys.argv)
bg_img = Mywidget()
db_manager= DBMS()
mainwindow = Sign_Up(db_manager, bg_img)
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()