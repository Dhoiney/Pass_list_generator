from itertools import *

chars = input("Введите все возможные символы\n")

comb_length = input("Введите длину комбинации\n")

with open('pass.txt', 'w') as file_hand:
    for i in combinations_with_replacement(chars, int(comb_length)):
        file_hand.write(''.join(i)+'\n')
