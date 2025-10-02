# tic_tac_toe.py

import random

# -------------------- Player Classes --------------------

class Player:
    """Base class for players"""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        """To be implemented by subclasses"""
        raise NotImplementedError


class HumanPlayer(Player):
    """Human player interacts via input"""
    def make_move(self, board):
        valid_move = False
        while not valid_move:
            try:
                move = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid input! Choose between 1-9.")
                    continue
                row, col = divmod(move - 1, 3)
                valid_move = board.update((row, col), self.symbol)
                if not valid_move:
                    print("Cell already taken! Try again.")
            except ValueError:
                print("Invalid input! Enter a number between 1-9.")


class ComputerPlayer(Player):
    """Computer chooses moves automatically"""
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")
        available_moves = board.get_empty_cells()
        row, col = random.choice(available_moves)
        board.update((row, col), self.symbol)

# -------------------- Board Class --------------------

class Board:
    """Tic-Tac-Toe board"""
    def __init__(self):
        self._grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\nCurrent Board:")
        print("-------------")
        for row in self._grid:
            print("| " + " | ".join(row) + " |")
            print("-------------")

    def update(self, position, symbol):
        row, col = position
        if self._grid[row][col] == " ":
            self._grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Check rows
        for row in self._grid:
            if all(cell == symbol for cell in row):
                return True
        # Check cols
        for col in range(3):
            if all(self._grid[row][col] == symbol for row in range(3)):
                return True
        # Check diagonals
        if all(self._grid[i][i] == symbol for i in range(3)):
            return True
        if all(self._grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self._grid for cell in row)

    def get_empty_cells(self):
        return [(r, c) for r in range(3) for c in range(3) if self._grid[r][c] == " "]

    def __str__(self):
        """String representation for printing"""
        rows = []
        for row in self._grid:
            rows.append(" | ".join(row))
        return "\n---------\n".join(rows)

# -------------------- Game Class --------------------

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0  # Index of current player

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        print("\n--- Welcome to Tic-Tac-Toe ---")
        self.board.display()

        while True:
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)
            self.board.display()

            if self.board.check_winner(current_player.symbol):
                print(f"\n{current_player.name} ({current_player.symbol}) WINS! 🎉")
                break
            elif self.board.is_full():
                print("\nIt's a DRAW! 🤝")
                break

            self.switch_turns()

# -------------------- Main Program --------------------

def main():
    print("Do you want to play with a friend (1) or vs computer (2)?")
    mode = input("Enter 1 or 2: ")

    if mode == "1":
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        player1 = HumanPlayer(name1, "X")
        player2 = HumanPlayer(name2, "O")

    elif mode == "2":
        name = input("Enter your name: ")
        player1 = HumanPlayer(name, "X")
        player2 = ComputerPlayer("Computer", "O")

    else:
        print("Invalid choice! Exiting...")
        return

    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
