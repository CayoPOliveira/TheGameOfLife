import os
import time
class Cell:
    def __init__(self, initState = True):
        self.state = initState

    def getState(self):
        return self.state

    def swapState(self):
        self.state = not self.state

class TheGameOfLife:
    def __init__(self, size):
        self.size = size
        self.G = [[Cell(False) for i in range(size)] for j in range(size)]
        self.gen = 0

    def swapState(self, x, y):
        self.G[x][y].swapState()

    def getNumberOfGens(self):
        return self.gen

    def initState(self):
        init = TheGameOfLife(self.size)
        [init.swapState(x,y) for x in range(self.size) for y in range(self.size) if self.G[x][y].getState()]
        return init

    def automaton(self):
        Gnext = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                neighborsAlive = 0
                for i in range(-1, 2):
                    if x + i < 0 or x + i >= self.size:
                        continue
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if y + j < 0 or y + j >= size:
                            continue
                        if self.G[x + i][y + j].getState():
                            neighborsAlive += 1
                if self.G[x][y].getState and (neighborsAlive < 2 or neighborsAlive > 3):
                    Gnext[x][y].swapState()
                elif not self.G[x][y].getState() and neighborsAlive != 3:
                    Gnext[x][y].swapState()
        equals = False if len([1 for x in range(self.size) for y in range(self.size) if self.G[x][y].getState() != Gnext[x][y].getState()])!=0 else True
        self.gen += 1
        if not equals:
            self.G = Gnext
        return equals


    def __str__(self):
        grid = ""
        for x in range(self.size):
            for y in range(self.size):
                grid += 'O ' if self.G[x][y].getState() else '- '
            grid += '\n'
        return grid

if __name__ == "__main__":
    size = int(input("Size: "))
    tgol = TheGameOfLife(size)
    random = input("(Y or N) Random State?:")
    if random[0] == 'Y' or random[0] == 'S':
        import random
        num_alives = random.randint(1, size*size)
        xs = random.choices(range(size), k=num_alives)
        ys = random.choices(range(size), k=num_alives)
        for x,y in zip(xs, ys):
            tgol.swapState(x,y)
    else:
        while True:
            x,y = [int(i) for i in input("Alive X and Y: ").split()]
            if x == -1 and y == -1:
                break
            tgol.swapState(x,y)
            print(tgol)

    while True:
        os.system('clear')
        if(tgol.getNumberOfGens() == 0):
            initialState = tgol.initState()
        else:
            print(f"Initial State")
            print(initialState)
        print(f"Gen {tgol.getNumberOfGens()}")
        print(tgol)
        if tgol.automaton():
            break
        time.sleep(2)

    os.system('clear')
    print(f"Initial State")
    print(initialState)
    print(f"Final State in Gen {tgol.getNumberOfGens()}")
    print(tgol)


