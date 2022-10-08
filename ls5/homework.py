from random import randint

score = 0
x = randint(1, 10)
y = randint(1, 10)
c1 = int(input(f'{x} + {y} = ?'))

if c1==x+y:
    print("Right")
    score += 1

c1 = int(input(f'{x} * {y} = ?'))

if c1==x*y:
    print("Right")
    score += 1

c1 = int(input(f'{x} - {y} = ?'))

if c1==x-y:
    print("Right")
    score += 1

if score==3:
    print("You win")
else: 
    print("You lose")