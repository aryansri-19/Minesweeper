import random


#Board Container
class Board:
    #Constructor
    def __init__(self, num_mines, side):
        self.num_mines = num_mines
        self.side = side
        self.field = [[' _ ' for i in range(self.side)] for j in range(self.side)] #playing field
        self.used_spots = set(tuple())
        self.lost = False
        self.mines = set(tuple())
        self.neighbours = 0 #counter for checking safe spots

    #printing fucntion    
    def printBoard(self):
        print("  1  2  3  4  5  6  7  8  9  10")
        for i in range(self.side):
            print("|", end="")
            for j in range(self.side):
                print(f"{self.field[i][j]}", end="")
            print(f"| {i+1}")

    def generate_mines(self):
        while len(self.mines) != self.side:
            mine = random.randrange(self.side, self.side**2)
            row = mine//self.side
            column = mine%self.side
            self.mines.add((row, column))

    #asking for guess from the user
    def guess(self):
        x, y = [int(x) for x in input("Enter the row and column for the safe spot: ").split()]
        if self.validationCheck(x, y):
            print("Wrong/Used spot, try again...")
            return
        elif self.mineCheck(x, y):
            pass
        else:
            board.safeCheck(x-1, y-1)
            self.used_spots.add((x-1, y-1))
        board.printBoard()

    #checking if coordinates are appropriate
    def validationCheck(self, row, column):
        if row > self.side or row < 1 or column > self.side or column < 1 or (row, column) in self.used_spots:
            return True
        return False
    
    #checking neighbours
    def safeCheck(self, row, column):
        if (row, column) in self.mines or (row, column) in self.used_spots or self.neighbours == self.side:
            return
        counter = 0
        for (x, y) in self.mines:
            if (row-1, column) == (x,y):
                counter += 1
            if (row+1, column) == (x,y):
                counter += 1
            if (row, column+1) == (x,y):
                counter += 1
            if (row, column-1) == (x,y):
                counter += 1
            self.field[row][column] = f' {counter} '
        self.used_spots.add((row, column))
        self.neighbours += 1
        mining = random.randint(0,4)
        if mining == 0 and row!=0:
            self.safeCheck(row-1, column)
        if mining == 1 and row!=self.side-1:
            self.safeCheck(row+1, column)
        if mining == 2 and column!=0:
            self.safeCheck(row, column-1)
        if mining == 3 and column!=self.side-1:
            self.safeCheck(row, column+1)
    
    def mineCheck(self, x, y):
        if (x-1, y-1) in self.mines:
            self.lost = True
            for x, y in self.mines:
                self.field[x][y] = ' # '
            return True
        return False

board = Board(20, 20)
board.generate_mines()

#main function
def main():
    board.printBoard()
    while not board.lost:
        print("\n---------------------------------------------------\n")
        board.guess()
        board.neighbours = 0
        if len(board.used_spots)==board.side**2-board.side:
            print("WOW! Congratulations, you won the game!")
            return

if __name__ == '__main__':
    main()
    if board.lost:
        print("\nBOOM! You stepped on a mine. Game Over!")
