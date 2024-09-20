
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


from hangman_art import logo
print(logo)

#Testing code
print(f'Shhhhhhh the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess of a letter: ").lower()

    
    
    if guess in display:
        print(f"You you have already guessed. {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Ooops! You are dead!.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Bravo! You live!.")

    
    from hangman_art import stages
    print(stages[lives])