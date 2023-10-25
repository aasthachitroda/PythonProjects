import random
print('Welcome to Bulls and Cows Game! \nHow to play: \nThere is a secret 4 digit code that you have to guess \nAfter each guess you\'ll be given 2 hints: \n1)Bulls: number of correct digits in correct place \n2)Cows: number of correct digits in wrong place \nYou have 10 tries to guess the secret code \nGood luck! \n')

def NumToList(num):
    numList = [int(i) for i in str(num)]
    return numList

def checkRepetition(numList):
    return len(numList)==len(set(numList))

def secretCodeGenerate():
    while True:
        randomNo = random.randint(1000,9999)
        secret_code = NumToList(randomNo)
        if checkRepetition(secret_code)==True:
            break
    return secret_code,randomNo

def BullsAndCows(secret_code,input_code):
    bull_cow = [0,0]
    for i,j in zip(secret_code,input_code): 
        if j in secret_code: 
            if j==i:
                bull_cow[0] += 1 
            else:
                bull_cow[1] += 1 
    return bull_cow

noOfGuesses = 10
guess = 0000
secret_codeList,secretcode = secretCodeGenerate()
while noOfGuesses != 0 and guess!=secretcode:
    guess = int(input('\nEnter your guess: '))
    input_code = NumToList(guess)

    if guess<1000 or guess>9999:
        print('Enter a 4 digit number only \nTry again')
        continue
    
    if checkRepetition(input_code)!=True:
        print('The digits should not be repeated \nTry again')
        continue
    
    noOfGuesses = noOfGuesses - 1
    hintList = BullsAndCows(secret_codeList,input_code)
    print('Bulls:', hintList[0],'\nCows:', hintList[1], '\nGuesses left:',noOfGuesses)

if secret_codeList == input_code:
        print('You Win! \nThe sceret code was:', secretcode)
else:
    print('You Lose \nOut of tries \nThe sceret code was:', secretcode)