import random

def get_computer_choice():
    # Randomly select between Rock, Paper, or Scissors
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    # Get user's choice
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        user_input = input("Enter your choice: ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the game rules
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def rock_paper_scissors():
    user_wins = 0
    computer_wins = 0
    rounds = 0

    print("Welcome to Rock, Paper, Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win this round!")
            user_wins += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_wins += 1
        else:
            print("This round is a tie!")

        rounds += 1

        print(f"Score: You {user_wins} - Computer {computer_wins}")

        # Ask if the user wants to play another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Game over! Final score: You {user_wins} - Computer {computer_wins}")

# To start the game, call the function
rock_paper_scissors()
