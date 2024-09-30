import random
# Import the random module to allow random choices this will choice from computer side
def get_user_choice():
    while True:# Loop until a valid choice is made
        # Prompts for input to user
        choice = input("Choose rock, paper, or scissor ").lower()# convert into lower case
        if choice in ['rock', 'paper', 'scissor']:
            return choice
       # checks for the valid input
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def decides_winner(user_choice, computer_choice):# going to decide winner btween user & computer
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
    # display the rsesults 
def display_results(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)
# main function of the game R,P,S
def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissor")
    
    while True: #this is the continuous loop frpm selecting choice by paperuser to score btween user & computer  
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = decides_winner(user_choice, computer_choice)
        
        display_results(user_choice, computer_choice, result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        # keep the record of the score of user & computer
        print(f"\nScore: You {user_score} - Computer {computer_score}")
        # this statement always gonna present after completion of game
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
