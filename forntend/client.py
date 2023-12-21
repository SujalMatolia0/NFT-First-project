from tkinter import *
from tkinter import ttk

def reset_gui():
    global frm
    frm.destroy()
    create_gui()

def create_gui():
    global frm
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="NFT Adda").grid(column=0, row=0)
    ttk.Button(frm, text="Reset", command=reset_gui).grid(column=1, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=0, sticky='ne', padx=(1315, 0))  

def appMain():
    global frm
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    ttk.Label(frm, text="Welcome To NFT ADDA!!!").grid(column=0, row=0) 
    ttk.Label(frm,text="HERE YOU WILL FIND MOST FAMOUS AND MOST SUITABLE NFT TO YOU...").grid(column=0, row=1) 
    

def mainMenu():
    global frm
    frm = ttk.Frame(root, padding =20)
    frm.grid()
    ttk.Label(frm, text="WHAT DO YOU WANT -").grid(column=0, row=0)
    ttk.Button(frm, text="WANT TO KNOW INFORMATION ABOUT NFT's" ).grid(column=0, row=1)
    ttk.Button(frm, text="WANT TO BUY, SELL or KNOW PRICE OF NFT's" ).grid(column=0, row=2)


def main():
    global root
    root = Tk()
    root.title("NFT Buying & Selling App")
    create_gui()
    appMain()
    mainMenu()
    root.mainloop()  

if __name__ == "__main__":
    main()
