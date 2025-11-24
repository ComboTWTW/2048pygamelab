import random

class Game2048:
    def __init__(self):
        self.size = 4
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.score = 0          # <-- ADD THIS LINE
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty = [(r, c) for r in range(self.size) for c in range(self.size)
                 if self.grid[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 2 if random.random() < 0.9 else 4

    # ---- Helper: compress row left ----
    def compress(self, row):
        """Move all non-zero numbers to the left"""
        new_row = [i for i in row if i != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    # ---- Helper: merge row left ----
    def merge(self, row):
        score = 0
        for i in range(self.size - 1):
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2
                row[i+1] = 0
                score += row[i]
        return row, score

    # ---- Move left ----
    def move_left(self):
        moved = False
        total_score = 0
        new_grid = []

        for row in self.grid:
            compressed = self.compress(row)
            merged, score = self.merge(compressed)
            compressed = self.compress(merged)
            new_grid.append(compressed)
            total_score += score

            if compressed != row:
                moved = True

        self.grid = new_grid

        # Add earned score
        if total_score > 0:
            self.score += total_score

        if moved:
            self.add_tile()


    # ---- Move right ----
    def move_right(self):
        self.grid = [row[::-1] for row in self.grid]
        self.move_left()
        self.grid = [row[::-1] for row in self.grid]

    # ---- Move up ----
    def move_up(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.move_left()
        self.grid = list(map(list, zip(*self.grid)))

    # ---- Move down ----
    def move_down(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.move_right()
        self.grid = list(map(list, zip(*self.grid)))

    def can_move(self):
        # If there is at least one empty tile, you can move
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return True

        # Check for horizontal merges
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.grid[r][c] == self.grid[r][c + 1]:
                    return True

        # Check for vertical merges
        for c in range(self.size):
            for r in range(self.size - 1):
                if self.grid[r][c] == self.grid[r + 1][c]:
                    return True

        # No moves left
        return False

