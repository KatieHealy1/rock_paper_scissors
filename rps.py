from random import randint, random



def game():
    
    d = {}
    # rand = random.randst(a, b, c)
    
    # a = "Rock"
    # b = "Paper"
    # c = "Scissors"

    while True:
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
        x = input("Choose rock, paper, scissors or say 'quit' to quit. ")
        if x.lower().strip() == "rock":
            if computer == "paper".lower().strip():
                print("You Lose")
        elif x.lower().strip() == "scissors":
            if computer == "rock".lower().strip():
                print("You Lose")
        elif x.lower().strip() == "scissors":
            if computer == "paper".lower().strip():
                print("You Win")       
        elif x.lower().strip() == "paper":
            if computer == "scissors".lower().strip():
                print("You Lose")
        
        else:
            print("You quit!")

game()







        #     if cart.lower().strip() == "show":
        #         print("Here is what is in your shopping cart." + str(items) + " You can say 'quit' to quit. ")
        #     if cart.lower().strip() == "add":
        #         item = input("Enter item to add to list :")
        #         items.append(item)
        #         print("An item has been added to your shopping cart. ")
        #     if cart.lower().strip() == "delete":
        #         item2 = input("Enter the item you would like removed from your shopping cart or say 'quit' to quit. ")
        #         items.remove(item2)
        #         print("Your item has been removed from your shopping cart.")
        #     clear_output   
        # if x.lower().strip() == "quit" or cart.lower().strip()== "quit":
        #     print(f"Here is your current shopping list: " + str(items))
        # break
            
        # d[x] = cart
        
