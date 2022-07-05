import random


class MineSweeper():

    def __init__(self, row=10, col=10, NO_mine=10):
        self.row = col
        self.col = row
        self.No_mine = NO_mine
        self.bomb_cells = []
        self.list = [['0' for i in range(self.col)] for j in range(self.row)]
        self.board = [["x" for i in range(self.col)] for j in range(self.row)]

    def RandomMine(self):
        counter = 0
        while True:
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.col - 1)

            if self.list[x][y] == '0':
                self.list[x][y] = "b"
                self.bomb_cells.append([x, y])

                counter += 1

            if counter >= self.No_mine:
                break

    def ValueAdjacency(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    row = x - i
                    col = y - j
                    if 0 <= row < self.row and 0 <= col < self.col:
                        if self.list[row][col] != "b":
                            self.list[row][col] = str(int(self.list[row][col]) + 1)

    def DeclareAdjacency(self):
        for i in self.bomb_cells:
            self.ValueAdjacency(i[0], i[1])

    def click(self, x, y):
        if self.list[x][y] == "b":
            pass

        elif self.list[x][y] == '0':
            self.list[x][y] = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        row = x - i
                        col = y - j
                        if 0 <= row < self.row and 0 <= col < self.col:
                            self.click(row, col)
        else:
            self.board[x][y] = str(self.list[x][y])

    def points(self):
        pts = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] != 'x':
                    pts += 1
        return pts


if "__main__" == __name__:
    Game = MineSweeper()
    Game.RandomMine()
    Game.DeclareAdjacency()

    while True:
        for i in Game.board:
            print(i)

        x = input("choose row :")
        y = input("choose col :")

        x, y = int(x), int(y)

        if Game.list[x][y] == "b":
            Game.board[x][y] = "b"
            for i in Game.board:
                print(i)
            print("game over")
            break

        elif Game.board[x][y] != "x":
            print("choose a unknown cell")
        else:
            Game.click(x, y)
            if Game.points() >= 90:
                print("win")
                break
