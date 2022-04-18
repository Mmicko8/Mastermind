from tkinter import (messagebox)
from Board import Board
from random import randint


# noinspection PyMethodMayBeStatic
class Game:
    NUMBER_OF_CIRCLES = 4
    MAX_NUMBER_OF_MOVES = 10

    def __init__(self, root):
        self.board = Board(self.NUMBER_OF_CIRCLES, self.MAX_NUMBER_OF_MOVES, self)
        self.random_combination = self.create_combination()  # todo check if correct
        self.current_move = 0
        self.guess_combination = []
        self.hint_used = False
        self.root = root

    def get_nb_black_white_matches(self, given, guess):
        """ Returns the number of black and white matches of the guessed
        combination with respect to the given combination. The first
        element in the resulting tuple reflects the number of correct colors
        on their positions (black matches). The second element reflects
        the number of correct colors not on their position (white matches)."""
        # TODO translate to English
        correcte_positie = 0
        correcte_kleur = 0
        current_index = 0

        for color in self.board.ALL_COLORS:
            aantal_random = given.count(color)
            aantal_guess = guess.count(color)

            if aantal_random >= aantal_guess:  # GEBRUIK min() functie
                correcte_kleur += aantal_guess
            elif aantal_random < aantal_guess:
                correcte_kleur += aantal_random

        while current_index < self.NUMBER_OF_CIRCLES:
            if guess[current_index] == given[current_index]:
                correcte_positie += 1
                correcte_kleur -= 1
            current_index += 1

        return correcte_positie, correcte_kleur

    def check_combination(self):

        """
          Check the current guess combination.
          If the guess combination is complete, the method increments the
          number of moves, it displays the number of correct colors on
          their position and the number of correct colors not on their
          position in the user interface, and it cleans the guess combination.
          If the guess combination is not complete, the method displays
          an error message.
        """
        print(self.guess_combination)
        print(self.random_combination)
        # check if a complete combination is provided
        if len(self.guess_combination) < self.NUMBER_OF_CIRCLES:
            messagebox.showerror("Error!", "Please fill in a complete combo before hitting the 'Check' button!")
        else:
            self.current_move = self.current_move + 1
            nb_black_white_matches = self.get_nb_black_white_matches(self.random_combination, self.guess_combination)
            print(nb_black_white_matches)

            # print nb_black_white_matches
            self.board.matching_position_label["text"] = str(nb_black_white_matches[0])  # todo check if correct
            self.board.correct_color_label["text"] = str(nb_black_white_matches[1])
            if nb_black_white_matches[0] == self.NUMBER_OF_CIRCLES:
                messagebox.showinfo("Congratulations", "You have won the game")
                self.root.destroy()
            else:
                self.check_game_over()
                self.guess_combination = []

    def any_color_in_combination(self, colors, given):
        """ Returns true if at least one color in colors is part of the
        given combination. False otherwise."""

        index = 0
        for color in colors:
            if given.count(color) > 0:  # Gebruik if color in return True en zo niet return False.
                return True
            else:
                index += 1
        return False

    def all_colors_in_combination(self, colors, given):
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

    def create_combination(self):
        """ Returns a random combination involving the number of elements."""
        combinatie_kleuren = []

        i = self.NUMBER_OF_CIRCLES
        while i > 0:
            a = randint(0, len(self.board.ALL_COLORS) - 1)
            combinatie_kleuren.append(self.board.ALL_COLORS[a])
            i -= 1

        return combinatie_kleuren

    def is_sublist(self, sublist=None, given=None):
        """ Returns whether the sublist is part of the given combination.
        The order of the sublist must also correspond to the order of the
        corresponding part in the given combination."""

        if given is None:
            given = self.random_combination
        sublist = self.guess_combination

        if len(sublist) == 0:
            messagebox.showerror('ERROR 404', "Sublist not found.")

        else:
            boolean = False
            for i in range(0, len(given) - len(sublist) + 1):
                if given[i:i + len(sublist)] == sublist:
                    boolean = True
                else:
                    i += 1

            if boolean:
                messagebox.showinfo('Sublist', "The sublist is correct.")
            else:
                messagebox.showinfo('Sublist', "The sublist is false.")

            for x in range(self.NUMBER_OF_CIRCLES):
                self.board.canvas.itemconfig(self.board.ovals[self.current_move][x],
                                             fill='light grey')  # todo make a bit cleaner
            self.guess_combination = []

    def is_sublist_of(self, sublist, given):
        """ Returns whether the sublist is part of the given combination.
        The order of the sublist must also correspond to the order of the
        corresponding part in the given combination."""

        for i in range(0, len(given) - len(sublist) + 1):
            if given[i:i + len(sublist)] == sublist:
                return True
            # else:
            #     i += 1
        return False

    def hint(self, combinatie=None):
        """ Gives away the position of one of the 4 colors from random_combination.
            However this function can only be used once per game. """

        if combinatie is None:
            combinatie = self.random_combination

        if not self.hint_used:
            index = randint(0, self.NUMBER_OF_CIRCLES - 1)
            result = (combinatie[index], f'position: {index + 1}')
            messagebox.showinfo('Hint', result)  # TODO
            self.hint_used = True

        else:
            messagebox.showerror('ERROR', 'Hint has already been used this game.')

    def check_game_over(self):

        """
          Display a message that the game is over, if the number of moves
          has reached the maximum number of moves.
        """

        if self.current_move == self.MAX_NUMBER_OF_MOVES:
            game_over_message = "Game Over! You have lost the game."
            solution = ", ".join(str(x) for x in self.random_combination)
            solution_message = "The correct combination was:\n" + solution
            ending_message = game_over_message + "\n" + solution_message
            messagebox.showinfo("Game over", ending_message)
            self.root.destroy()
