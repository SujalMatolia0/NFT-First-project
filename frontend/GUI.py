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
        self.setFixedSize(800, 600)
    
    
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
            checkbac = self.db_manager.isbankthere(Login.email)
            if checkbac:
                mainmenu = Mainmenu(self.db_manager, self.bg_img)
                widget.addWidget(mainmenu)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
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
        wallet = int(self.wallet.text())
        if not(cardno and cvv):
            QMessageBox.warning(None,"Error", "Please fill the bank details properly.")
            return
        if (len(cardno) != 16):
            QMessageBox.warning(None,"Error", "Please enter correct 16 digit code.")
            return
        if (len(cvv) != 3):
            QMessageBox.warning(None,"Error", "Please enter correct cvv code.")
            return
        if (wallet <= 0 or wallet >= 10000):
            QMessageBox.warning(None,"Error", "Please enter the wallet amount between 1 and 9999.")
            return
        success = self.db_manager.insert_bank(cardno, cvv, wallet, email = self.email)
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
        self.info.clicked.connect(self.buymenu)
        self.buyorsell.clicked.connect(self.sellmenu)
        self.exit.clicked.connect(QApplication.quit)
    def buymenu(self):
        buymenu = Buymenu(self.db_manager, self.bg_img)
        widget.addWidget(buymenu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def sellmenu(self):
        sellmenu = Sellmenu(db_manager, bg_img)
        widget.addWidget(sellmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
        
class Buymenu(QDialog):
    def __init__(self, db_manager, bg_img):
        super(Buymenu , self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('buymenu.ui', self)
        print(f"Children of Buymenu: {[child.objectName() for child in self.children()]}")
        self.db_manager = db_manager
        self.nftname = self.findChild(QtWidgets.QComboBox, 'nftname')
        nft_names = ""
        names = self.db_manager.nftnames_for_nftdetails(nft_names)
        for name in names:
            self.nftname.addItem(name[0])
        #self.nftname = name[0]
        self.buyquant.setMaximum(self.db_manager.maxquantity(name[0]))
        self.nftname.currentIndexChanged[int].connect(self.show_nft_details)
        self.backbutton.clicked.connect(self.gotoMainmenu)
        self.buybutton.clicked.connect(lambda: self.buynft(self.nftname.currentText()))
        
        initial_index = 0
        self.show_nft_details(initial_index)

            
    def gotoMainmenu(self):
        mainmenu = Mainmenu(db_manager, bg_img)
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def buynft(self, nftname):
        self.value = self.buyquant.value()
        nft_name = nftname
        reply = QMessageBox.question(self, 'Confirmation', f'Do you really want to buy NFT?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            total_cost, balance = self.db_manager.buynft(Login.email, nft_name, self.value)
            if (total_cost == 0 and balance == 0):
                QMessageBox.warning(self, "Warning", f"Insufficient balance")
            else:
                QMessageBox.information(self, "Success", f"NFT bought successfully \n Total cost: {total_cost} \n The left balance: {balance}")
            
    
    def show_nft_details(self, index): #PROBLEMATIC
        selected_nft = self.nftname.itemText(index)
        nftdetails = self.db_manager.show_nft_details(selected_nft)
        if nftdetails:
                self.nftdetails.setText(nftdetails[0])
                print("Nft details: ", nftdetails[0])
        else:
            self.nftdetails.setText("No details available for this NFT")
        original_quantity = self.db_manager.maxquantity(selected_nft)
        self.buyquant.setMaximum(original_quantity)
            
class Sellmenu(QDialog):
    def __init__(self, db_manager, bg_img):
        super(Sellmenu, self).__init__()
        self.bg_img = bg_img
        self.bg_img.setParent(self)
        loadUi('sellmenu.ui', self)
        self.nftquant.setMinimum(1)
        self.nftquant.setMaximum(99)
        self.nftquant.setValue(1)
        self.nftquant.valueChanged.connect(self.showresult)
        self.db_manager = db_manager
        self.value = 1
        self.backbutton.clicked.connect(self.gotoMainmenu)
        self.sellnft.clicked.connect(self.gotosell)
    def showresult(self):
            self.value = self.nftquant.value()
    def gotoMainmenu(self):
        mainmenu = Mainmenu(db_manager, bg_img)
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotosell(self):
        nftname = self.nftname.text()
        nftprice = self.nftprice.text()
        nftquant = self.value
        nftdesc = self.nftdescription.text()
        success  = self.db_manager.nft_for_sale(Login.email, nftname, nftprice, nftquant, nftdesc)
        if success:
            QMessageBox.information(None, "Success", "Your NFT showcased successfully.")
            mainmenu = Mainmenu(db_manager, bg_img)
            widget.addWidget(mainmenu)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else: 
            QMessageBox.warning(None, "Error", "Failed to showcased NFT. Please try again.")
        
app = QApplication(sys.argv)
bg_img = Mywidget()
db_manager= DBMS()
mainwindow = Sign_Up(db_manager, bg_img)
widget = QtWidgets.QStackedWidget()
widget_width = int(620 * 1.3)
widget_height = int(470 * 1.3)
widget.setFixedSize(widget_width, widget_height)
widget.setStyleSheet('background: transparent;')
widget.addWidget(mainwindow)
widget.show()