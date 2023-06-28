import random 

# Creating a dice roller

print("Welcome to dice roller")

while True: 
    player = input("Would you like to roll a dice? (y/n): ")
    if(player == "y"):
        ai = random.randint(1,6)
        strAi = str(ai)
        print ("You have rolled a " + strAi)
    elif(player == "n"):
        print ("Thank you")
        break
    else: print ("Invalid choice")

