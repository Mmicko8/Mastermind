from MasterMindAsked import *
from random import randint
from sense_hat import SenseHat

ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")
E = (0,0,0)

R = (204,0,0)
B = (0,0,204)
G = (0,204,0)
W = (200,200,200)
Y = (204,204,0)
O = (255,128,0)

matrix = [E]*64
pogingen = 0
combinatie = create_combination(4)
print(combinatie)



while pogingen < 8: # and black != 4:

    kleuren = (input('Geef kleuren: '))
    print(kleuren)
    for i in range(0,4):
        matrix[i+pogingen*8] = kleuren[i]
    sense.set_pixels(matrix)

    white, black = get_nb_black_white_matches(combinatie, kleuren)

    if black == 4:
        sense.show_message("You Win!  You Win!", text_colour=[255, 0, 0])

    pogingen += 1
    if pogingen == 8:
        sense.show_message("You Lose!  You Lose!", text_colour=[255, 0, 0])

