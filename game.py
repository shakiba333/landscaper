money = 0
tools = []
userChoice = ""

while userChoice != "quit":
    userChoice = input("Using just your teeth, you can spend the day cutting lawns and make $1.\n")
    if "teeth" in userChoice:
        money = money + 1;
        print(money)
     



