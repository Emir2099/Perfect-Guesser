import random 

a = random.randint(1,100)

userGuess = None

guesses = 0

while(userGuess != a):
     userGuess = int(input("Enter your guess: "))
     if(userGuess == a):
         print("You guessed it right!")
         guesses += 1
     else:
            if(userGuess > a):
               print("You guessed it wrong! Enter a smaller number")
               guesses += 1
            else:
                print("You guessed it wrong! Enter a larger number") 
                guesses += 1

print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if(guesses < highscore):
    print("You have just broken the high score")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))