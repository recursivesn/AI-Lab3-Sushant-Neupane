import random

ROWS = 8
COLS = 8

class Environment:
    def __init__(self):
        self.grid = [['dirty' if random.random() < 0.3 else 'clean' for _ in range(COLS)] for _ in range(ROWS)]

    def is_dirty(self, x, y):
        return self.grid[x][y] == 'dirty'

    def clean(self, x, y):
        self.grid[x][y] = 'clean'

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
        print()

    def any_dirty_left(self):
        return any('dirty' in row for row in self.grid)


class UtilityBasedVacuumAgent:
    def __init__(self, env):
        self.env = env
        self.x = 0
        self.y = 0

    def utility(self, x, y):
        """Higher utility for dirty tiles that are closer."""
        distance = abs(self.x - x) + abs(self.y - y)
        if self.env.is_dirty(x, y):
            return 100 - distance  # prioritize dirty tiles closer to agent
        return -1  # no utility for clean tiles

    def find_best_tile(self):
        best_score = -1
        best_pos = None
        for i in range(ROWS):
            for j in range(COLS):
                score = self.utility(i, j)
                if score > best_score:
                    best_score = score
                    best_pos = (i, j)
        return best_pos

    def move_to(self, x, y):
        print(f"Moving from ({self.x},{self.y}) to ({x},{y})")
        self.x = x
        self.y = y

    def clean(self):
        if self.env.is_dirty(self.x, self.y):
            print(f"Cleaning ({self.x},{self.y})")
            self.env.clean(self.x, self.y)
        else:
            print(f"({self.x},{self.y}) already clean.")

    def run(self):
        while self.env.any_dirty_left():
            target = self.find_best_tile()
            if target:
                self.move_to(*target)
                self.clean()
            else:
                break


env = Environment()
agent = UtilityBasedVacuumAgent(env)

print("Initial Environment:")
env.display()

agent.run()

print("Final Environment:")
env.display()
