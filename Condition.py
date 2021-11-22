# age=int(input("please enter your age"))
# if(age>20):
#     print('U are an adult, you can vote')
# elif(age>12):
#     print("you are a teenager, you can't vote")
# else:
#     print('you are a kid, and can not vote')


# Friends=["Pratham","Srujan","Vinni","Rudra"]
# for f in Friends:
#     print (f)
# count=5
# while(count>=0):
#     print (count)
#     count-=1

# name=input('enter your name')
# cc=0
# wc=1
# for i in name:
#     cc+=1
#     print (cc)
# F=open('Test.txt',"r")
# F=open('test.txt')
# F.read()

import random
print("Number guessing Challenge")
number = random.radint(1,9)
chances=0
print("guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("Enter your guess:-"))

    if guess == number:
        print("Congratulations You Won!")
        break
    elif guess < number:
        print ("Your guess was too low: Guess a higher number", guess)

    else:
        print("Your guess was too high: Guess a number lower", guess)

        chances +=1

    If not chances < 5:
        print("You lost! The number is", number)