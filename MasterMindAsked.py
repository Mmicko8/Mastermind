# The definition of ALL_COLORS is repeated here. That repetition can
# be avoided, but it would lead us to far at this point.
from random import randint
ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")
NUMBER_OF_CIRCLES = 4


def get_nb_black_white_matches(given, guess):
    """ Returns the number of black and white matches of the guessed
    combination with respect to the given combination. The first
    element in the resulting tuple reflects the number of correct colors
    on their positions (black matches). The second element reflects
    the number of correct colors not on their position (white matches)."""

    correcte_positie = 0
    correcte_kleur = 0
    current_index = 0

    for color in ALL_COLORS:
        aantal_random = given.count(color)
        aantal_guess = guess.count(color)

        if aantal_random >= aantal_guess:   #GEBRUIK min() functie
            correcte_kleur += aantal_guess
        elif aantal_random < aantal_guess:
            correcte_kleur += aantal_random

    while current_index < NUMBER_OF_CIRCLES:
        if guess[current_index] == given[current_index]:
            correcte_positie += 1
            correcte_kleur -= 1
        current_index += 1

    return((correcte_positie,correcte_kleur))


assert get_nb_black_white_matches(["red", "yellow", "yellow", "blue"], ["blue", "yellow", "blue", "yellow"]) == (1, 2)
assert get_nb_black_white_matches(["blue", "yellow", "red", "blue"], ["blue", "yellow", "blue", "yellow"]) == (2, 1)


def create_combination(nb_elements):
    """ Returns a random combination involving the number of elements."""
    combinatie_kleuren = []

    while nb_elements > 0:
        a = randint(0,len(ALL_COLORS)-1)
        combinatie_kleuren.append(ALL_COLORS[a])
        nb_elements -= 1

    return combinatie_kleuren

# ! on the board, each row will consist of 4 circles representing 1 guess
# ! in total 10 rows should be drawn (as the user is given 10 guesses)
# ! You can create a circle by using the function:
# !     canvas.create_oval(x0, y0, x1, y1)
# ! It takes two pairs of coordinates: the top left and bottom right
# ! corners of the bounding rectangle. The (0,0) point is located in the
# ! top left corner of the canvas. We assume that each bounding square has
# ! a size of 30x30 and that all the circles are separated by 10 pixels
# ! from each other, and from the border (see picture in assignment).
# ! For example, the method call (with actual parameters) that generates
# ! the second circle of the third guess will look like:
# !         canvas.create_oval(50, 90, 80, 120)
# ! Later on in the program we modify the ovals to change color depending on
# ! the color that is selected by the person playing.
# ! In order to easily retrieve the correct oval, we expect that the function
# ! you implement here returns a nested list (i.e. a matrix) of
# ! the following form:
# !         [[circle1_guess1, circle2_guess1, ...],
# !          [circle1_guess2, ...],
# !          ...,
# !          [circle4_guess10]]
# ! The second circle of the third guess would for example be stored at:
# !          ovals[2][1] = canvas.create_oval(50, 90, 80, 120)
# ! Instead of approaching the nested list as a matrix, you can also
# ! treat it as a list of lists
# !          e.g. ovals[2].append(...)
# ! Note that the method create_oval has an implementation that
# ! takes 5 parameters. The fifth parameter has name 'fill' and allows
# ! you to assign a color (as a string) to it.
# ! Make sure that all the circles you draw get the fill color "grey".



def any_color_in_combination(colors, given):
    """ Returns true if at least one color in colors is part of the
    given combination. False otherwise."""

    index = 0
    for color in colors:
        if given.count(color) > 0:  ##Gebruik if color in return True en zo niet return False.
            return True
        else:
            index += 1
    return False


assert any_color_in_combination(['blue', 'green', 'red', 'yellow'], ['green', 'blue', 'red', 'yellow'])
assert not any_color_in_combination(['white', 'white', 'purple', 'white'], ['green', 'blue', 'red', 'yellow'])
assert any_color_in_combination(['blue'], ['red','white', 'blue'])


def all_colors_in_combination(colors, given):
    """ Returns true if all the colors in colors are part of the
    given combination. False otherwise."""

    correcte_kleur = 0

    for color in colors:
        aantal_colors = colors.count(color)
        aantal_given = given.count(color)

        if aantal_given >= aantal_colors:
            correcte_kleur += aantal_colors
        elif aantal_given < aantal_colors:
            correcte_kleur += aantal_given

    if correcte_kleur == len(colors):
        return True


assert all_colors_in_combination(['blue', 'green', 'red', 'yellow'], ['green', 'blue', 'red', 'yellow'])
assert not all_colors_in_combination(['blue', 'green', 'red', 'yellow'], ['green', 'blue', 'red', 'purple'])


def is_sublist_of(sublist, given):
    """ Returns whether the sublist is part of the given combination.
    The order of the sublist must also correspond to the order of the
    corresponding part in the given combination."""

    for i in range(0,len(given)-len(sublist)+1):
        if given[i:i+len(sublist)] == sublist:
            return True
        # else:
        #     i += 1
    return False


assert is_sublist_of(['blue', 'green'], ['red','blue', 'green', 'red', 'yellow'])
assert not is_sublist_of(['green', 'blue'], ['blue', 'green', 'red', 'yellow'])
assert is_sublist_of(['red', 'yellow'], ['red','blue', 'green', 'red', 'yellow'])
assert is_sublist_of(['yellow'], ['red','blue', 'green', 'red', 'yellow'])

