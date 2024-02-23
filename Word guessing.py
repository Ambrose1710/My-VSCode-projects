import random
import time as t 


word = ['magic', 'program', 'python', 'dancer', 'movie', 'geeks'
        'artist', 'player','mother', 'computer', 'gamble']

word = random.choice(word)
spaces = ['_']*len(word) #shows blank lines indicating how long the word is
turns = 10 #the number of turns I want the user to have

print(spaces)
print(f"This word has {len(word)} letters")
t.sleep(1)
print(f"You have {turns} attempts")
print("Guess the characters in my word😁!")

all_guesses = []

def word_game(turns):
    
    #game loop
    while turns > 0:
        guess = input("What's your guess?: ")
        #guess = guess.lower
        #check if it is a single letter
        if len(guess) != 1 or not guess.isalpha() : #.isalpha() is true if all the characters are alphabetic letters(a - z)
            print("Invalid guess. Please enter a single letter.")
            continue #continue to the next iteration of the loop
        
        all_guesses.append(guess) #add valid guess to the list of guesses
        
        if guess in word:
            print("You got one!")
        else:
            print("Wrong guess but try again")
            turns -= 1 
        revealed_word = '' #empty string to store the revealed word
        
        #we now update the revealed word with the correctly guessed letters and underscores
        for letter in word:
            if letter in all_guesses:
                revealed_word += letter + ''
            else:
                revealed_word += '_'
        print("My word: ", revealed_word) #prints the current state of the word
        print("Attempts left: ", turns)
        
        # Checking if all the letters have been guessed
        if all(letter in all_guesses for letter in word):
            print("Congratulations!! You've guessed all the correct letters!")
            break #exit loop
        
        if turns == 0:
            print(f"""Oh no! You're out of turns.
                The word was {word}. Better luck next time!""")
            break
    

def play_again():       
    play_again = input("Do you want to play again? (y/n): ").lower

    if play_again == 'y':
        word_game(word)
    else:
        pass 

word_game(10)
play_again()
            
        

           
        
            
            
    
        
