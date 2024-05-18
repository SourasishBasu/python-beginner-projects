#Step 2
import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
chosen_list = list(chosen_word.strip(""))

#print(f'Pssst, the solution is {chosen_word}.')
#Above code used for debugging and testing purposes. 

lives = 6

display=[]
for i in range(len(chosen_word)):
    display.append("_")
#print(display)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

while display != chosen_list:

    guess = input("Guess a letter: ").lower()
    count = 0

    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    if guess in display:
        print(f"You have already guessed {guess}.")
    for letter in chosen_word:
        if letter == guess:
            count = 0
            break
        else:
            count +=1
    if count > 0:
        print(f"You guessed {guess}. It's not in the word. You lose a life. ")
        print(hangman_art.stages[lives-1])
        lives -= 1
    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    else:
        for letter in range(len(display)):
            if chosen_list[letter] == guess:
                display[letter] = guess
                
    print(" ".join(display))

    if lives == 0:
        print("You died. GAME OVER.")
        break
        
disp_str="".join(display)
if disp_str == chosen_word:
    print(f"You guessed the word {disp_str}. You win.")
    
