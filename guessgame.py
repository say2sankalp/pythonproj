import random



comGuess= random.randint(0,100)
while True:
    userGuess= int(input("enter the guessing number "))
    if (userGuess> comGuess):
        print("you have guessed the number more than computer")
    elif(userGuess < comGuess):
        print("you have guessed the number less than ")
    else:
        print("congrrats you have gguessed correctly ")
        break

        
