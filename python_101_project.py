import random

winning_move = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}

choices = ["Rock", "Paper", "Scissors"]

print("Welcome to the Rock, Paper, Scissors Game! Type quit to quit.")

while True:
    pc = random.choice(choices)
    
    player = input("Do you choose Rock, Paper, or Scissors? ").capitalize()
    if player == "Quit":
        break

    if player not in choices:
        print("Invalid answer. Please enter only Rock, Paper, or Scissors.")
        continue

    if player != winning_move[pc]:
        if player == pc:
            msg = f"You both chose {pc}. It's a draw."
        else:
            msg = f"{pc} beats {player}. Sorry, try again."

        print(msg)
        continue
    else:
        print(f"{player} beats {pc}. Congratulations!")
        new_game = input("Do you want to play again? Y/N ").capitalize()
        if new_game != "Y":
            print("Goodbye")
            break