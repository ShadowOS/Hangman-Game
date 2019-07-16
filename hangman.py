# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word_letters=[]

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    b=0
    a=list(secret_word)
    for i in letters_guessed:
        for p in a:
            if i==p:
                b=b+1
    return(len(a)==b)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    my_word=[]
    a=list(secret_word)
    
    for i in a:
        if i in letters_guessed:
            my_word.append(i)
        else:
            my_word.append("_")
    my_word=' '.join(my_word)        

    return(my_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    a=string.ascii_lowercase
    b=[]
    b=list(a)
    
    for i in letters_guessed:
        if i in b:
            b.remove(i)
    b=' '.join(b)        
    return(b)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings=3
    letters_guessed=[]
    guess=6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("-------------")
    print("You have",guess,"guesses left.")
    print("You have '3 WARNINGS !!!',if you provide invalid input,you get warning 3 times,after that you will loose your guess as a Penalty")
    print("Available letters: abcdefghijklmnopqrstuvwxyz ")
    print("if you guess incorrect vowels then you loose 2 guesses")
    print("lets start to Play HANGMAN!!! Be READY")
    letters_guessed.clear()
    Vowels=['a','e','i','o','u']
    i=0
    while i < 6:
        if is_word_guessed(secret_word, letters_guessed)==False:
            a=input("Guess a letter=")
            a=a.lower()
            
            cd=get_available_letters(letters_guessed)
            if a in cd:
                letters_guessed.append(a)
                if a in secret_word:
                    print(get_guessed_word(secret_word, letters_guessed) )
                    print( get_available_letters(letters_guessed))
                    print("You have",guess,"guesses left")
                    print(letters_guessed)
                    print("-------------")
                    i=i
                elif a in Vowels:
                    i=i+2
                    guess=guess-2
                    print("you guess incorrect vowels")
                    print(get_guessed_word(secret_word, letters_guessed) )
                    print("You have",guess,"guesses left")
                    print( get_available_letters(letters_guessed))
                    print(letters_guessed)
                    print("-------------")
                else:
                    i=i+1
                    guess=guess-1
                    print(get_guessed_word(secret_word, letters_guessed) )
                    print("You have",guess,"guesses left")
                    print( get_available_letters(letters_guessed))
                    print(letters_guessed)
                    print("-------------")
            elif a in letters_guessed:
                warnings=warnings-1
                print("Oops you have entered Invalid input, you have left",warnings,"warnings !!!")
                print(get_guessed_word(secret_word, letters_guessed) )
                print("You have",guess,"guesses left")
                print( get_available_letters(letters_guessed))
                print(letters_guessed)
                print("-------------")
                if warnings<=0:
                    warnings=1
                    guess=guess-1
                    i=i+1      
            else:
                warnings=warnings-1
                print("Oops you have entered Invalid input, you have left",warnings,"warnings !!!")
                print(get_guessed_word(secret_word, letters_guessed) )
                print("You have",guess,"guesses left")
                print( get_available_letters(letters_guessed))
                print(letters_guessed)
                print("-------------")
                if warnings<=0:
                    warnings=1
                    guess=guess-1
                    i=i+1
                
        else:
            i=6
    b=0
    a=list(secret_word)
    letters_guessed_copy=letters_guessed[:]
    for p in a:
        for i in letters_guessed_copy:
            if i==p:
                b=b+1
                letters_guessed_copy.remove(p)       
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("You Won !!!")
        c=guess*b                            #guess*10
        print("Congratulations!!! You have earned",c,"Points")
    else:
        print("You loss , Better luck next time ")
        print("The 'SECRET WORD' is=",secret_word)         
               
        
    return()
    
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    secret_word=my_word
    letters_guessed=[]
    for i in secret_word:
        if i!='_':
            letters_guessed.append(i)

    secret_word=other_word
    other_word=get_guessed_word(secret_word, letters_guessed)
    return(my_word==other_word)


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches=[]
    for i in wordlist:
        other_word=i
        if match_with_gaps(my_word, other_word):
            possible_matches.append(i)
    return(possible_matches)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings=3
    letters_guessed=[]
    guess=6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("-------------")
    print("You have",guess,"guesses left.")
    print("You have '3 WARNINGS !!!',if you provide invalid input,you get warning 3 times")
    print("after that you will loose your guess as a Penalty")
    print("Available letters: abcdefghijklmnopqrstuvwxyz ")
    print("if you guess incorrect vowels then you loose 2 guesses")
    print("lets start to Play HANGMAN!!! Be READY")
    letters_guessed.clear()
    x=[]
    x.append('*')
    Vowels=['a','e','i','o','u']
    i=0
    while i < 6:
        if is_word_guessed(secret_word, letters_guessed)==False:
            a=input("Guess a letter=")
            a=a.lower()
            
            cd=get_available_letters(letters_guessed)
            if a in cd:
                letters_guessed.append(a)
                if a in secret_word:
                    print(get_guessed_word(secret_word, letters_guessed) )
                    print( get_available_letters(letters_guessed))
                    print("You have",guess,"guesses left")
                    print(letters_guessed)
                    print("-------------")
                    i=i
                elif a in Vowels:
                    i=i+2
                    guess=guess-2
                    print("you guess incorrect vowels")
                    print(get_guessed_word(secret_word, letters_guessed) )
                    print("You have",guess,"guesses left")
                    print( get_available_letters(letters_guessed))
                    print(letters_guessed)
                    print("-------------")
                else:
                    i=i+1
                    guess=guess-1
                    print(get_guessed_word(secret_word, letters_guessed) )
                    print("You have",guess,"guesses left")
                    print( get_available_letters(letters_guessed))
                    print(letters_guessed)
                    print("-------------")
            elif a in letters_guessed:
                warnings=warnings-1
                print("Oops you have entered Invalid input, you have left",warnings,"warnings !!!")
                print(get_guessed_word(secret_word, letters_guessed) )
                print("You have",guess,"guesses left")
                print( get_available_letters(letters_guessed))
                print(letters_guessed)
                print("-------------")
                if warnings<=0:
                    warnings=1
                    guess=guess-1
                    i=i+1
            elif a in x:
                my_word=get_guessed_word(secret_word, letters_guessed)
                print(show_possible_matches(my_word))
                x.remove('*')
                
            else:
                warnings=warnings-1
                print("Oops you have entered Invalid input, you have left",warnings,"warnings !!!")
                print(get_guessed_word(secret_word, letters_guessed) )
                print("You have",guess,"guesses left")
                print( get_available_letters(letters_guessed))
                print(letters_guessed)
                print("-------------")
                if warnings<=0:
                    warnings=1
                    guess=guess-1
                    i=i+1
                
        else:
            i=6
    b=0
    a=list(secret_word)
    letters_guessed_copy=letters_guessed[:]
    for p in a:
        for i in letters_guessed_copy:
            if i==p:
                b=b+1
                letters_guessed_copy.remove(p)       
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("You Won !!!")
        c=guess*b                            #guess*10
        print("Congratulations!!! You have earned",c,"Points")
    else:
        print("You loss , Better luck next time ")
        print("The 'SECRET WORD' is=",secret_word)         
               
        
    return()



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
input("please enter to exit")