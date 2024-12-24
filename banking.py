balance=int(input("input bank balance: "))
withdraw=int(input("how much do you wish to withdraw: "))
if balance>(withdraw+50):
    balance=balance-(withdraw+50)
    print("the withdrawal is complete")
    print("the remeaning balance: ",balance)
else:
    print("you dont have sufficient balance")    