class ATM:
    def __init__(self,name,surname,account,addaccount):
        self.name=name
        self.surname=surname
        self.account=account
        self.addaccount=addaccount

    def Intro(self):
        print("Mr/Mrs {self.name} {self.surname} hello")
        self.Options()

    def Options(self):
        select=input("If you want to withdrow press 'w' or if you want to deposit press 'd' or for quit press 'q'")
        if select=="w" or select=="W":
            self.Withdrow()
        elif select=="d" or select=="D":
            self.Deposit()
        elif select=="q" or "Q":
            self.Finish()
        else:
            print("Sorry! You selected a wrong character, please try again")
            self.Options()
    
    def Withdrow(self):
        add_Selection=input("If you want to use additional account press 'y', if you don't want it press 'n' or for quit press 'q': ")
        if add_Selection=="y" or add_Selection=="Y":
            amount=int(input("How much money do you want to withdrow?: "))
            if amount<(self.account+self.addaccount):
                sum=(self.account)-amount
                print(f"After your withdrow process, the remaining is {sum}")
            else:
                print("Sorry! Your account is not sufficient")
        elif add_Selection=="n" or add_Selection=="N":
            amount=int(input("How much money do you want to withdrow?: "))
            if amount<(self.account):
                sum=self.account-amount
                print(f"After your withdrow process, the remaining is {sum}")
            else:
                print("Sorry! Your account is not sufficient")
            self.Finish()
        elif add_Selection=="q" or add_Selection=="Q":
            self.Finish()
        else:
            print("Sorry! You selected a wrong character, please try again")
            self.Withdrow()
        

    def Deposit(self):
        amount=int(input("How much money do you want to deposit?"))
        sum=self.account+amount
        print(f"After your deposit process, your account is {sum}")
        self.Finish()
        
    def Finish(self):
        print(f"Have a nice days Mr/Mrs {self.name} {self.surname}")
    

user1=ATM("Soner", "Varkan",5000,2000)
print(user1.Intro())