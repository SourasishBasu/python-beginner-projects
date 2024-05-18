############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user=[]
comp=[]
flag = 1

def winloss(u,c,comp,user):
    if u <= 21 and c <= 21:
        if u == 21 and c !=21 and (user == [10,11] or user == [11,10]):
            print("  You win with a blackjack.")
        elif c==21 and u <= 21 and (comp == [10,11] or comp == [11,10]):
            print("  Computer wins with a blackjack.")
        elif u > c:
            print("  You win.")
        elif c > u:
            print("  You lose.")
        elif u == c:
            print("  Draw.")
    elif u <= 21 and c > 21:
        if u == 21 and (user == [10,11] or user == [11,10]):
            print("  Computer went Over. You win with a blackjack.")
        elif u < 21:
            print("  Computer went Over. You win.")
    elif  u > 21 and c > 21:
        if u > c:
            print("  You went Over. You lose.")
        elif c > u:
            print("  Computer went Over. You win.")
    elif u > 21 and c <= 21:
        if c == 21 and (comp == [10,11] or comp == [11,10]):
            print("  You went Over. You lose. Computer wins with a blackjack.")
        elif c < 21:
            print("  You went Over. You lose.")    
        
        
def blackjack(no_user,no_comp):
    global flag
    flag1=flag
    if flag1 != 0:
        play_con = "y"
    while play_con == "y": 
        for i in range(no_user): 
            user.append(random.choice(cards))
        for i in range(no_comp):
            comp.append(random.choice(cards))
        score_user = sum(user)
        score_comp = sum(comp)
        if score_user>21 and 11 in user:
            user.pop(-1)
            user.append(1)
            score_user = sum(user)
        elif score_comp>21 and 11 in comp:
            comp.pop(-1)
            comp.append(1)
            score_comp = sum(comp)
#        print(user)
        print(f"  Your cards: {user}, current score: {score_user}")
 #       print(comp)
        print(f"  Computer's first card: {comp[0]}")
        if score_user >= 21 or score_comp >= 21:
            print(f"  Your final hand: {user}, final score: {score_user}")
            print(f"  Computer's final hand: {comp}, final score: {score_comp}")
            winloss(score_user,score_comp,comp,user)
            flag1 = 0
            play_con="n"
            break
        else:
            play_con=input("Type 'y' to get another card or 'n' to pass: ")
            if play_con =='y':
                no_user = 1
                no_comp = random.randint(0,1)
                continue
            elif play_con =='n':
                print(f"  Your final hand: {user}, final score: {score_user}")
                print(f"  Computer's final hand: {comp}, final score: {score_comp}")
                winloss(score_user, score_comp, comp, user)
                flag1 = 0
                play_con="n"
                break
    
play=input("Do you want to play a game of Blackjack? Type y or n: ")

while play == 'y':
    clear()
    print(logo)
    blackjack(2,2)
    user=[]
    comp=[]
    play=input("Do you want to play a game of Blackjack? Type y or n: ")



    
    










##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

