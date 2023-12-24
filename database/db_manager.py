import mysql.connector as sql

class DBMS:
    def __init__(self):
        self.con = sql.connect(host = "localhost",user = 'root',passwd = 'pass',database = 'nft_project')
        self.c1 = self.con.cursor()
    def insert_user(self, fname, lname, email, pswd):
        try:
            self.c1.execute( "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                (fname, lname, email, pswd))
            self.con.commit()
            return True
        except sql.Error as e:
            print(f"Error: {e}")
            return False
    def fetch_query(self, query, values = None):
        try:
            if values:
                self.c1.execute(query, values)
            else:
                self.c1.execute(query)
            return self.c1.fetchone()
        except sql.Error as e:
            print(f"Error: {e}")
    def close_connection(self):
        self.con.close()