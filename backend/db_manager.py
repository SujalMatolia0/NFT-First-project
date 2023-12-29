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
    def insert_bank(self, cardno, cvv, email):
        try:
            self.c1.execute("Update user_details set credit_card = %s, cvv = %s where email = %s", (cardno, cvv, email))
            self.con.commit()
            return True
        except sql.Error as e:
            print("The error is: ", e)
            return False
    def fetch_user(self, email, pswd):
        try:
            self.c1.execute(f"SELECT email,pass from user_details WHERE email = %s AND pass = %s", (email, pswd))
            user = self.c1.fetchone()
            return user is not None
        except sql.Error as e:
            print(f"Error: {e}")
    def nftnames_for_nftdetails(self, nft_names):
        try:
            self.c1.execute("Select nft_name from nft_details")
            nft_names = self.c1.fetchall()
            return nft_names
        except sql.Error as e:
             print(f"Error: {e}")
    def show_nft_details(self, selected_nft):
        try:
            self.c1.execute(f"SELECT desciption FROM nft_details WHERE nft_name = '{selected_nft}'")
            nft_details = self.c1.fetchone()
            return nft_details
        except sql.Error as e:
            print(f"Error: {e}")
    def close_connection(self):
        self.con.close()