import random

class Basketball:
    def __init__(self):
        self.blocks = 0
        self.shots = 0
        self.scored = False

    def getPlayingBoard(self):
        playingBoard = []
        rowResult = []
        defenderPos = random.randint(3, 5)
        for row in range(8):
            for column in range(9):
                if row == 0:  # handle first row with Basket
                    if column != 4:
                        rowResult.append("_")
                    else:
                        rowResult.append("O")
                elif row == 1:
                    if column != defenderPos:
                        rowResult.append("_")
                    else:
                        rowResult.append("D")
                elif row == 7:
                    if column != 4:
                        rowResult.append("_")
                    else:
                        rowResult.append("P")
                else:
                    rowResult.append("_")
            playingBoard.append(rowResult)
            rowResult = []

        return playingBoard
    
    def renderPlayingBoard(self):
        _ = ""
        for row in self.playingBoard:
            for char in row:
                _ += char
            print(_)
            _ = ""

    def getDefenderPos(self) -> list:
        rowNum = 0
        columnNum = 0
        for row in self.playingBoard:
            columnNum = 0
            for column in row:
                if column == "D":
                    return [rowNum, columnNum]
                columnNum += 1
            rowNum += 1

    def getPlayerPos(self) -> list:
        rowNum = 0
        columnNum = 0
        for row in self.playingBoard:
            columnNum = 0
            for column in row:
                if column == "P":
                    return [rowNum, columnNum]
                columnNum += 1
            rowNum += 1

    def calculateMistake(self) -> bool:
        _ = random.randint(0, 10)

        if _ > self.difficulty*self.mistakes:
            self.mistakes += 1
            return True
        
        return False

    def getDefenderMove(self) -> int:
        mistake = self.calculateMistake()
        if mistake == True:
            if self.playerPos[1] == self.defenderPos[1]:
                return random.randint(-1, 1)
            elif self.playerPos[1] < self.defenderPos[1]:
                return random.randint(-1, 0)
            elif self.playerPos[1] > self.defenderPos[1]:
                return random.randint(0, 1)
        else:
            if self.playerPos[1] == self.defenderPos[1]:
                return 0
            elif self.playerPos[1] < self.defenderPos[1]:
                return -1
            elif self.playerPos[1] > self.defenderPos[1]:
                return 1
        

    def updatePlayingBoard(self, move):
        self.playingBoard[self.playerPos[0]][self.playerPos[1]] = "_"
        self.playingBoard[self.defenderPos[0]][self.defenderPos[1]] = "_"
        self.playerPos[0] -= 1
        self.playerPos[1] += move
        
        bestMove = self.getDefenderMove()
        if random.randint(0, 1) != 1:
            self.defenderPos[0] += 1
        self.defenderPos[1] += bestMove

        self.playingBoard[self.playerPos[0]][self.playerPos[1]] = "P"
        self.playingBoard[self.defenderPos[0]][self.defenderPos[1]] = "D"

        self.renderPlayingBoard()

        if self.playerPos == self.defenderPos:
            return True
        if self.playerPos[0] == 1:
            self.scored = True
            return True 
        
        return False
                    

        

        
        

    def play(self, difficulty: int):
        self.mistakes = 1
        self.difficulty = difficulty
        self.playingBoard = self.getPlayingBoard()
        self.renderPlayingBoard()

        while self.scored == False:
            self.defenderPos = self.getDefenderPos()
            self.playerPos = self.getPlayerPos()
            move = input("Enter your move (left/forward/right): ")
            if move == "left":
                move = -1
            elif move == "forward":
                move = 0
            elif move == "right":
                move = 1
            else:
                print("Invalid move")
                continue

            
            end = self.updatePlayingBoard(move)
            if end:
                if self.scored:
                    print("You won!")
                    break
                else:
                    print("You lost!")
                    break



basket = Basketball()
basket.play(2)