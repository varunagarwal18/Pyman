import random
HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    word=random.choice(wordList)
    return word

def getGuess(alreadyGuessed):
    while True:
        print('\nGuess a letter:')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

while(True):
    print('Do you want to play? (yes or no)')
    if(input()=='no'):
        break
    else:
        print('Topic: Animal')
        secretWord = getRandomWord(words)
        GuessedLetters = ''
        miss=0
        blanks = '_ ' * len(secretWord)
        print(blanks)
        while(True):
            guess=getGuess(GuessedLetters)
            GuessedLetters = GuessedLetters + guess
            print("Guessed Letters: "+GuessedLetters)
            if guess not in secretWord:
                miss=miss+1
                print("Wrong guess,"+str(6-miss)+" chances left.")
                print(HANGMANPICS[miss])
                if(miss==6):
                    print('You lost. The word was '+secretWord+"\n")
                    break
            else:
                for i in range(len(secretWord)):
                    if secretWord[i] == guess:
                        blanks = blanks[:2*i] + guess + blanks[2*i+1:]
                print("Right guess")
                print(blanks)
                if '_' not in blanks:
                    print("You won\n")
                    break
                
            
        
