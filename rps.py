#import random module for AI functions
import random

# file i/o function for historical results
def load_results():
    text_file = open("history.txt", "r")
    #read file function that reads each element separated by a comma as a separate value
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l):
    text_file = open("history.txt", "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l))
    text_file.close()

#welcome message
results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print("Welcome")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")

#initialize user, computer choices
computer = random.randint(1,3)
user = int(input("[1]Rock   [2]Paper   [3]Scissors   [9]Quit\n"))

#gameplay loop
while not user == 9:
    #User chooses Rock
    if user == 1:
        if computer == 1:
            print("Computer chooses Rock ... you TIE!")
            ties += 1
        elif computer == 2:
            print("Computer chooses Paper ... you LOSE")
            losses += 1
        else:
            print("Computer chooses Scissors ... you WIN")
            wins += 1
    #User Chooses Paper
    elif user == 2:
        if computer == 1:
            print("Computer chooses Rock ... you TIE!")
            wins += 1       
        elif computer == 2:
            print("Computer chooses Paper ... you LOSE")
            ties += 1
        else:
            print("Computer chooses Scissors ... you WIN")
            losses += 1
    #User Chooses Scissors
    elif user == 3:
        if computer == 1:
            print("Computer chooses Rock ... you TIE!")
            losses += 1       
        elif computer == 2:
            print("Computer chooses Paper ... you LOSE")
            wins += 1
        else:
            print("Computer chooses Scissors ... you WIN")
            ties += 1
    else:
        print("Invalid Selection. Please Choose to Continue.")
    #Print updated Results
    print("Wins: %s Ties: %s Losses: %s" % (wins, ties, losses))

    #Prompt User to make another selection
    print("Please Choose to Continue...")
    #initialize user, computer choices
    computer = random.randint(1,3)
    user = int(input("[1]Rock   [2]Paper   [3]Scissors   [9]Quit\n"))

#game over, save results
print("You ROCK! Let's WRAP this up! We'll CUT to the chase next time!")
save_results(wins, ties, losses)