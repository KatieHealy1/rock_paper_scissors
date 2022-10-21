from random import choice



def game():
    
    d = {}


    while True:
        choices = ["rock", "paper", "scissors"]
<<<<<<< HEAD
        computer = random.choice(choices)
=======
        computer = choice(choices)
>>>>>>> d66d1361ef797aef4c6231ae356982edc07ea6b4
        x = input("Choose rock, paper, scissors or say 'quit' to quit. ")
        if x == computer:
            print("It's a tie!") 
        elif x.lower().strip() == "rock":
            if computer == "scissors":
                print("You Win!!")
            if computer == "paper":
                print("You Lose!!")
        elif x.lower().strip() == "scissors":
            if computer == "rock":
                print("You Lose")
            if computer == "paper":
                print("You Win")     
        elif x.lower().strip() == "paper":
            if computer == "scissors":
                print("You Lose")
            if computer == "rock":
                print("You Win!")
        else:
            print("You quit! Thank you for playing")
        break

game()
