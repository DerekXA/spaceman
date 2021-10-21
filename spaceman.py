import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('word.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    #print letters used!!!!
    for letters in secret_word:
        if letters not in letters_guessed:
            return False 
    return True
            
        
    
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    word = [ ]
    for letter in secret_word:
        correct_letter = False
        for guessed_letter in letters_guessed:
            if letter == guessed_letter:
                word.append(letter)
                correct_letter = True
        if correct_letter == False:
            word.append("_")
    return " ".join(word)
    



def is_guess_in_word(user_guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
        
    
    
    guessed_correctly = False
    for letter in secret_word:
        if user_guess == letter:
            print('thats right!!!')
            guessed_correctly = True
            return True
        if guessed_correctly == False:
            print('Thats wrong')
            return False




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    guesses_left = 7
    while guesses_left > 0:

        #TODO: show the player information about the game according to the project spec
        print('next guess')

        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        print('you only have 1 guess per round')
        user_guess = input("enter guess:")
        if len(user_guess) > 1:
            print('only 1 leter at a time') 
            return  
        if user_guess in letters_guessed:
            print('you already guessed that!')
            
         
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        guessed_right = is_guess_in_word(user_guess, secret_word)
        if guessed_right == False:
            guesses_left -= 1
        letters_guessed.append(user_guess)
        print(f'you have {guesses_left} guesses left')
        
        #TODO: show the guessed word so far
        get_guessed_word(secret_word, letters_guessed)
        print(get_guessed_word(secret_word, letters_guessed))
        #TODO: check if the game has been won or lost
        is_word_guessed(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('you win!')
            break
        
        # if guesses_left == 0:
        #     print ('you lost')
        # if user_guess==secret_word:
        #    print('you win')
        # break
        
            
            






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
