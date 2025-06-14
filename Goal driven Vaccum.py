import random

# Grid size
ROWS = 8
COLS = 8

# Represent the environment
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


# Goal-driven vacuum agent
class GoalDrivenVacuumAgent:
    def __init__(self, env):
        self.env = env
        self.x = 0
        self.y = 0

    def find_next_dirty(self):
        for i in range(ROWS):
            for j in range(COLS):
                if self.env.is_dirty(i, j):
                    return (i, j)
        return None

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
            target = self.find_next_dirty()
            if target:
                self.move_to(*target)
                self.clean()
            else:
                break


# Main program
env = Environment()
agent = GoalDrivenVacuumAgent(env)

print("Initial Environment:")
env.display()

agent.run()

print("Final Environment:")
env.display()
