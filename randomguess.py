import random

guesses_made = 0

name = raw_input('Hello! What is your name?\n')

number = random.randint(1, 20)
print 'Hi, {0}, Guess my number between 1 and 20.'.format(name)

while guesses_made < 6:

    guess = int(raw_input('Guess my number: '))

    guesses_made += 1

    if guess < number:
        print 'Your guess is too low.'

    if guess > number:
        print 'Your guess is too high.'

    if guess == number:
        break

if guess == number:
    print 'Good job, {0}! That took {1} guesses!'.format(name, guesses_made)
else:
    print ' You lose! the number was, {0}'.format(number)
