import random, time


name = input("What is your name?:")
print(f"Hello {name} ! Welcome to Guess the Number game!")
print("I'm guessing a number between 1 and 20, guess it and you win..")
num = random.randint(1,20)

for i in range(1,7):
    print("Take a guess:")
    gnum = int(input())
    if gnum > num:
        print("That guess was too high...")
    elif gnum < num:
        print("That guess was too low...")
    else :
        break

if gnum == num:
    print(f"Congrats {name}, you guessed it in {str(i)} rounds!")
else:
    print(f"Sorry, you lost, I had guessed {num}")
time.sleep(5)
