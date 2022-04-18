from tkinter import Tk
from Game import Game
from Board import Board


def main():
    root = Tk()
    game = Game(root)
    game.board.draw_board(root, game.current_move, game.guess_combination)
    root.mainloop()


if __name__ == "__main__":
    main()
