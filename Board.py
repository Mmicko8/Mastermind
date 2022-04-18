from tkinter import (Button,
                     Canvas,
                     FLAT,
                     NW,
                     Label,
                     messagebox)


class Board:
    ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")

    # NUMBER_OF_CIRCLES = 4
    # MAX_NUMBER_OF_MOVES = 10

    def __init__(self, number_of_circles, max_number_of_moves):
        self.canvas = None
        self.ovals = None
        self.matching_position_label = None
        self.correct_color_label = None
        self.number_of_circles = number_of_circles
        self.max_number_of_moves = max_number_of_moves

    def color(self, color_name, current_move, guess_combination):

        """
          Add the given color to the guess combination. The corresponding circle
          in the display is also filled with the color. If the guess combination is
          complete, an error message is displayed.
        """

        if len(guess_combination) == self.number_of_circles:
            messagebox.showerror("Colors are full",
                                 "No more colors allowed, please hit the 'Check' button to check your result")
        else:
            self.canvas.itemconfig(self.ovals[current_move][len(guess_combination)], fill=color_name)
            guess_combination.append(color_name)

    def draw_color_buttons(self, current_move, guess_combination):
        for i in range(len(self.ALL_COLORS)):
            self.canvas.create_window(self.number_of_circles * 50 + 10, 20 + i * 45, anchor=NW,
                                      window=Button(self.canvas,
                                                    command=lambda color_name=self.ALL_COLORS[i]: self.color(
                                                        color_name, current_move, guess_combination),
                                                    width=5,
                                                    text=self.ALL_COLORS[i]))

    def create_empty_circles(self):
        """ Returns a matrix containing grey ovals that are correctly initialized
            at their required location."""
        ovals = []

        for i in range(self.max_number_of_moves):
            ovals.insert(0, [])

        for i in range(self.max_number_of_moves):
            for x in range(self.number_of_circles):
                circle = self.canvas.create_oval(10 + 40 * x, 10 + 40 * i, 40 + 40 * x, 40 + 40 * i,
                                                 fill='light gray')
                ovals[i].append(circle)

        return ovals

    def draw_result_labels(self):
        self.canvas.create_window(50, self.max_number_of_moves * 40 + 30, anchor=NW,
                                  window=Label(self.canvas, text="Correct position: "))

        matching_position_label = Label(self.canvas)
        self.canvas.create_window(200, self.max_number_of_moves * 40 + 30, anchor=NW, window=matching_position_label)

        self.canvas.create_window(50, self.max_number_of_moves * 40 + 60, anchor=NW,
                                  window=Label(self.canvas, text="Correct color: "))

        correct_color_label = Label(self.canvas)
        self.canvas.create_window(200, self.max_number_of_moves * 40 + 60, anchor=NW, window=correct_color_label)

    def draw_submit_button(self):
        submit_button = Button(self.canvas, text="Check", command=check_combination)
        submit_button.configure(width=10, relief=FLAT)
        self.canvas.create_window(50, self.max_number_of_moves * 40 + 90, anchor=NW, window=submit_button)

    def draw_sublist_button(self):
        sublist_button = Button(self.canvas, text="Sublist", command=is_sublist)
        sublist_button.configure(width=10, relief=FLAT)
        self.canvas.create_window(180, self.max_number_of_moves * 40 + 90, anchor=NW, window=sublist_button)

    def draw_hint_button(self):
        hint_button = Button(self.canvas, text="Hint", command=hint)
        hint_button.configure(width=10, relief=FLAT)
        self.canvas.create_window(50, self.max_number_of_moves * 40 + 130, anchor=NW, window=hint_button)

    def draw_quit_button(self, root):
        quit_button = Button(self.canvas, text="Quit", command=root.destroy)
        quit_button.configure(width=10, relief=FLAT)
        self.canvas.create_window(180, self.max_number_of_moves * 40 + 130, anchor=NW, window=quit_button)

    def draw_board(self, root, current_move, guess_combination):
        """
          Create the graphical user interface.
        """

        # provide the title that will be shown in the header
        root.title("Mastermind")

        # canvas will be the main board used for mastermind
        canvas = Canvas(root, bg="white", height=self.max_number_of_moves * 40 + 170,
                        width=self.number_of_circles * 50 + 100)

        # Draw the empty circles representing the guesses
        self.ovals = self.create_empty_circles()

        # Draw a line to separate the circles form the buttons
        canvas.create_line(self.number_of_circles * 50, 10, self.number_of_circles * 50, 400, width=3, fill="black")

        # Draw the color buttons that will be used throughout the game
        self.draw_color_buttons(current_move, guess_combination)

        # Draw the result labels
        # ! matching_position_label and correct_color_label can be used later on
        # ! to show the user the number of correct positions and colors
        # ! (e.g. matching_position_label["text"] = "2")
        self.draw_result_labels()

        # Draw the submit button
        # ! when the user clicks the button,
        # ! the function check_combination is called
        self.draw_submit_button()

        # Draw the sublist button
        # ! when the user clicks the button,
        # ! the function is_sublist is called
        self.draw_sublist_button()

        # Draw the hint button
        # ! when the user clicks the button,
        # ! the function hint is called
        self.draw_hint_button()

        # Draw the quit button
        self.draw_quit_button(root)

        # draw the canvas
        canvas.pack()
