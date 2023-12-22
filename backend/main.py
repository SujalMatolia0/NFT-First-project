class Mainmenu():
    def Mainmenu():
      print('''WHAT DO YOU WANT -
          1.WANT TO KNOW INFORMATION ABOUT NFT's
          2. WANT TO BUY,SELL or KNOW PRICE OF NFT's
          3. EXIT''')
      MMs = int(input("which option do you want to select ?- "))
      if MMs == 1:
        knowinfo()
      elif MMs == 2:
        nfts()
      else:
         while MMs == 3:
            break
    
    def knowinfo():
      print('''IN INTERNATIONAL -
             1.AXIE INFINITY AXS
             2.THE SANDBOX SAND
             3.CRYPTO PUNK
             FOR SANSKARIANS -
             4. SANSKARIANS ARTWORK
             5. ANNUAL FUNCTION TOKEN BOOKING
             6. BACK TO MAIN MENU''')
      kps = int(input("Which option do you want to select ?- "))
      if kps == 1:
       print('''It is a INFINITY AXS game-based nft where you can buy your private areas to
          play, you can have your private island in the game so that you can play, 
          enjoy and meetup their. Then what are you waiting for go buy and enjoy with your friends.''')
       ak = input("Do you want to go back to main menu ? y/n -")
       if ak == "y":
          Mainmenu()
       else:
           knowinfo()
      elif  kps == 2:
        print('''It is a SANDBOX SAND game-based nft where you can buy your private areas to
          play, you can have your private island in the game so that you can play, 
          enjoy and meetup their. Then what are you waiting for go buy and enjoy with your friends.''')
        ak = input("Do you want to go back to main menu ? y/n -")
        if ak == "y":
          Mainmenu()
        else:
           knowinfo()
      elif kps == 3:
        print('''Cryptopunks is an NFT project released on the Ethereum blockchain by Larva Labs,
          and consists of 10,000 unique pixelated characters. Some are human, some aliens,
          some zombies and some apes. 
          Each punk has certain attributes that are of a different level of rarity amongst the entire fleet''')
        ak = input("Do you want to go back to main menu ? y/n -")
        if ak == "y":
          Mainmenu()
        else:
           knowinfo()
      elif kps == 4:
        print("It is a NFT made by SANSKAR INTERNATIONAL SCHOOL and you can get assets of the pure art of sanskarians so what are you waiting for just go and grab a new and trendy art of sanskarians..")
        ak = input("Do you want to go back to main menu ? y/n -")
        if ak == "y":
          Mainmenu()
        else:
           knowinfo()
      elif kps == 5:
        print("It is a NFT that gives you assets of sanskar international school annual function tokens and fest so what are you waiting for grab your toke of enjoyment.")
        ak = input("Do you want to go back to main menu ? y/n -")
        if ak == "y":
          Mainmenu()
        else:
           knowinfo()
      else:
        Mainmenu()
            
    def nfts():
        print('''IN INTERNATIONAL -
             1.AXIE INFINITY AXS 
             2.THE SANDBOX SAND
             3.CRYPTO PUNK
             FOR SANSKARIANS -
             4. SANSKARIANS ARTWORK
             5. ANNUAL FUNCTION TOKEN BOOKING
             6. BACK TO MAIN MENU
             7. EXIT...''')
        slt = int(input("Which one of the do you want to know information ?- "))
        if slt == 1:
         nam = "AXIE INFINITY AXS"
         price = 30
         bse(nam,price)
        elif slt == 2:
         nam = "THE SANDBOX SAND"
         price = 50
         bse(nam,price)
        elif slt == 3:
         nam = "CRYPTO PUNK"
         price = 20
         bse(nam,price)
        elif slt == 4:
         nam = "SANSKARIANS ARTWORK"
         price = 10
         bse(nam,price)
        elif slt == 5:
         nam = "ANNUAL FUNCTION TICKET BOOKING"
         price = 5
         bse(nam,price)
        elif slt == 6:
         Mainmenu()
        else :
         while slt == 7:
            break


class Welcome():
    if con.is_connected():
     print("!!!     WELCOME HERE     !!!")
     a = input("What's your name ? -")
     print("SO Hello", a)
     print("BEFORE WE BEGIN", a, "I would like to know")
     b = int(input('''DO YOU WANT TO 
                  1.sign up  or
                  2.log in   (!!!YOU CAN ANSWER IT BY TYPING 1 OR 2 ON SCREEN!!!) '''))
    if b == 1:
     print("!!!WELCOME TO THE SIGN UP!!!")
     name1 = input("Enter Your First Name :")
     name2 = input("Enter Your Last Name  :")
     email = input("Enter Your EMAIL :")
     pswd = input("Create your password :")
     cpswd = input("Confirm Your Created password :")
     while pswd != cpswd  and len(pswd) <= 5 :
        print("***********************please enter correct 6 digit password***********")
        continue
     else:
        print("success")
     bac()
     dat = date.today()
     data_insert = "insert into userdetails values( '{}', '{}','{}','{}','{}',{},{},{},'{}')".format(name1,name2,email,pswd,cpswd,B_AC,cvv,wlt,dat)
     c1.execute(data_insert)
     con.commit()
    if b == 2:
     Email = input("Enter a username:")
     c1.execute(f"SELECT email from userdetails WHERE email ='{Email}'")
     if c1.fetchall():
        print('OK!!! ACCOUNT VERIFIED')
        print()
        psswd = input("Enter a password")
        bac()
        c1.execute(f"select password from userdetails where password = '{psswd}'")
        print("WELCOME", a)
    

class Account():
    def bac(B_AC,cvv,wlt):
      B_AC = int(input('''Enter your 16 digit credit card number : '''))
      cvv = int(input('''Enter your CVV code : '''))
      print("YOUR ACCOUNT SUCCESSFULLY FOUND.")
      global wlt

      wlt = int(input("ENTER YOUR MONEY TO BE ADDED : "))
      return B_AC
      return cvv
      return wlt


class Buyyer():
    def bse(nam,price) :
        print("THIS IS", nam)
        AIAa = int(input('''DO YOU WANT TO KNOW 
                 1. PRICE IN NFT ADDA 
                 2.WANT TO BUY 
                 3.WANT TO SELL
                 4. EXIT -'''))
        if AIAa == 1:
                  print(" IT's PRICE IN NFT ADDA -", "$",price)
        elif AIAa == 2:
                  print("To Buy NFT")
                  if wlt > price:
                      abuy = int(input("Enter your token want to buy :"))
                      attl = abuy * price
                      print("Your token worth will be :",attl)
                      cnfm = input("DO you want to buy ?y/n ")
                      if cnfm == "y":
                          print(abuy, "NFT BOUGHT")
                          uawlt = wlt-attl
                          print("THE money you left in your wallet :",uawlt)
                          nfts()
                      else :
                          while cnfm !="y":
                              break
                          nfts()
                  else :
                      print("YOU DON't have enough balance.")
                      nfts()
        elif AIAa == 3:
            print("To sell NFT")
            b = 5>2
            if b == True:
                i = input("DO you want  to sell your nft ?y/n -")
                if i =="y":
                    b = False
                    print("You Got $30 in your wallet")
                    print("Now you have :",wlt + 30)
        else:
            while cnfm !="y":
                break
            nfts()