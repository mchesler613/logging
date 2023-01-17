import random
from logger import Logger
from typing import List


class TicTacToe:
    """
    This class is a representation of a 2-player TicTacToe game
    between you and the computer.
    An instance of this class logs selected information in a log file located
    at 'logs/tictactoe.log'.
    """

    quit_prompt = "Type q to quit"
    grid = [x for x in range(10)]
    markers = ["x", "o"]
    you_win_msg = "You won!"
    i_win_msg = "I won!"
    tie_msg = "It's a tie!"

    def __init__(self, name: str) -> None:
        self.name = name
        self.logger = Logger(name)

    def log(self, message: str) -> None:
        """
        Wrapper function for self.logger.log
        """
        self.logger.log(message)

    def reset(self):
        self.updated_grid = self.grid.copy()
        self.available_indices = [x for x in range(1, 10)]
        self.player_symbol = random.choice(self.markers)
        self.game_symbol = (
            self.markers[0]
            if (self.player_symbol == self.markers[1])
            else self.markers[1]
        )

    def display(self, message: str = None) -> None:
        rows = 3
        index = 1
        for row in range(1, rows + 1):
            row_values = (
                f"{self.updated_grid[index]} "
                f"{self.updated_grid[index+1]} "
                f"{self.updated_grid[index+2]}"
            )
            print(row_values)
            self.log(row_values)
            index += 3
        self.log("")
        if message:
            print(message)
            self.log(message)

    def run(self):
        """
        This method is called to start a game with the correct prompts
        and display
        """
        self.reset()
        answer = None
        instruction = "Enter a number:"
        while answer != "q":
            self.display()
            self.log(f"You are {self.player_symbol}")

            formatted_question = f"{self.quit_prompt} or {instruction} "

            # ask question, log answer
            answer = input(formatted_question)

            try:
                index = int(answer)
            except ValueError:
                # ignore non-number response
                continue

            # evaluate player response
            if index in self.available_indices:
                self.updated_grid[index] = self.player_symbol
                # did the player win?
                if self.three_in_a_row(index, self.player_symbol):
                    self.display(self.you_win_msg)
                    break
                self.available_indices.remove(index)

                # game responds accordingly based on the available positions
                if self.available_indices:
                    # the game picks a random available position and
                    # updates the grid
                    game_index = random.choice(self.available_indices)
                    self.updated_grid[game_index] = self.game_symbol

                    # did the computer win?
                    if self.three_in_a_row(game_index, self.game_symbol):
                        self.display(self.i_win_msg)
                        break
                    self.available_indices.remove(game_index)
                else:
                    print(self.tie_msg)
                    break

    def three_in_a_row(
        self,
        index: int,
        symbol: str,
    ) -> bool:
        """
        This method evaluates if a 'symbol' at 'index' contributes to a winning
        row by returning True or False
        """
        # A list of pre-programmed evaluations based on position
        # Does this position, index, have two neighbors with same symbol?
        evaluations = {
            1: (
                True
                if (self.evaluate_neighbors(index, [2, 3], symbol))
                or (self.evaluate_neighbors(index, [4, 5], symbol))
                or (self.evaluate_neighbors(index, [5, 9], symbol))
                else False
            ),
            2: (
                True
                if (self.evaluate_neighbors(index, [1, 3], symbol))
                or (self.evaluate_neighbors(index, [5, 8], symbol))
                else False
            ),
            3: (
                True
                if (self.evaluate_neighbors(index, [1, 2], symbol))
                or (self.evaluate_neighbors(index, [5, 7], symbol))
                or (self.evaluate_neighbors(index, [6, 9], symbol))
                else False
            ),
            4: (
                True
                if (self.evaluate_neighbors(index, [1, 7], symbol))
                or (self.evaluate_neighbors(index, [5, 6], symbol))
                else False
            ),
            5: (
                True
                if (self.evaluate_neighbors(index, [2, 8], symbol))
                or (self.evaluate_neighbors(index, [3, 7], symbol))
                or (self.evaluate_neighbors(index, [1, 9], symbol))
                or (self.evaluate_neighbors(index, [4, 6], symbol))
                else False
            ),
            6: (
                True
                if (self.evaluate_neighbors(index, [3, 9], symbol))
                or (self.evaluate_neighbors(index, [4, 5], symbol))
                else False
            ),
            7: (
                True
                if (self.evaluate_neighbors(index, [1, 4], symbol))
                or (self.evaluate_neighbors(index, [3, 5], symbol))
                or (self.evaluate_neighbors(index, [8, 9], symbol))
                else False
            ),
            8: (
                True
                if (self.evaluate_neighbors(index, [2, 5], symbol))
                or (self.evaluate_neighbors(index, [7, 9], symbol))
                else False
            ),
            9: (
                True
                if (self.evaluate_neighbors(index, [1, 5], symbol))
                or (self.evaluate_neighbors(index, [3, 6], symbol))
                or (self.evaluate_neighbors(index, [7, 8], symbol))
                else False
            ),
        }
        return evaluations[index]

    def evaluate_neighbors(
        self,
        index: int,
        neighbors: List[int],
        symbol: str,
    ) -> bool:
        """
        This is the crux of the tictactoe game. It evaluates if a symbol's
        neighbors, either horizontally or vertically or diagonally also have
        the same symbol
        """
        assert len(neighbors) == 2
        return (
            True
            if (self.updated_grid[neighbors[0]] == symbol)
            and (self.updated_grid[neighbors[1]] == symbol)
            else False
        )
