import random #gets the random package
import sys


def get_cat(cat):
    '''gets the selected category words and creates a list of all the words in it in lowercase'''
    file=open(str(cat)+'.txt')
    text=file.read()
    words=text.lower().split()
    file.close()
    return words

def letterCheck(letter,word):
    '''Checks if the letter is in the word and will return the list of indexes of the letter. If the letter is not found then it returns -1.'''
    index=[]
    for i in range(len(word)):
        if(word[i:].find(letter))!=-1:
            index.append(word[i:].find(letter)+i)
    if len(index)!=0:
        return set(index)
    else:
        return -1

specialChar='?!@#$%^&*();:.,\'\"-0123456789' #special chars that need to be rejected
state='start' #this will keep track of the state of the game
while state=='start': #While loop keeps the game running unles it is explicitly exited
    state=input("Welcome to Koosha's guessing game! To begin, enter one of the following options:\n\n1)Number Guessing Game\n2)Word Guessing Game\nX)Quit the Game\n")
    if state!='1' and state!='2' and state!='x' and state!='X':
        mistake=True
        while(mistake):
            state=input("Error: Invalid input.\n To begin, enter one of the following options:\n\n1)Number Guessing Game\n2)Word Guessing Game\nX)Quit the Game\n")
            if state!='1' and state!='2' and state!='x' and state!='X':
                mistake=True
            else:
                mistake=False
        
    if state=='1': #Number game section, this needs a way to check if the guessed number is higher or lower
        while True: #makes sure that the number is grater than 0
            diff=int(input("Please enter a number greater than 0. The larger the number, the more options and the higher the difficulty\n"))
            if diff>0: 
                break
        snum=random.randint(0,diff)#secret number
        guessnum=0#guesses
        while state=='1':
            try: #makes sure the guess is valid
                guess=int(input("Guess a number!\n"))
                if 0>guess or guess>diff:
                    raise ValueError("Number not in bounds")
            except ValueError as e:
                print(e)
            else:
                if snum>guess:
                    print('Too low')
                    guessnum+=1
                    print('You have guessed',guessnum,'times')
                if snum<guess:
                    print('Too high')
                    guessnum+=1
                    print('You have guessed',guessnum,'times')
                if snum==guess:
                    print('Congratulations! You guessed correctly! It took',guessnum,'times to get the right answer!')
                    state='start'

    if state=='2': #Word Guessing, We need a way to show the #of wrong guesses and the word slowly being revealed with the guessed letters
        while state=='2':
            try:
                cat=int(input("Choose a Category:\n\n1)Days of the Week\n2)Elements of the Periodic Table\n3)Months of the Year\n4)Objects\n5)Planets in the Solar System\n")) #This is the list of all the categories. Remember to put a \n at the end of the category so it looks nice.
                if (cat!=1 and cat!=2 and cat!=3 and cat!=4 and cat!=5): #to add another category, make a text file in the same directory of the game and name it a number(or letter if you need to) and also add a cat!=**YOUR TEXT FILE NAME** to this line
                    raise ValueError('Invalid Input')
            except ValueError as e:
                print(e)
            else:
                lst=get_cat(cat)
                break
        sword=random.choice(lst).strip(specialChar)#secret word
        wguess=0 #wrong guesses
        gletter=[] #guessed letters
        print("The word is",len(sword),"letters long")
        gword=[] #the word that will be revealed slowly
        for c in range(len(sword)):
            gword.append('_')
        print(gword)
        while state=='2':
            try: #makes sure only one letter is given
                letter=input("Guess a letter!\n").lower()
                if len(letter)!=1:
                    raise ValueError('Guess must be one character long')
                if letter.isdigit():
                    raise ValueError('Guess must be a letter')
                if any(char in specialChar for char in letter):
                    raise ValueError('Special characters are not accepted')
                if letter in gletter:
                    raise ValueError('You have already guessed that letter')
            except ValueError as e:
                print(e)
            else:
                indexes=letterCheck(letter,sword)
                if indexes==-1: #the letter is not in the word
                    wguess+=1
                    print('There is no',letter,'in the word. You have guessed incorrectly',wguess,'times')
                    print(gword)
                    gletter.append(letter)
                else:
                    for i in indexes: #the letter is in the word
                        gword[i]=letter
                    print(gword)
                    gletter.append(letter)
                    if not '_' in gword:
                        state='start'
                        print('Congratulations! The word is',sword,'and you guessed incorrectly',wguess,'times!')
                    
    if state.lower()=='x':
        print('Goodbye!')
        sys.exit()
