import random

print("Welcome to Word Guessing Game!")

words_list = ['elephant','cycle','sunshine','symphony','mountain','octopus','galaxy','parachute','dragon','avalanche','tornado','firecrackers','saffron','onomatopoeia','chair','smile']

randomword = random.choice(words_list)
correctoutput = [char for char in randomword]

output = ['_' for ele in randomword] #makes a list of underscores for each char in word
guesses = 5
print (output , "\nNumber of guesses: ", guesses)

while (guesses!=0 and output != correctoutput):
    myguess = input('Enter your guess: ')
    if myguess in randomword:
        for index,char in enumerate(randomword): #enumerate keeps track of element and its index at the same time(pehle index fir element)
            if char == myguess:
                output[index]=myguess
        print (output , "\nNumber of guesses left: " , guesses)
    else:
        guesses = guesses - 1
        print (output , "\nNumber of guesses left: " , guesses)

if guesses==0:
    print("You lost \nThe word was: " , randomword)
elif output==correctoutput:
    print("You win \nThw word was: " , randomword)