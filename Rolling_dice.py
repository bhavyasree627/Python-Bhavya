import random
r = input("Would you like to roll the dice : Y/N ")
if(r.upper() == "Y"):
    num1 = random.randint(1,6)
    print("You rolled a ",num1,"!")
    r= input("Do you want to roll a dice again? ")
else:
    print("Thank you for playing!")
    