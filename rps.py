from random import choice



def game():

    while True:
        
        choices = ["rock", "paper", "scissors"]
        computer = choice(choices)
        a = "Quit"
        userInput = input("Choose rock, paper, scissors or type 'quit' to quit: ")
        if(userInput == computer):
                print("The computer also chose " + userInput + " so, it's  a tie.")
        elif userInput.lower() == "rock":
            if computer == "paper":
                print("You Lose!! Computer chose " + computer + ". Try again, see if you can beat the computer!")
            if computer == "scissors":
                print("You Win!! Computer chose " + computer)           
        elif userInput.lower() == "scissors":
            if computer == "rock":
                print("You Lose!! Computer chose " + computer + ". Try again, see if you can beat the computer!")
            if computer == "paper":
                print("You Win!! Computer chose " + computer)    
        elif userInput.lower() == "paper":
            if computer == "scissors":
                print("You Lose!! Computer chose " + computer + ". Try again, see if you can beat the computer!")
            if computer == "rock":
                print("You Win!! Computer chose " + computer) 
        elif userInput != a.lower().strip():
            print("invalid name")
        else:
            print("You quit! Thank you for playing")
            break
   
game()


