import random 

def Game(choice):
    tools = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(tools)
    
    if comp_choice == "Rock" and choice == "Scissors":
        print(f"Computer choice: {comp_choice}")
        print("You Lose")
    elif comp_choice == "Rock" and choice == "Paper":
        print(f"Computer choice: {comp_choice}")
        print("You win")
    elif comp_choice == "Rock" and choice == "Rock":
        print(f"Computer choice: {comp_choice}")
        print("Tie")

    if comp_choice == "Paper" and choice == "Scissors":
        print(f"Computer choice: {comp_choice}")
        print("You Win")
    elif comp_choice == "Paper" and choice == "Paper":
        print(f"Computer choice: {comp_choice}")
        print("Tie")
    elif comp_choice == "Paper" and choice == "Rock":
        print(f"Computer choice: {comp_choice}")
        print("You Lose")

    if comp_choice == "Scissors" and choice == "Scissors":
        print(f"Computer choice: {comp_choice}")
        print("Tie")
    elif comp_choice == "Scissors" and choice == "Paper":
        print(f"Computer choice: {comp_choice}")
        print("You Lose")
    elif comp_choice == "Scissors" and choice == "Rock":
        print(f"Computer choice: {comp_choice}")
        print("You Win")                
        

            
print("Do you want to play ?")

decision = input("Enter Yes or No:")

while decision == "Yes":
    option = input("Enter Rock, Paper or Scissors:")
    Game(option)
    print("Do you want to play ?")
    decision = input("Enter Yes or No:")

