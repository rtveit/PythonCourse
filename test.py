import random, time, math , os,  sys

total = 0 
for num in range (101):
	total = total + num
print (total)



total = 0               #(1)
for num in range(101):  #(2)
   total = total + num  #(3)
print(total)            #(4)



import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')






1
true and false
2
and, or, not, 
4
true   and  false = false
false = false
(5 > 4) or (3 == 5) = true
not ((5 > 4) or (3 == 5))
      true   or  false = false
(True and True) and (True == False) = false
(not False) or (not True)  = true

5
> < != == 
6
What is the difference between the equal to operator and the assignment operator?
7
Explain what a condition is and where you would use one.
8 
spam = 100
if spam == 10:            
 print('eggs')
elif spam < 5:          
 print('bacon')
else:                  
 print('ham')
   



9 
prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings!

mitt første forsøk ... :-D
if spam == 1:
 print("Hello")
 if spam == 2:
   print("Howady")
  if spam == 3:
   print "Greetings")
   
  spam = 3 
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

	
	
def hello():
 print('Howdy!')
 print('Howdy!!!')
 print('Hello there.')
 
hello()
hello()
hello()

def hello(name):
 print('Hello ' + name)

hello('Robert')
hello('Marie')



import random
def getAnswer(answerNumber):
 if answerNumber == 1:
  return 'It is certain'
 elif answerNumber == 2:
  return 'It is decidedly so'
 elif answerNumber == 3:
  return 'Yes'
 elif answerNumber == 4:
  return 'Reply hazy try again'
 elif answerNumber == 5:
  return 'Ask again later'
 elif answerNumber == 6:
  return 'Concentrate and ask again'
 elif answerNumber == 7:
  return 'My reply is no'
 elif answerNumber == 8:
  return 'Outlook not so good'
 elif answerNumber == 9:
  return 'Very doubtful'

r = random.randint(1, 9)     er det samme som 
fortune = getAnswer(r)							print(getAnswer(random.randint(1, 9)))
print(fortune)


def spam():
 global eggs
 eggs = 'spam' # this is the global

def bacon():
 eggs = 'bacon' # this is a local
def ham():
 print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)

Guessing game
--------------

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
 print('Take a guess.')
 guess = int(input())

if guess < secretNumber:
 print('Your guess is too low.')
elif guess > secretNumber:
 print('Your guess is too high.')
else:
 break    # This condition is the correct guess!

if guess == secretNumber:
 print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
 print('Nope. The number I was thinking of was ' + str(secretNumber))




