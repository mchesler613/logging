from logger import Logger
from typing import List
import random


class TicTacToe():

    quit_prompt = 'Type q to quit'
    grid = [x for x in range(10)]
    markers = ['x', 'o']
    you_win_msg = 'You won!'
    i_win_msg = 'I won!'
    tie_msg = "It's a tie!"

    def __init__(
        self,
        name: str
    ) -> None:
        self.name = name
        self.logger = Logger(name).logger

    def reset(self):
        self.updated_grid = self.grid.copy()
        self.available_indices = [x for x in range(1, 10)]
        self.player_symbol = random.choice(self.markers)
        self.game_symbol = self.markers[0] if (
            self.player_symbol == self.markers[1]
        ) else self.markers[1]

    def display(self):
        rows = 3
        index = 1
        for row in range(1, rows+1):
            row_values = (
                f"{self.updated_grid[index]} "
                f"{self.updated_grid[index+1]} "
                f"{self.updated_grid[index+2]}"
            )
            print(row_values)
            self.logger.info(row_values)
            index += 3
        self.logger.info("")

    def run(self):
        self.reset()
        answer = None
        instruction = "Enter a number:"
        while answer != 'q':
            self.display()
            self.logger.info(f"You are {self.player_symbol}")

            formatted_question = (
                f"{self.quit_prompt} or {instruction} "
            )

            # ask question, log answer
            answer = input(formatted_question)

            try:
                index = int(answer)
            except ValueError:
                continue

            # update grid with symbol
            if index in self.available_indices:
                self.updated_grid[index] = self.player_symbol
                if self.three_in_a_row(index, self.player_symbol):
                    self.display()
                    print(self.you_win_msg)
                    self.logger.info(self.you_win_msg)
                    break
                self.available_indices.remove(index)

                # game responds
                if self.available_indices:
                    game_index = random.choice(self.available_indices)
                    self.updated_grid[game_index] = self.game_symbol
                    if self.three_in_a_row(game_index, self.game_symbol):
                        self.display()
                        print(self.i_win_msg)
                        self.logger.info(self.i_win_msg)
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
        Does this position have two neighbors with same symbol?
        """
        if index == 1:
            # evaluate 2 and 3
            # evaluate 4 and 5
            # evaluate 5 and 9
            return True if (
                self.evaluate_neighbors(index, [2, 3], symbol)
            ) or (
                self.evaluate_neighbors(index, [4, 5], symbol)
            ) or (
                self.evaluate_neighbors(index, [5, 9], symbol)
            ) else False

        if index == 2:
            # evaluate 1 and 3
            # evaluate 5 and 8
            return True if (
                self.evaluate_neighbors(index, [1, 3], symbol)
            ) or (
                self.evaluate_neighbors(index, [5, 8], symbol)
            ) else False

        if index == 3:
            # evaluate 1 and 2
            # evaluate 5 and 7
            # evaluate 6 and 9
            return True if (
                self.evaluate_neighbors(index, [1, 2], symbol)
            ) or (
                self.evaluate_neighbors(index, [5, 7], symbol)
            ) or (
                self.evaluate_neighbors(index, [6, 9], symbol)
            ) else False

        if index == 4:
            # evaluate 1 and 7
            # evaluate 5 and 6
            return True if (
                self.evaluate_neighbors(index, [1, 7], symbol)
            ) or (
                self.evaluate_neighbors(index, [5, 6], symbol)
            ) else False

        if index == 5:
            # evaluate 1 and 9
            # evaluate 2 and 8
            # evaluate 3 and 7
            return True if (
                self.evaluate_neighbors(index, [2, 8], symbol)
            ) or (
                self.evaluate_neighbors(index, [3, 7], symbol)
            ) or (
                self.evaluate_neighbors(index, [1, 9], symbol)
            ) else False

        if index == 6:
            # evaluate 3 and 9
            # evaluate 4 and 5
            return True if (
                self.evaluate_neighbors(index, [3, 9], symbol)
            ) or (
                self.evaluate_neighbors(index, [4, 5], symbol)
            ) else False

        if index == 7:
            # evaluate 1 and 4
            # evaluate 3 and 5
            # evaluate 8 and 9
            return True if (
                self.evaluate_neighbors(index, [1, 4], symbol)
            ) or (
                self.evaluate_neighbors(index, [3, 5], symbol)
            ) or (
                self.evaluate_neighbors(index, [8, 9], symbol)
            ) else False

        if index == 8:
            # evaluate 2 and 5
            # evaluate 7 and 9
            return True if (
                self.evaluate_neighbors(index, [2, 5], symbol)
            ) or (
                self.evaluate_neighbors(index, [7, 9], symbol)
            ) else False

        if index == 9:
            # evaluate 1 and 5
            # evaluate 3 and 6
            # evaluate 7 and 8
            return True if (
                self.evaluate_neighbors(index, [1, 5], symbol)
            ) or (
                self.evaluate_neighbors(index, [3, 6], symbol)
            ) or (
                self.evaluate_neighbors(index, [7, 8], symbol)
            ) else False

    def evaluate_neighbors(
        self,
        index: int,
        neighbors: List[int],
        symbol: str,
    ) -> bool:
        assert len(neighbors) == 2
        return True if (
            self.updated_grid[neighbors[0]] == symbol
        ) and (
            self.updated_grid[neighbors[1]] == symbol
        ) else False

    """
    def __del__(self):
        del self.logger
    """
