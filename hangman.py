import random
def hangman(word):
    stages = ['',
             '----------          ' ,
             '          |           ',
             '          0          ',
             '         /|\            ',
             '         / \ ',
             '                         ',
             '']
    wrong = 0
    board = list('_'*len(word))
    wrong_letters=[]
    wordlist=list(word)
    print("Letter Board: " + ''.join(board))

    while wrong < len(stages)-1:
        guess = input("Enter a letter:")
        if guess in wordlist:
            board[wordlist.index(guess)] = guess
            wordlist[wordlist.index(guess)]='$'
            print("Correct!!")
            print("---------------------------------------")
            print('\n'.join(stages[0:wrong]))
            print("---------------------------------------")

            print("Letter Board: "+''.join(board))
            print("---------------------------------------")
            if '_' not in board:
                print("Congratulations!! you win")
                break
        else :
            wrong_letters.append(guess)
            print("Wrong Guess...")
            print("Wrong Guesses till now:",wrong_letters)
            print("---------------------------------------")
            print('\n'.join(stages[0:wrong]))
            wrong+=1
            print("---------------------------------------")
            print("Letter Board: ",board)
            print("---------------------------------------")
        if wrong==len(stages)-1:
            print("Sorry.. you lose")

list_of_words = ['india','america','russia','china','brazil','australia']
hangman(random.choice(list_of_words))