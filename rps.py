from random import random


def game():
    
    d = {}
    rand = random.randstr(a, b, c)

    a = "Rock"
    b = "Paper"
    c = "Scissors"

    while True:
        x = input("Choose rock, paper, scissors or say 'quit' to quit. ")
        if x.lower().strip() == "Rock" and rand == b.lower().strip():
            print("You Lose")
        elif x.lower().strip() == "Scissors" and rand == a.lower().strip():
            print("You Lose")
        elif x.lower().strip() == "Paper" and rand == c.lower().strip():
            print("You Lose")
        
        else:
            print("You quit!")









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
        
