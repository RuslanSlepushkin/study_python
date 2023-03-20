import random


rand_num = random.randint(1, 10)
inp_num = int(input("Сhoose number between 1 and 10: "))
if rand_num == inp_num:
    print("You guessed it. It's", rand_num)
else:
    print("You haven't guessed. It's", rand_num)