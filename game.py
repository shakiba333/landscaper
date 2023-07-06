money = 0
userChoice = ""
tools = [
    {
        "tool": "teeth",
        "income": 1 ,
        "price": 0
    },
    {
        "tool": "scissors",
        "income": 5,
        "price": 5
    },
    {
        "tool": "lawnmower",
        "income": 50,
        "price": 25
    },
    {
        "tool": "battery powered lawnmower",
        "income": 100,
        "price": 250
    },
    {
        "tool": "hired students",
        "income": 1000,
        "price": 500
    }
]

my_inventory = [
    {
        "tool": "teeth",
        "income": 1,
        "price": 0
    }
]


def check_tools():
    global money
    last_bought_tools = my_inventory[-1]
    userChoice = input(f"You can spend the day cutting lawns and make ${last_bought_tools['income']}. Using just your {last_bought_tools['tool']}: y or n\n")
    if 'y' in userChoice:
        money = money + last_bought_tools['income'];
        print(f"your income now equals to ${money}")
        if money == 1000:
            print("You've won!")
    else:
        return True    
        



def buy_tools():
    global money
    for tool in tools:
        if  money == tool["price"]:
            userChoice = input(f"You can buy {tool['tool']} for ${tool['price']}:y or n\n")
            if 'y' in userChoice:
                my_inventory.append(tool)
                money = money - tool["price"]
                check_tools()


while userChoice != "n" and money < 1000:
    if check_tools():
        break
    buy_tools()







