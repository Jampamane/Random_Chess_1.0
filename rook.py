import pyautogui
import random
import ctypes
import time

def click():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # Left mouse down
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # Left mouse up

class Rook():
    def __init__(self, boardPosition, tipe, m, s, color):
        self.mouseDictionary = m
        self.screenshotDictionary = s
        self.boardPosition = boardPosition
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.tipe = tipe
        self.color = color
        self.detectionMessage = "Rook " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def updatePositions(self):
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.detectionMessage = "Rook " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def checkForPiece(self):
        if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(self.cornerPosition[0], self.cornerPosition[1], 95,95), confidence=0.6, grayscale=True) == None:
            print("Can't find rook " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1]))
            return False
        else:
            print(self.detectionMessage)
            return True

    def determineCapture(self, pieceList):
        for piece in pieceList:
            if piece.boardPosition == self.boardPosition:
                piece.boardPosition = [0,0]
                pieceList.remove(piece)
                print("Rook " + str(self.color) + " captured!")
        
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

    def occupiedPlayer(self, moveAttemptPos, playerPiecePositions):
        if moveAttemptPos == False:
                return False
        else:
            for piece in playerPiecePositions:
                if moveAttemptPos == piece:
                    return False
        return moveAttemptPos

    def occupiedEnemy(self, moveAttemptPos, enemyPiecePositions):
        if moveAttemptPos == False:
            return False
        else:
            for piece in enemyPiecePositions:
                if moveAttemptPos == piece:
                    return True
        return moveAttemptPos

    def getValidMoves(self, playerPiecePositions, enemyPiecePositions):
        validMoves = []
        #Left
        move1AttemptPos = self.outOfBounds((self.boardPosition[0] - 1), self.boardPosition[1])
        move2AttemptPos = self.outOfBounds((self.boardPosition[0] - 2), self.boardPosition[1])
        move3AttemptPos = self.outOfBounds((self.boardPosition[0] - 3), self.boardPosition[1])
        move4AttemptPos = self.outOfBounds((self.boardPosition[0] - 4), self.boardPosition[1])
        move5AttemptPos = self.outOfBounds((self.boardPosition[0] - 5), self.boardPosition[1])
        move6AttemptPos = self.outOfBounds((self.boardPosition[0] - 6), self.boardPosition[1])
        move7AttemptPos = self.outOfBounds((self.boardPosition[0] - 7), self.boardPosition[1])
        #Right
        move8AttemptPos = self.outOfBounds((self.boardPosition[0] + 1), self.boardPosition[1])
        move9AttemptPos = self.outOfBounds((self.boardPosition[0] + 2), self.boardPosition[1])
        move10AttemptPos = self.outOfBounds((self.boardPosition[0] + 3), self.boardPosition[1])
        move11AttemptPos = self.outOfBounds((self.boardPosition[0] + 4), self.boardPosition[1])
        move12AttemptPos = self.outOfBounds((self.boardPosition[0] + 5), self.boardPosition[1])
        move13AttemptPos = self.outOfBounds((self.boardPosition[0] + 6), self.boardPosition[1])
        move14AttemptPos = self.outOfBounds((self.boardPosition[0] + 7), self.boardPosition[1])
        #Up
        move15AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 1))
        move16AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 2))
        move17AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 3))
        move18AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 4))
        move19AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 5))
        move20AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 6))
        move21AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] + 7))
        #Down
        move22AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 1))
        move23AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 2))
        move24AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 3))
        move25AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 4))
        move26AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 5))
        move27AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 6))
        move28AttemptPos = self.outOfBounds(self.boardPosition[0], (self.boardPosition[1] - 7))

        move1AttemptPos = self.occupiedPlayer(move1AttemptPos, playerPiecePositions)
        move2AttemptPos = self.occupiedPlayer(move2AttemptPos, playerPiecePositions)
        move3AttemptPos = self.occupiedPlayer(move3AttemptPos, playerPiecePositions)
        move4AttemptPos = self.occupiedPlayer(move4AttemptPos, playerPiecePositions)
        move5AttemptPos = self.occupiedPlayer(move5AttemptPos, playerPiecePositions)
        move6AttemptPos = self.occupiedPlayer(move6AttemptPos, playerPiecePositions)
        move7AttemptPos = self.occupiedPlayer(move7AttemptPos, playerPiecePositions)
        #Right
        move8AttemptPos = self.occupiedPlayer(move8AttemptPos, playerPiecePositions)
        move9AttemptPos = self.occupiedPlayer(move9AttemptPos, playerPiecePositions)
        move10AttemptPos = self.occupiedPlayer(move10AttemptPos, playerPiecePositions)
        move11AttemptPos = self.occupiedPlayer(move11AttemptPos, playerPiecePositions)
        move12AttemptPos = self.occupiedPlayer(move12AttemptPos, playerPiecePositions)
        move13AttemptPos = self.occupiedPlayer(move13AttemptPos, playerPiecePositions)
        move14AttemptPos = self.occupiedPlayer(move14AttemptPos, playerPiecePositions)
        #Up
        move15AttemptPos = self.occupiedPlayer(move15AttemptPos, playerPiecePositions)
        move16AttemptPos = self.occupiedPlayer(move16AttemptPos, playerPiecePositions)
        move17AttemptPos = self.occupiedPlayer(move17AttemptPos, playerPiecePositions)
        move18AttemptPos = self.occupiedPlayer(move18AttemptPos, playerPiecePositions)
        move19AttemptPos = self.occupiedPlayer(move19AttemptPos, playerPiecePositions)
        move20AttemptPos = self.occupiedPlayer(move20AttemptPos, playerPiecePositions)
        move21AttemptPos = self.occupiedPlayer(move21AttemptPos, playerPiecePositions)
        #Down
        move22AttemptPos = self.occupiedPlayer(move22AttemptPos, playerPiecePositions)
        move23AttemptPos = self.occupiedPlayer(move23AttemptPos, playerPiecePositions)
        move24AttemptPos = self.occupiedPlayer(move24AttemptPos, playerPiecePositions)
        move25AttemptPos = self.occupiedPlayer(move25AttemptPos, playerPiecePositions)
        move26AttemptPos = self.occupiedPlayer(move26AttemptPos, playerPiecePositions)
        move27AttemptPos = self.occupiedPlayer(move27AttemptPos, playerPiecePositions)
        move28AttemptPos = self.occupiedPlayer(move28AttemptPos, playerPiecePositions)

        move1AttemptPos = self.occupiedEnemy(move1AttemptPos, enemyPiecePositions)
        move2AttemptPos = self.occupiedEnemy(move2AttemptPos, enemyPiecePositions)
        move3AttemptPos = self.occupiedEnemy(move3AttemptPos, enemyPiecePositions)
        move4AttemptPos = self.occupiedEnemy(move4AttemptPos, enemyPiecePositions)
        move5AttemptPos = self.occupiedEnemy(move5AttemptPos, enemyPiecePositions)
        move6AttemptPos = self.occupiedEnemy(move6AttemptPos, enemyPiecePositions)
        move7AttemptPos = self.occupiedEnemy(move7AttemptPos, enemyPiecePositions)
        #Right
        move8AttemptPos = self.occupiedEnemy(move8AttemptPos, enemyPiecePositions)
        move9AttemptPos = self.occupiedEnemy(move9AttemptPos, enemyPiecePositions)
        move10AttemptPos = self.occupiedEnemy(move10AttemptPos, enemyPiecePositions)
        move11AttemptPos = self.occupiedEnemy(move11AttemptPos, enemyPiecePositions)
        move12AttemptPos = self.occupiedEnemy(move12AttemptPos, enemyPiecePositions)
        move13AttemptPos = self.occupiedEnemy(move13AttemptPos, enemyPiecePositions)
        move14AttemptPos = self.occupiedEnemy(move14AttemptPos, enemyPiecePositions)
        #Up
        move15AttemptPos = self.occupiedEnemy(move15AttemptPos, enemyPiecePositions)
        move16AttemptPos = self.occupiedEnemy(move16AttemptPos, enemyPiecePositions)
        move17AttemptPos = self.occupiedEnemy(move17AttemptPos, enemyPiecePositions)
        move18AttemptPos = self.occupiedEnemy(move18AttemptPos, enemyPiecePositions)
        move19AttemptPos = self.occupiedEnemy(move19AttemptPos, enemyPiecePositions)
        move20AttemptPos = self.occupiedEnemy(move20AttemptPos, enemyPiecePositions)
        move21AttemptPos = self.occupiedEnemy(move21AttemptPos, enemyPiecePositions)
        #Down
        move22AttemptPos = self.occupiedEnemy(move22AttemptPos, enemyPiecePositions)
        move23AttemptPos = self.occupiedEnemy(move23AttemptPos, enemyPiecePositions)
        move24AttemptPos = self.occupiedEnemy(move24AttemptPos, enemyPiecePositions)
        move25AttemptPos = self.occupiedEnemy(move25AttemptPos, enemyPiecePositions)
        move26AttemptPos = self.occupiedEnemy(move26AttemptPos, enemyPiecePositions)
        move27AttemptPos = self.occupiedEnemy(move27AttemptPos, enemyPiecePositions)
        move28AttemptPos = self.occupiedEnemy(move28AttemptPos, enemyPiecePositions)

        while True:
            if move1AttemptPos == False:
                move2AttemptPos = False
                move3AttemptPos = False
                move4AttemptPos = False
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            elif move1AttemptPos == True:
                validMoves.append(1)
                move2AttemptPos = False
                move3AttemptPos = False
                move4AttemptPos = False
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            else:
                validMoves.append(1)

            if move2AttemptPos == False:
                move3AttemptPos = False
                move4AttemptPos = False
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            elif move2AttemptPos == True:
                validMoves.append(2)
                move3AttemptPos = False
                move4AttemptPos = False
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            else:
                validMoves.append(2)

            if move3AttemptPos == False:
                move4AttemptPos = False
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            elif move3AttemptPos == True:
                validMoves.append(3)
                move4AttemptPos = False
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            else:
                validMoves.append(3)

            if move4AttemptPos == False:
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            elif move4AttemptPos == True:
                validMoves.append(4)
                move5AttemptPos = False
                move6AttemptPos = False
                move7AttemptPos = False
                break
            else:
                validMoves.append(4)

            if move5AttemptPos == False:
                move6AttemptPos = False
                move7AttemptPos = False
                break
            elif move5AttemptPos == True:
                validMoves.append(5)
                move6AttemptPos = False
                move7AttemptPos = False
                break
            else:
                validMoves.append(5)

            if move6AttemptPos == False:
                move7AttemptPos = False
                break
            elif move6AttemptPos == True:
                validMoves.append(6)
                move7AttemptPos = False
                break
            else:
                validMoves.append(6)

            if move7AttemptPos == False:
                break
            elif move7AttemptPos == True:
                validMoves.append(7)
                break
            else:
                validMoves.append(7)
                break
        
        while True:
            if move8AttemptPos == False:
                move9AttemptPos = False
                move10AttemptPos = False
                move11AttemptPos = False
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            elif move8AttemptPos == True:
                validMoves.append(8)
                move9AttemptPos = False
                move10AttemptPos = False
                move11AttemptPos = False
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            else:
                validMoves.append(8)

            if move9AttemptPos == False:
                move10AttemptPos = False
                move11AttemptPos = False
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            elif move9AttemptPos == True:
                validMoves.append(9)
                move10AttemptPos = False
                move11AttemptPos = False
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            else:
                validMoves.append(9)

            if move10AttemptPos == False:
                move11AttemptPos = False
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            elif move10AttemptPos == True:
                validMoves.append(10)
                move11AttemptPos = False
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            else:
                validMoves.append(10)

            if move11AttemptPos == False:
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            elif move11AttemptPos == True:
                validMoves.append(11)
                move12AttemptPos = False
                move13AttemptPos = False
                move14AttemptPos = False
                break
            else:
                validMoves.append(11)

            if move12AttemptPos == False:
                move13AttemptPos = False
                move14AttemptPos = False
                break
            elif move12AttemptPos == True:
                validMoves.append(12)
                move13AttemptPos = False
                move14AttemptPos = False
                break
            else:
                validMoves.append(12)

            if move13AttemptPos == False:
                move14AttemptPos = False
                break
            elif move13AttemptPos == True:
                validMoves.append(13)
                move14AttemptPos = False
                break
            else:
                validMoves.append(13)

            if move14AttemptPos == False:
                break
            elif move14AttemptPos == True:
                validMoves.append(14)
                break
            else:
                validMoves.append(14)
                break

        while True:
            if move15AttemptPos == False:
                move16AttemptPos = False
                move17AttemptPos = False
                move18AttemptPos = False
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            elif move15AttemptPos == True:
                validMoves.append(15)
                move16AttemptPos = False
                move17AttemptPos = False
                move18AttemptPos = False
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            else:
                validMoves.append(15)

            if move16AttemptPos == False:
                move17AttemptPos = False
                move18AttemptPos = False
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            elif move16AttemptPos == True:
                validMoves.append(16)
                move17AttemptPos = False
                move18AttemptPos = False
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            else:
                validMoves.append(16)

            if move17AttemptPos == False:
                move18AttemptPos = False
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            elif move17AttemptPos == True:
                validMoves.append(17)
                move18AttemptPos = False
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            else:
                validMoves.append(17)

            if move18AttemptPos == False:
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            elif move18AttemptPos == True:
                validMoves.append(18)
                move19AttemptPos = False
                move20AttemptPos = False
                move21AttemptPos = False
                break
            else:
                validMoves.append(18)

            if move19AttemptPos == False:
                move20AttemptPos = False
                move21AttemptPos = False
                break
            elif move19AttemptPos == True:
                validMoves.append(19)
                move20AttemptPos = False
                move21AttemptPos = False
                break
            else:
                validMoves.append(19)

            if move20AttemptPos == False:
                move21AttemptPos = False
                break
            elif move20AttemptPos == True:
                validMoves.append(20)
                move21AttemptPos = False
                break
            else:
                validMoves.append(20)

            if move21AttemptPos == False:
                break
            elif move21AttemptPos == True:
                validMoves.append(21)
                break
            else:
                validMoves.append(21)
                break

        while True:
            if move22AttemptPos == False:
                move23AttemptPos = False
                move24AttemptPos = False
                move25AttemptPos = False
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            elif move22AttemptPos == True:
                validMoves.append(22)
                move23AttemptPos = False
                move24AttemptPos = False
                move25AttemptPos = False
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            else:
                validMoves.append(22)

            if move23AttemptPos == False:
                move24AttemptPos = False
                move25AttemptPos = False
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            elif move2AttemptPos == True:
                validMoves.append(23)
                move24AttemptPos = False
                move25AttemptPos = False
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            else:
                validMoves.append(23)

            if move24AttemptPos == False:
                move25AttemptPos = False
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            elif move24AttemptPos == True:
                validMoves.append(24)
                move25AttemptPos = False
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            else:
                validMoves.append(24)

            if move25AttemptPos == False:
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            elif move25AttemptPos == True:
                validMoves.append(25)
                move26AttemptPos = False
                move27AttemptPos = False
                move28AttemptPos = False
                break
            else:
                validMoves.append(25)

            if move26AttemptPos == False:
                move27AttemptPos = False
                move28AttemptPos = False
                break
            elif move26AttemptPos == True:
                validMoves.append(26)
                move27AttemptPos = False
                move28AttemptPos = False
                break
            else:
                validMoves.append(26)

            if move27AttemptPos == False:
                move28AttemptPos = False
                break
            elif move27AttemptPos == True:
                validMoves.append(27)
                move28AttemptPos = False
                break
            else:
                validMoves.append(27)

            if move28AttemptPos == False:
                break
            elif move28AttemptPos == True:
                validMoves.append(28)
                break
            else:
                validMoves.append(28)
                break

        if len(validMoves) == 0:
            return False
        else:
            return validMoves


    def move1(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move2(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move3(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move4(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move5(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move6(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move7(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move8(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move9(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move10(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move11(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move12(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move13(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move14(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move15(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move16(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move17(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move18(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move19(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move20(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move21(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] + 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] - 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move22(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move23(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move24(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move25(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move26(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move27(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move28(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[1] = self.boardPosition[1] - 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[1] = self.boardPosition[1] + 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True

    def movePiece(self, playerPiecePositions, enemyPiecePositions, enemyPieceList):
        validMoves = self.getValidMoves(playerPiecePositions, enemyPiecePositions)
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
            elif moveChoice == 9:
                a = self.move9(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 10:
                a = self.move10(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 11:
                a = self.move11(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 12:
                a = self.move12(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 13:
                a = self.move13(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 14:
                a = self.move14(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 15:
                a = self.move15(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 16:
                a = self.move16(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 17:
                a = self.move17(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 18:
                a = self.move18(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 19:
                a = self.move19(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 20:
                a = self.move20(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 21:
                a = self.move21(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 22:
                a = self.move22(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 23:
                a = self.move23(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 24:
                a = self.move24(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 25:
                a = self.move25(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 26:
                a = self.move26(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 27:
                a = self.move27(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 28:
                a = self.move28(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue

    def enemyFind(self, playerPiecePositions, enemyPiecePositions, playerPieceList):
        validMoves = self.getValidMoves(enemyPiecePositions, playerPiecePositions)
        if validMoves == False:
            return False
        for pos in validMoves:
            if pos == 1:
                checkPosition = [(self.boardPosition[0] - 1), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 2:
                checkPosition = [(self.boardPosition[0] - 2), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 3:
                checkPosition = [(self.boardPosition[0] - 3), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 4:
                checkPosition = [(self.boardPosition[0] - 4), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 5:
                checkPosition = [(self.boardPosition[0] - 5), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 6:
                checkPosition = [(self.boardPosition[0] - 6), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 7:
                checkPosition = [(self.boardPosition[0] - 7), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 8:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 9:
                checkPosition = [(self.boardPosition[0] + 2), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 10:
                checkPosition = [(self.boardPosition[0] + 3), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 11:
                checkPosition = [(self.boardPosition[0] + 4), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 12:
                checkPosition = [(self.boardPosition[0] + 5), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 13:
                checkPosition = [(self.boardPosition[0] + 6), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 14:
                checkPosition = [(self.boardPosition[0] + 7), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 15:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 16:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 17:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 18:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 19:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 20:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 21:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 22:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 23:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 24:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 25:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 26:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 27:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 28:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("rook_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return