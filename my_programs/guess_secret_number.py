secret_number = 9

guess_count = 1
guess_limit = 3

while guess_count <= guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You win!')
        break

else:
    print('You lose!')

#Note: The usage of WHILE ELSE loop. Just like IF ELSE, ELSE can also be used with WHILE loop.