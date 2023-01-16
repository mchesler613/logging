from busybody import Busybody
from tictactoe import TicTacToe

choices = {
    "1": "Busybody",
    "2": "TicTacToe",
    "q": "quit",
}


busybody_game = Busybody("busybody")
tictactoe_game = TicTacToe("tictactoe")


def main():
    answer = None

    while answer != "q":
        for choice in choices:
            print(choice, choices[choice])
        answer = input("Pick a game: ")
        if answer == "1":
            global busybody_game
            busybody_game.run()
        elif answer == "2":
            global tictactoe_game
            tictactoe_game.run()
        elif answer == "q":
            break

    print("Goodbye")


if __name__ == "__main__":
    main()
