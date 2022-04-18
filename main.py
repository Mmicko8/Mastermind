from tkinter import Tk
from Game import Game
from Board import Board


def main():
    root = Tk()
    game = Game(root)
    game.board.draw_board(root)
    root.mainloop()


if __name__ == "__main__":
    main()
