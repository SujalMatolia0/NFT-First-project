import mysql.connector as sql

class DBMS:
    def __init__(self):
        self.con = sql.connect(host = "localhost",user = 'root',passwd = 'pass',database = 'nft_project')
        self.c1 = self.con.cursor()
    def insert_user(self, fname, lname, email, pswd):
        try:
            self.c1.execute( "INSERT INTO user_details(first_name, last_name, email, pass) VALUES (%s, %s, %s, %s)",
                (fname, lname, email, pswd))
            self.con.commit()
            return True
        except sql.Error as e:
            print(f"Error: {e}")
            return False

    def insert_bank(self, cardno, cvv, wallet, email):
        try:
            self.c1.execute("Update user_details set credit_card = %s, cvv = %s, BALANCE = %s where email = %s", (cardno, cvv, wallet, email))
            self.con.commit()
            return True
        except sql.Error as e:
            print("The error is: ", e)
            return False
    
    def isbankthere(self, email):
        try: 
            self.c1.execute("select email from user_details where credit_card is NOT NULL")
            emails = [row[0] for row in self.c1.fetchall()]
            if email in emails:
                return True
            else:
                return False
        except sql.Error as e:
            print(f"The error is: {e}")
    
    def fetch_user(self, email, pswd):
        try:
            self.c1.execute(f"SELECT email,pass from user_details WHERE email = %s AND pass = %s", (email, pswd))
            user = self.c1.fetchone()
            return user is not None
        except sql.Error as e:
            print(f"Error: {e}")
    
    def nft_for_sale(self, email, nftname, nftprice, nftquant, nftdesc):
        try:
            self.c1.execute("Insert into seller_details(email, nft_name, Price, quantity, describe_nft) values(%s, %s, %s, %s, %s)", (email, nftname, nftprice, nftquant, nftdesc))
            self.con.commit()
            return True
        except sql.Error as e:
             print(f"Error: {e}")
             return False
 
    def nftnames_for_nftdetails(self, nft_names):
        try:
            self.c1.execute("select nft_name from seller_details")
            nft_names = self.c1.fetchall()
            return nft_names
        except sql.Error as e:
            print(f"THe error is: {e}")
 
    def maxquantity(self, nft_name):
        try:
            self.c1.execute("select Quantity from seller_details where nft_name = %s", (nft_name, ))
            result = self.c1.fetchone()
            if result:
                return int(result[0])
            else:
                return 0 
        except sql.Error as e:
            print(f"The Error is: {e}")
    
    def buynft(self, email, nft_name, quantity):
        try:
            self.c1.execute("select price from seller_details where nft_name = %s", (nft_name,))
            price_tuple = self.c1.fetchone()
            price = price_tuple[0] if price_tuple else 0
            print(f"Price: {price}")
            self.c1.execute("select Balance from user_details where email = %s", (email,))
            balance_tuple = self.c1.fetchone()    
            balance = balance_tuple[0] if balance_tuple else 0
            print(f"Balance: {balance}")
            total_cost = quantity * price
            if balance < total_cost:
                return 0, 0
            balance = balance - total_cost
            self.c1.execute("Update user_details set Balance = %s where email = %s", (balance, email))
            self.con.commit()
            return total_cost, balance
        except sql.Error as e:
            print(f"The error is: {e}")
    
    def show_nft_details(self, selected_nft):
        try:
            self.c1.execute(f"SELECT describe_NFT FROM seller_details WHERE nft_name = %s", (selected_nft, ))
            nft_details = self.c1.fetchone()
            return nft_details
        except sql.Error as e:
            print(f"Error: {e}")
    def close_connection(self):
        self.con.close()