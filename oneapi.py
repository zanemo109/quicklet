from define import *

words = input('Input words as a comma separated list: ').split(',')
definitions = definitions_only(words).split('<')
cards = list(zip(words, definitions))

for card in cards:
    print(f'{card[0]}    {card[1]}')



    


