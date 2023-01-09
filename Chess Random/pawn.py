import pyautogui
import random
import ctypes
import time

def click():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # Left mouse down
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # Left mouse up

class Pawn():
    def __init__(self, boardPosition, tipe, m, s, color):
        self.mouseDictionary = m
        self.screenshotDictionary = s
        self.boardPosition = boardPosition
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.tipe = tipe
        self.color = color
        self.detectionMessage = "Pawn " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def updatePositions(self):
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.detectionMessage = "Pawn " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def checkForPiece(self):
        if pyautogui.locateCenterOnScreen("pawn_" + str(self.color) + ".png", region=(self.cornerPosition[0], self.cornerPosition[1], 95,95), confidence=0.6, grayscale=True) == None:
            print("Can't find pawn " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1]))
            return False
        else:
            print(self.detectionMessage)
            return True
    
    def checkForQueen(self):
        if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(self.cornerPosition[0], self.cornerPosition[1], 95,95), confidence=0.6, grayscale=True) == None:
            return False
        else:
            return True

    def determineCapture(self, pieceList):
        for piece in pieceList:
            if piece.boardPosition == self.boardPosition:
                piece.boardPosition = [0,0]
                pieceList.remove(piece)
                print("Pawn " + str(self.color) + " captured!")

    def move1(self): #Move up 1
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] += 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.boardPosition[1] == 8:
            a = self.checkForQueen()
            if a == False:
                return False
            elif a == True:
                return "Queen"
        if self.checkForPiece() == False:
            self.boardPosition[1] -= 1
            self.updatePositions()
            return False
        else:
            return True
        
    def move2(self): #Move up 2
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] += 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] -= 2
            self.updatePositions()
            return False
        else:
            return True

    def move3(self, enemyPieceList): #Capture left
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] += 1
        self.boardPosition[0] -= 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.boardPosition[1] == 8:
            a = self.checkForQueen()
            if a == False:
                return False
            elif a == True:
                return "Queen"
        if self.checkForPiece() == False:
            self.boardPosition[1] -= 1
            self.boardPosition[0] += 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move4(self, enemyPieceList): #Capture right
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] += 1
        self.boardPosition[0] += 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.boardPosition[1] == 8:
            a = self.checkForQueen()
            if a == False:
                return False
            elif a == True:
                return "Queen"
        if self.checkForPiece() == False:
            self.boardPosition[1] -= 1
            self.boardPosition[0] -= 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    
    #Validation for pawn movement. Returns either a list 
    #of values or False. False means there are no valid moves.
    def getValidMoves(self, playerPiecePositions, enemyPiecePositions, move1AttemptPos, move2AttemptPos, move3AttemptPos, move4AttemptPos, tipe="Opponent"):
        validMoves = []
        for piecePosition in playerPiecePositions:
            if piecePosition == move1AttemptPos: #Can't move if friendly piece is directly in front of pawn
                move1AttemptPos = False
                move2AttemptPos = False
            if piecePosition == move2AttemptPos: #Can't move twice if friendly piece is two spaces in front of pawn
                move2AttemptPos = False
            if tipe == "Player":
                if self.boardPosition[1] != 2: #Can't move twice if already moved once
                    move2AttemptPos = False
            if tipe == "Opponent":
                if self.boardPosition[1] != 7: #Can't move twice if already moved once
                    move2AttemptPos = False

        for piecePosition in enemyPiecePositions:
            if piecePosition == move3AttemptPos: #Capture left if enemy piece is there
                move3AttemptPos = True
            if piecePosition == move4AttemptPos: #Capture right if enemy piece is there
                move4AttemptPos = True
            if piecePosition == move1AttemptPos: #Can't move if enemy piece is directly in front of pawn
                move1AttemptPos = False
                move2AttemptPos = False
            if piecePosition == move2AttemptPos: #Can't move twice if enemy piece is two spaces in front of pawn
                move2AttemptPos = False

        if move1AttemptPos == False:
            pass
        else:
            validMoves.append(1)
        if move2AttemptPos == False:
            pass
        else:
            validMoves.append(2)
        if move3AttemptPos == True:
            validMoves.append(3)
        else:
            pass
        if move4AttemptPos == True:
            validMoves.append(4)
        else:
            pass
        if len(validMoves) == 0:
            return False
        else:
            return validMoves

    def movePiece(self, playerPiecePositions, enemyPiecePositions, enemyPieceList):
        validMoves = self.getValidMoves(playerPiecePositions, enemyPiecePositions, 
                                        [self.boardPosition[0], (self.boardPosition[1] + 1)],
                                        [self.boardPosition[0], (self.boardPosition[1] + 2)], 
                                        [(self.boardPosition[0] - 1), (self.boardPosition[1] + 1)],
                                        [(self.boardPosition[0] + 1), (self.boardPosition[1] + 1)],
                                        self.tipe)
        if validMoves == False:
            return False
        while True:
            if len(validMoves) == 0:
                return False
            move = random.choice(validMoves)
            if move == 1:
                a = self.move1()
                if a == "Queen":
                    return "Queen"
                elif a == True:
                    return True
                elif a == False:
                    validMoves.remove(move)
                    continue
            if move == 2:
                a = self.move2()
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(move)
                    continue
            if move == 3:
                a = self.move3(enemyPieceList)
                if a == "Queen":
                    return "Queen"
                elif a == True:
                    return True
                elif a == False:
                    validMoves.remove(move)
                    continue
            if move == 4:
                a = self.move4(enemyPieceList)
                if a == "Queen":
                    return "Queen"
                elif a == True:
                    return True
                elif a == False:
                    validMoves.remove(move)
                    continue

    def enemyFind(self, playerPiecePositions, enemyPiecePositions, playerPieceList):
        validMoves = self.getValidMoves(enemyPiecePositions, playerPiecePositions, 
                                        [self.boardPosition[0], (self.boardPosition[1] - 1)],
                                        [self.boardPosition[0], (self.boardPosition[1] - 2)], 
                                        [(self.boardPosition[0] - 1), (self.boardPosition[1] - 1)],
                                        [(self.boardPosition[0] + 1), (self.boardPosition[1] - 1)])
        if validMoves == False:
            return False
        for pos in validMoves:
            if pos == 1:
                checkPosition = [self.boardPosition[0], (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("pawn_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    if self.boardPosition[1] == 2:
                        if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                            pass
                        else:
                            self.boardPosition = checkPosition
                            self.updatePositions()
                            self.determineCapture(playerPieceList)
                            return "Queen"
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    
                    return
            if pos == 2:
                checkPosition = [self.boardPosition[0], (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("pawn_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 3:
                checkPosition = [(self.boardPosition[0] - 1), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("pawn_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    if self.boardPosition[1] == 2:
                        if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                            pass
                        else:
                            self.boardPosition = checkPosition
                            self.updatePositions()
                            self.determineCapture(playerPieceList)
                            return "Queen"
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    
                    return
            if pos == 4:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("pawn_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    if self.boardPosition[1] == 2:
                        if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                            pass
                        else:
                            self.boardPosition = checkPosition
                            self.updatePositions()
                            self.determineCapture(playerPieceList)
                            return "Queen"
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    
                    return