from tkinter import (Button,
                     Canvas,
                     FLAT,
                     NW,
                     Tk,
                     Label,
                     messagebox)

import MasterMindAsked
from random import randint


random_combination = []

current_move = 0
guess_combination = []
canvas = ""
ovals = []
matching_position_label = ""
correct_color_label = ""
used = None





# def check_combination():
#
#     """
#       Check the current guess combination.
#       If the guess combination is complete, the method increments the
#       number of moves, it displays the number of correct colors on
#       their position and the number of correct colors not on their
#       position in the user interface, and it cleans the guess combination.
#       If the guess combination is not complete, the method displays
#       an error message.
#     """
#
#     global current_move, guess_combination
#
#     # check if a complete combination is provided
#     if len(guess_combination) < NUMBER_OF_CIRCLES:
#         messagebox.showerror("Error!", "Please fill in a complete combo before hitting the 'Check' button!")
#     else:
#         current_move = current_move + 1
#         nb_black_white_matches = MasterMindAsked.get_nb_black_white_matches(random_combination, guess_combination)
#
#         # print nb_black_white_matches
#         matching_position_label["text"] = str(nb_black_white_matches[0])
#         correct_color_label["text"] = str(nb_black_white_matches[1])
#         if nb_black_white_matches[0] == NUMBER_OF_CIRCLES:
#             messagebox.showinfo("Congratulations", "You have won the game")
#             root.destroy()
#         else:
#             check_game_over()
#             guess_combination = []


# def check_game_over():
#
#     """
#       Display a message that the game is over, if the number of moves
#       has reached the maximum number of moves.
#     """
#
#     global current_move
#
#     if current_move == MAX_NUMBER_OF_MOVES:
#         game_over_message = "Game Over! You have lost the game."
#         solution = ", ".join(str(x) for x in random_combination)
#         solution_message = "The correct combination was:\n" + solution
#         ending_message = game_over_message + "\n" + solution_message
#         messagebox.showinfo("Game over", ending_message)
#         root.destroy()


# color callback function



random_combination = MasterMindAsked.create_combination(NUMBER_OF_CIRCLES)


# def is_sublist(sublist = None, given = random_combination):
#     """ Returns whether the sublist is part of the given combination.
#     The order of the sublist must also correspond to the order of the
#     corresponding part in the given combination."""
#
#     global guess_combination
#     sublist = guess_combination
#
#     if len(sublist) == 0:
#         messagebox.showerror('ERROR 404', "Sublist not found.")
#
#     else:
#         boolean = False
#         for i in range(0,len(given)-len(sublist)+1):
#             if given[i:i+len(sublist)] == sublist:
#                 boolean = True
#             else:
#                 i += 1
#
#         if boolean:
#             messagebox.showinfo('Sublist',"The sublist is correct.")
#         else:
#             messagebox.showinfo('Sublist',"The sublist is false.")
#
#         for x in range(NUMBER_OF_CIRCLES):
#             canvas.itemconfig(ovals[current_move][x],fill= 'light grey')
#         guess_combination = []
#
#
# def hint(combinatie = random_combination):
#     ''' Gives away the position of one of the 4 colors from random_combination.
#         However this function can only be used once per game. '''
#     global used
#     if not used:
#         index = randint(0, NUMBER_OF_CIRCLES - 1)
#         result = (combinatie[index],f'position: {index+1}')
#         messagebox.showinfo('Hint', result)
#         used = True
#
#     else:
#         messagebox.showerror('ERROR', 'Hint has already been used this game.')


root = Tk()
draw_board(root)
root.mainloop()
