import pyautogui
import random
import ctypes
import time

def click():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # Left mouse down
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # Left mouse up

class Knight():
    def __init__(self, boardPosition, tipe, m, s, color):
        self.mouseDictionary = m
        self.screenshotDictionary = s
        self.boardPosition = boardPosition
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.tipe = tipe
        self.color = color
        self.detectionMessage = "Knight " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def updatePositions(self):
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.detectionMessage = "Knight " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def checkForPiece(self):
        if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(self.cornerPosition[0], self.cornerPosition[1], 95,95), confidence=0.4, grayscale=True) == None:
            print("Can't find knight " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1]))
            return False
        else:
            print(self.detectionMessage)
            return True

    def determineCapture(self, pieceList):
        for piece in pieceList:
            if piece.boardPosition == self.boardPosition:
                piece.boardPosition = [0,0]
                pieceList.remove(piece)
                print("Knight " + str(self.color) + " captured!")
    
    def move1(self, enemyPieceList): #Move left tall L up
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 1
        self.boardPosition[1] = self.boardPosition[1] + 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 1
            self.boardPosition[1] = self.boardPosition[1] - 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move2(self, enemyPieceList): #Move left long L up
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 2
        self.boardPosition[1] = self.boardPosition[1] + 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 2
            self.boardPosition[1] = self.boardPosition[1] - 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move3(self, enemyPieceList): #Move left tall L down
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 1
        self.boardPosition[1] = self.boardPosition[1] - 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 1
            self.boardPosition[1] = self.boardPosition[1] + 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move4(self, enemyPieceList): #Move left long L down
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 2
        self.boardPosition[1] = self.boardPosition[1] - 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 2
            self.boardPosition[1] = self.boardPosition[1] + 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move5(self, enemyPieceList): #Move right tall L up
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 1
        self.boardPosition[1] = self.boardPosition[1] + 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 1
            self.boardPosition[1] = self.boardPosition[1] - 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move6(self, enemyPieceList): #Move right long L up
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 2
        self.boardPosition[1] = self.boardPosition[1] + 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 2
            self.boardPosition[1] = self.boardPosition[1] - 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move7(self, enemyPieceList): #Move right long L down
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 2
        self.boardPosition[1] = self.boardPosition[1] - 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 2
            self.boardPosition[1] = self.boardPosition[1] + 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def move8(self, enemyPieceList): #Move right tall L down
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 1
        self.boardPosition[1] = self.boardPosition[1] - 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 1
            self.boardPosition[1] = self.boardPosition[1] + 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def outOfBounds(self, x, y):
        if x > 8:
            return False
        if x < 1:
            return False
        if y > 8:
            return False
        if y < 1:
            return False
        return [x, y]

    def occupied(self, moveAttemptPos, playerPiecePositions):
        if moveAttemptPos == False:
                pass
        else:
            for piece in playerPiecePositions:
                if moveAttemptPos == piece:
                    return False
        return moveAttemptPos

    def getValidMoves(self, playerPiecePositions):
        validMoves = []
        move1AttemptPos = self.outOfBounds((self.boardPosition[0] - 1), (self.boardPosition[1] + 2))
        move2AttemptPos = self.outOfBounds((self.boardPosition[0] - 2), (self.boardPosition[1] + 1))
        move3AttemptPos = self.outOfBounds((self.boardPosition[0] - 1), (self.boardPosition[1] - 2))
        move4AttemptPos = self.outOfBounds((self.boardPosition[0] - 2), (self.boardPosition[1] - 1))
        move5AttemptPos = self.outOfBounds((self.boardPosition[0] + 1), (self.boardPosition[1] + 2))
        move6AttemptPos = self.outOfBounds((self.boardPosition[0] + 2), (self.boardPosition[1] + 1))
        move7AttemptPos = self.outOfBounds((self.boardPosition[0] + 2), (self.boardPosition[1] - 1))
        move8AttemptPos = self.outOfBounds((self.boardPosition[0] + 1), (self.boardPosition[1] - 2))
        move1AttemptPos = self.occupied(move1AttemptPos, playerPiecePositions)
        move2AttemptPos = self.occupied(move2AttemptPos, playerPiecePositions)
        move3AttemptPos = self.occupied(move3AttemptPos, playerPiecePositions)
        move4AttemptPos = self.occupied(move4AttemptPos, playerPiecePositions)
        move5AttemptPos = self.occupied(move5AttemptPos, playerPiecePositions)
        move6AttemptPos = self.occupied(move6AttemptPos, playerPiecePositions)
        move7AttemptPos = self.occupied(move7AttemptPos, playerPiecePositions)
        move8AttemptPos = self.occupied(move8AttemptPos, playerPiecePositions)

        if move1AttemptPos == False:
            pass
        else:
            validMoves.append(1)
        if move2AttemptPos == False:
            pass
        else:
            validMoves.append(2)
        if move3AttemptPos == False:
            pass
        else:
            validMoves.append(3)
        if move4AttemptPos == False:
            pass
        else:
            validMoves.append(4)
        if move5AttemptPos == False:
            pass
        else:
            validMoves.append(5)
        if move6AttemptPos == False:
            pass
        else:
            validMoves.append(6)
        if move7AttemptPos == False:
            pass
        else:
            validMoves.append(7)
        if move8AttemptPos == False:
            pass
        else:
            validMoves.append(8)

        if len(validMoves) == 0:
            return False
        else:
            return validMoves

    def movePiece(self, playerPiecePositions, enemyPiecePositions, enemyPieceList):
        validMoves = self.getValidMoves(playerPiecePositions)
        if validMoves == False:
            return False
        while True:
            if len(validMoves) == 0:
                return False
            moveChoice = random.choice(validMoves)
            if moveChoice == 1:
                a = self.move1(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 2:
                a = self.move2(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 3:
                a = self.move3(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 4:
                a = self.move4(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 5:
                a = self.move5(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 6:
                a = self.move6(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 7:
                a = self.move7(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 8:
                a = self.move8(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
        
    def enemyFind(self, playerPiecePositions, enemyPiecePositions, playerPieceList):
        validMoves = self.getValidMoves(enemyPiecePositions)
        if validMoves == False:
            return False
        for pos in validMoves:
            if pos == 1:
                checkPosition = [(self.boardPosition[0] - 1), (self.boardPosition[1] + 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 2:
                checkPosition = [(self.boardPosition[0] - 2), (self.boardPosition[1] + 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 3:
                checkPosition = [(self.boardPosition[0] - 1), (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 4:
                checkPosition = [(self.boardPosition[0] - 2), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 5:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1] + 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 6:
                checkPosition = [(self.boardPosition[0] + 2), (self.boardPosition[1] + 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 7:
                checkPosition = [(self.boardPosition[0] + 2), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 8:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("knight_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.4, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return