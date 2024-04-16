import pyautogui
import random
import ctypes
import time

def click():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # Left mouse down
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # Left mouse up

class Queen():
    def __init__(self, boardPosition, tipe, m, s, color):
        self.mouseDictionary = m
        self.screenshotDictionary = s
        self.boardPosition = boardPosition
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.tipe = tipe
        self.color = color
        self.detectionMessage = "Queen " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def updatePositions(self):
        self.mousePosition = self.mouseDictionary[','.join(str(e) for e in self.boardPosition)]
        self.cornerPosition = self.screenshotDictionary[','.join(str(e) for e in self.boardPosition)]
        self.detectionMessage = "Queen " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1])

    def checkForPiece(self):
        if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(self.cornerPosition[0], self.cornerPosition[1], 95,95), confidence=0.6) == None:
            print("Can't find queen " + str(self.color) + " located at " + str(self.boardPosition[0]) + "," + str(self.boardPosition[1]))
            return False
        else:
            print(self.detectionMessage)
            return True

    def determineCapture(self, pieceList):
        for piece in pieceList:
            if piece.boardPosition == self.boardPosition:
                piece.boardPosition = [0,0]
                pieceList.remove(piece)
                print("Queen " + str(self.color) + " captured!")

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
        #Upper-Left
        move29AttemptPos = self.outOfBounds((self.boardPosition[0] - 1), (self.boardPosition[1] + 1))
        move30AttemptPos = self.outOfBounds((self.boardPosition[0] - 2), (self.boardPosition[1] + 2))
        move31AttemptPos = self.outOfBounds((self.boardPosition[0] - 3), (self.boardPosition[1] + 3))
        move32AttemptPos = self.outOfBounds((self.boardPosition[0] - 4), (self.boardPosition[1] + 4))
        move33AttemptPos = self.outOfBounds((self.boardPosition[0] - 5), (self.boardPosition[1] + 5))
        move34AttemptPos = self.outOfBounds((self.boardPosition[0] - 6), (self.boardPosition[1] + 6))
        move35AttemptPos = self.outOfBounds((self.boardPosition[0] - 7), (self.boardPosition[1] + 7))
        #Upper-Right
        move36AttemptPos = self.outOfBounds((self.boardPosition[0] + 1), (self.boardPosition[1] + 1))
        move37AttemptPos = self.outOfBounds((self.boardPosition[0] + 2), (self.boardPosition[1] + 2))
        move38AttemptPos = self.outOfBounds((self.boardPosition[0] + 3), (self.boardPosition[1] + 3))
        move39AttemptPos = self.outOfBounds((self.boardPosition[0] + 4), (self.boardPosition[1] + 4))
        move40AttemptPos = self.outOfBounds((self.boardPosition[0] + 5), (self.boardPosition[1] + 5))
        move41AttemptPos = self.outOfBounds((self.boardPosition[0] + 6), (self.boardPosition[1] + 6))
        move42AttemptPos = self.outOfBounds((self.boardPosition[0] + 7), (self.boardPosition[1] + 7))
        #Down-Left
        move43AttemptPos = self.outOfBounds((self.boardPosition[0] - 1), (self.boardPosition[1] - 1))
        move44AttemptPos = self.outOfBounds((self.boardPosition[0] - 2), (self.boardPosition[1] - 2))
        move45AttemptPos = self.outOfBounds((self.boardPosition[0] - 3), (self.boardPosition[1] - 3))
        move46AttemptPos = self.outOfBounds((self.boardPosition[0] - 4), (self.boardPosition[1] - 4))
        move47AttemptPos = self.outOfBounds((self.boardPosition[0] - 5), (self.boardPosition[1] - 5))
        move48AttemptPos = self.outOfBounds((self.boardPosition[0] - 6), (self.boardPosition[1] - 6))
        move49AttemptPos = self.outOfBounds((self.boardPosition[0] - 7), (self.boardPosition[1] - 7))
        #Down-Right
        move50AttemptPos = self.outOfBounds((self.boardPosition[0] + 1), (self.boardPosition[1] - 1))
        move51AttemptPos = self.outOfBounds((self.boardPosition[0] + 2), (self.boardPosition[1] - 2))
        move52AttemptPos = self.outOfBounds((self.boardPosition[0] + 3), (self.boardPosition[1] - 3))
        move53AttemptPos = self.outOfBounds((self.boardPosition[0] + 4), (self.boardPosition[1] - 4))
        move54AttemptPos = self.outOfBounds((self.boardPosition[0] + 5), (self.boardPosition[1] - 5))
        move55AttemptPos = self.outOfBounds((self.boardPosition[0] + 6), (self.boardPosition[1] - 6))
        move56AttemptPos = self.outOfBounds((self.boardPosition[0] + 7), (self.boardPosition[1] - 7))
        #Left
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
        #Upper-Left
        move29AttemptPos = self.occupiedPlayer(move29AttemptPos, playerPiecePositions)
        move30AttemptPos = self.occupiedPlayer(move30AttemptPos, playerPiecePositions)
        move31AttemptPos = self.occupiedPlayer(move31AttemptPos, playerPiecePositions)
        move32AttemptPos = self.occupiedPlayer(move32AttemptPos, playerPiecePositions)
        move33AttemptPos = self.occupiedPlayer(move33AttemptPos, playerPiecePositions)
        move34AttemptPos = self.occupiedPlayer(move34AttemptPos, playerPiecePositions)
        move35AttemptPos = self.occupiedPlayer(move35AttemptPos, playerPiecePositions)
        #Upper-Right
        move36AttemptPos = self.occupiedPlayer(move36AttemptPos, playerPiecePositions)
        move37AttemptPos = self.occupiedPlayer(move37AttemptPos, playerPiecePositions)
        move38AttemptPos = self.occupiedPlayer(move38AttemptPos, playerPiecePositions)
        move39AttemptPos = self.occupiedPlayer(move39AttemptPos, playerPiecePositions)
        move40AttemptPos = self.occupiedPlayer(move40AttemptPos, playerPiecePositions)
        move41AttemptPos = self.occupiedPlayer(move41AttemptPos, playerPiecePositions)
        move42AttemptPos = self.occupiedPlayer(move42AttemptPos, playerPiecePositions)
        #Down-Left
        move43AttemptPos = self.occupiedPlayer(move43AttemptPos, playerPiecePositions)
        move44AttemptPos = self.occupiedPlayer(move44AttemptPos, playerPiecePositions)
        move45AttemptPos = self.occupiedPlayer(move45AttemptPos, playerPiecePositions)
        move46AttemptPos = self.occupiedPlayer(move46AttemptPos, playerPiecePositions)
        move47AttemptPos = self.occupiedPlayer(move47AttemptPos, playerPiecePositions)
        move48AttemptPos = self.occupiedPlayer(move48AttemptPos, playerPiecePositions)
        move49AttemptPos = self.occupiedPlayer(move49AttemptPos, playerPiecePositions)
        #Down-Right
        move50AttemptPos = self.occupiedPlayer(move50AttemptPos, playerPiecePositions)
        move51AttemptPos = self.occupiedPlayer(move51AttemptPos, playerPiecePositions)
        move52AttemptPos = self.occupiedPlayer(move52AttemptPos, playerPiecePositions)
        move53AttemptPos = self.occupiedPlayer(move53AttemptPos, playerPiecePositions)
        move54AttemptPos = self.occupiedPlayer(move54AttemptPos, playerPiecePositions)
        move55AttemptPos = self.occupiedPlayer(move55AttemptPos, playerPiecePositions)
        move56AttemptPos = self.occupiedPlayer(move56AttemptPos, playerPiecePositions)


        #Left
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
        #Upper-Left
        move29AttemptPos = self.occupiedEnemy(move29AttemptPos, enemyPiecePositions)
        move30AttemptPos = self.occupiedEnemy(move30AttemptPos, enemyPiecePositions)
        move31AttemptPos = self.occupiedEnemy(move31AttemptPos, enemyPiecePositions)
        move32AttemptPos = self.occupiedEnemy(move32AttemptPos, enemyPiecePositions)
        move33AttemptPos = self.occupiedEnemy(move33AttemptPos, enemyPiecePositions)
        move34AttemptPos = self.occupiedEnemy(move34AttemptPos, enemyPiecePositions)
        move35AttemptPos = self.occupiedEnemy(move35AttemptPos, enemyPiecePositions)
        #Upper-Right
        move36AttemptPos = self.occupiedEnemy(move36AttemptPos, enemyPiecePositions)
        move37AttemptPos = self.occupiedEnemy(move37AttemptPos, enemyPiecePositions)
        move38AttemptPos = self.occupiedEnemy(move38AttemptPos, enemyPiecePositions)
        move39AttemptPos = self.occupiedEnemy(move39AttemptPos, enemyPiecePositions)
        move40AttemptPos = self.occupiedEnemy(move40AttemptPos, enemyPiecePositions)
        move41AttemptPos = self.occupiedEnemy(move41AttemptPos, enemyPiecePositions)
        move42AttemptPos = self.occupiedEnemy(move42AttemptPos, enemyPiecePositions)
        #Down-Left
        move43AttemptPos = self.occupiedEnemy(move43AttemptPos, enemyPiecePositions)
        move44AttemptPos = self.occupiedEnemy(move44AttemptPos, enemyPiecePositions)
        move45AttemptPos = self.occupiedEnemy(move45AttemptPos, enemyPiecePositions)
        move46AttemptPos = self.occupiedEnemy(move46AttemptPos, enemyPiecePositions)
        move47AttemptPos = self.occupiedEnemy(move47AttemptPos, enemyPiecePositions)
        move48AttemptPos = self.occupiedEnemy(move48AttemptPos, enemyPiecePositions)
        move49AttemptPos = self.occupiedEnemy(move49AttemptPos, enemyPiecePositions)
        #Down-Right
        move50AttemptPos = self.occupiedEnemy(move50AttemptPos, enemyPiecePositions)
        move51AttemptPos = self.occupiedEnemy(move51AttemptPos, enemyPiecePositions)
        move52AttemptPos = self.occupiedEnemy(move52AttemptPos, enemyPiecePositions)
        move53AttemptPos = self.occupiedEnemy(move53AttemptPos, enemyPiecePositions)
        move54AttemptPos = self.occupiedEnemy(move54AttemptPos, enemyPiecePositions)
        move55AttemptPos = self.occupiedEnemy(move55AttemptPos, enemyPiecePositions)
        move56AttemptPos = self.occupiedEnemy(move56AttemptPos, enemyPiecePositions)

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

        while True:
            if move29AttemptPos == False:
                move30AttemptPos = False
                move31AttemptPos = False
                move32AttemptPos = False
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            elif move29AttemptPos == True:
                validMoves.append(29)
                move30AttemptPos = False
                move31AttemptPos = False
                move32AttemptPos = False
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            else:
                validMoves.append(29)

            if move30AttemptPos == False:
                move31AttemptPos = False
                move32AttemptPos = False
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            elif move30AttemptPos == True:
                validMoves.append(30)
                move31AttemptPos = False
                move32AttemptPos = False
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            else:
                validMoves.append(30)

            if move31AttemptPos == False:
                move32AttemptPos = False
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            elif move31AttemptPos == True:
                validMoves.append(31)
                move32AttemptPos = False
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            else:
                validMoves.append(31)

            if move32AttemptPos == False:
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            elif move32AttemptPos == True:
                validMoves.append(32)
                move33AttemptPos = False
                move34AttemptPos = False
                move35AttemptPos = False
                break
            else:
                validMoves.append(32)

            if move33AttemptPos == False:
                move34AttemptPos = False
                move35AttemptPos = False
                break
            elif move33AttemptPos == True:
                validMoves.append(33)
                move34AttemptPos = False
                move35AttemptPos = False
                break
            else:
                validMoves.append(33)

            if move34AttemptPos == False:
                move35AttemptPos = False
                break
            elif move34AttemptPos == True:
                validMoves.append(34)
                move35AttemptPos = False
                break
            else:
                validMoves.append(34)

            if move35AttemptPos == False:
                break
            elif move35AttemptPos == True:
                validMoves.append(35)
                break
            else:
                validMoves.append(35)
                break
        
        while True:
            if move36AttemptPos == False:
                move37AttemptPos = False
                move38AttemptPos = False
                move39AttemptPos = False
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            elif move36AttemptPos == True:
                validMoves.append(36)
                move37AttemptPos = False
                move38AttemptPos = False
                move39AttemptPos = False
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            else:
                validMoves.append(36)

            if move37AttemptPos == False:
                move38AttemptPos = False
                move39AttemptPos = False
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            elif move37AttemptPos == True:
                validMoves.append(37)
                move38AttemptPos = False
                move39AttemptPos = False
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            else:
                validMoves.append(37)

            if move38AttemptPos == False:
                move39AttemptPos = False
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            elif move38AttemptPos == True:
                validMoves.append(38)
                move39AttemptPos = False
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            else:
                validMoves.append(38)

            if move39AttemptPos == False:
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            elif move39AttemptPos == True:
                validMoves.append(39)
                move40AttemptPos = False
                move41AttemptPos = False
                move42AttemptPos = False
                break
            else:
                validMoves.append(39)

            if move40AttemptPos == False:
                move41AttemptPos = False
                move42AttemptPos = False
                break
            elif move40AttemptPos == True:
                validMoves.append(40)
                move41AttemptPos = False
                move42AttemptPos = False
                break
            else:
                validMoves.append(40)

            if move41AttemptPos == False:
                move42AttemptPos = False
                break
            elif move41AttemptPos == True:
                validMoves.append(41)
                move42AttemptPos = False
                break
            else:
                validMoves.append(41)

            if move42AttemptPos == False:
                break
            elif move42AttemptPos == True:
                validMoves.append(42)
                break
            else:
                validMoves.append(42)
                break

        while True:
            if move43AttemptPos == False:
                move44AttemptPos = False
                move45AttemptPos = False
                move46AttemptPos = False
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            elif move43AttemptPos == True:
                validMoves.append(43)
                move44AttemptPos = False
                move45AttemptPos = False
                move46AttemptPos = False
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            else:
                validMoves.append(43)

            if move44AttemptPos == False:
                move45AttemptPos = False
                move46AttemptPos = False
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            elif move44AttemptPos == True:
                validMoves.append(44)
                move45AttemptPos = False
                move46AttemptPos = False
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            else:
                validMoves.append(44)

            if move45AttemptPos == False:
                move46AttemptPos = False
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            elif move45AttemptPos == True:
                validMoves.append(45)
                move46AttemptPos = False
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            else:
                validMoves.append(45)

            if move46AttemptPos == False:
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            elif move46AttemptPos == True:
                validMoves.append(46)
                move47AttemptPos = False
                move48AttemptPos = False
                move49AttemptPos = False
                break
            else:
                validMoves.append(46)

            if move47AttemptPos == False:
                move48AttemptPos = False
                move49AttemptPos = False
                break
            elif move47AttemptPos == True:
                validMoves.append(47)
                move48AttemptPos = False
                move49AttemptPos = False
                break
            else:
                validMoves.append(47)

            if move48AttemptPos == False:
                move49AttemptPos = False
                break
            elif move48AttemptPos == True:
                validMoves.append(48)
                move49AttemptPos = False
                break
            else:
                validMoves.append(48)

            if move49AttemptPos == False:
                break
            elif move49AttemptPos == True:
                validMoves.append(49)
                break
            else:
                validMoves.append(49)
                break

        while True:
            if move50AttemptPos == False:
                move51AttemptPos = False
                move52AttemptPos = False
                move53AttemptPos = False
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            elif move50AttemptPos == True:
                validMoves.append(50)
                move51AttemptPos = False
                move52AttemptPos = False
                move53AttemptPos = False
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            else:
                validMoves.append(50)

            if move51AttemptPos == False:
                move52AttemptPos = False
                move53AttemptPos = False
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            elif move51AttemptPos == True:
                validMoves.append(51)
                move52AttemptPos = False
                move53AttemptPos = False
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            else:
                validMoves.append(51)

            if move52AttemptPos == False:
                move53AttemptPos = False
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            elif move52AttemptPos == True:
                validMoves.append(52)
                move53AttemptPos = False
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            else:
                validMoves.append(52)

            if move53AttemptPos == False:
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            elif move53AttemptPos == True:
                validMoves.append(53)
                move54AttemptPos = False
                move55AttemptPos = False
                move56AttemptPos = False
                break
            else:
                validMoves.append(53)

            if move54AttemptPos == False:
                move55AttemptPos = False
                move56AttemptPos = False
                break
            elif move54AttemptPos == True:
                validMoves.append(54)
                move55AttemptPos = False
                move56AttemptPos = False
                break
            else:
                validMoves.append(54)

            if move55AttemptPos == False:
                move55AttemptPos = False
                break
            elif move55AttemptPos == True:
                validMoves.append(55)
                move56AttemptPos = False
                break
            else:
                validMoves.append(55)

            if move56AttemptPos == False:
                break
            elif move56AttemptPos == True:
                validMoves.append(56)
                break
            else:
                validMoves.append(56)
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

    def move29(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 1
        self.boardPosition[1] = self.boardPosition[1] + 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 1
            self.boardPosition[1] = self.boardPosition[1] - 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move30(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 2
        self.boardPosition[1] = self.boardPosition[1] + 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 2
            self.boardPosition[1] = self.boardPosition[1] - 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move31(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 3
        self.boardPosition[1] = self.boardPosition[1] + 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 3
            self.boardPosition[1] = self.boardPosition[1] - 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move32(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 4
        self.boardPosition[1] = self.boardPosition[1] + 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 4
            self.boardPosition[1] = self.boardPosition[1] - 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move33(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 5
        self.boardPosition[1] = self.boardPosition[1] + 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 5
            self.boardPosition[1] = self.boardPosition[1] - 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move34(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 6
        self.boardPosition[1] = self.boardPosition[1] + 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 6
            self.boardPosition[1] = self.boardPosition[1] - 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move35(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 7
        self.boardPosition[1] = self.boardPosition[1] + 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 7
            self.boardPosition[1] = self.boardPosition[1] - 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move36(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 1
        self.boardPosition[1] = self.boardPosition[1] + 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 1
            self.boardPosition[1] = self.boardPosition[1] - 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move37(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 2
        self.boardPosition[1] = self.boardPosition[1] + 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 2
            self.boardPosition[1] = self.boardPosition[1] - 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move38(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 3
        self.boardPosition[1] = self.boardPosition[1] + 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 3
            self.boardPosition[1] = self.boardPosition[1] - 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move39(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 4
        self.boardPosition[1] = self.boardPosition[1] + 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 4
            self.boardPosition[1] = self.boardPosition[1] - 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move40(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 5
        self.boardPosition[1] = self.boardPosition[1] + 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 5
            self.boardPosition[1] = self.boardPosition[1] - 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move41(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 6
        self.boardPosition[1] = self.boardPosition[1] + 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 6
            self.boardPosition[1] = self.boardPosition[1] - 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move42(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 7
        self.boardPosition[1] = self.boardPosition[1] + 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 7
            self.boardPosition[1] = self.boardPosition[1] - 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move43(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 1
        self.boardPosition[1] = self.boardPosition[1] - 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 1
            self.boardPosition[1] = self.boardPosition[1] + 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move44(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 2
        self.boardPosition[1] = self.boardPosition[1] - 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 2
            self.boardPosition[1] = self.boardPosition[1] + 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move45(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 3
        self.boardPosition[1] = self.boardPosition[1] - 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 3
            self.boardPosition[1] = self.boardPosition[1] + 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move46(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 4
        self.boardPosition[1] = self.boardPosition[1] - 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 4
            self.boardPosition[1] = self.boardPosition[1] + 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move47(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 5
        self.boardPosition[1] = self.boardPosition[1] - 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 5
            self.boardPosition[1] = self.boardPosition[1] + 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move48(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 6
        self.boardPosition[1] = self.boardPosition[1] - 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 6
            self.boardPosition[1] = self.boardPosition[1] + 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move49(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] - 7
        self.boardPosition[1] = self.boardPosition[1] - 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] + 7
            self.boardPosition[1] = self.boardPosition[1] + 7
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move50(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 1
        self.boardPosition[1] = self.boardPosition[1] - 1
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 1
            self.boardPosition[1] = self.boardPosition[1] + 1
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move51(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 2
        self.boardPosition[1] = self.boardPosition[1] - 2
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 2
            self.boardPosition[1] = self.boardPosition[1] + 2
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move52(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 3
        self.boardPosition[1] = self.boardPosition[1] - 3
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 3
            self.boardPosition[1] = self.boardPosition[1] + 3
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move53(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 4
        self.boardPosition[1] = self.boardPosition[1] - 4
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 4
            self.boardPosition[1] = self.boardPosition[1] + 4
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move54(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 5
        self.boardPosition[1] = self.boardPosition[1] - 5
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 5
            self.boardPosition[1] = self.boardPosition[1] + 5
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move55(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 6
        self.boardPosition[1] = self.boardPosition[1] - 6
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 6
            self.boardPosition[1] = self.boardPosition[1] + 6
            self.updatePositions()
            return False
        else:
            self.determineCapture(enemyPieceList)
            return True
    def move56(self, enemyPieceList):
        pyautogui.moveTo(self.mousePosition)
        click()
        self.boardPosition[0] = self.boardPosition[0] + 7
        self.boardPosition[1] = self.boardPosition[1] - 7
        self.updatePositions()
        pyautogui.moveTo(self.mousePosition)
        click()
        time.sleep(0.2)
        if self.checkForPiece() == False:
            self.boardPosition[0] = self.boardPosition[0] - 7
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
            elif moveChoice == 29:
                a = self.move29(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 30:
                a = self.move30(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 31:
                a = self.move31(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 32:
                a = self.move32(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 33:
                a = self.move33(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 34:
                a = self.move34(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 35:
                a = self.move35(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 36:
                a = self.move36(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 37:
                a = self.move37(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 38:
                a = self.move38(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 39:
                a = self.move39(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 40:
                a = self.move40(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 41:
                a = self.move41(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 42:
                a = self.move42(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 43:
                a = self.move43(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 44:
                a = self.move44(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 45:
                a = self.move45(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 46:
                a = self.move46(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 47:
                a = self.move47(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 48:
                a = self.move48(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 49:
                a = self.move49(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 50:
                a = self.move50(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 51:
                a = self.move51(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 52:
                a = self.move52(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 53:
                a = self.move53(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 54:
                a = self.move54(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 55:
                a = self.move55(enemyPieceList)
                if a == True:
                    return True
                elif a == False:
                    validMoves.remove(moveChoice)
                    continue
            elif moveChoice == 56:
                a = self.move56(enemyPieceList)
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
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 2:
                checkPosition = [(self.boardPosition[0] - 2), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 3:
                checkPosition = [(self.boardPosition[0] - 3), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 4:
                checkPosition = [(self.boardPosition[0] - 4), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 5:
                checkPosition = [(self.boardPosition[0] - 5), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 6:
                checkPosition = [(self.boardPosition[0] - 6), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 7:
                checkPosition = [(self.boardPosition[0] - 7), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 8:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 9:
                checkPosition = [(self.boardPosition[0] + 2), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 10:
                checkPosition = [(self.boardPosition[0] + 3), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 11:
                checkPosition = [(self.boardPosition[0] + 4), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 12:
                checkPosition = [(self.boardPosition[0] + 5), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 13:
                checkPosition = [(self.boardPosition[0] + 6), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 14:
                checkPosition = [(self.boardPosition[0] + 7), (self.boardPosition[1])]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 15:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 16:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 17:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 18:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 19:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 20:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 21:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] + 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 22:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 23:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 24:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 25:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 26:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 27:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 28:
                checkPosition = [(self.boardPosition[0]), (self.boardPosition[1] - 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 29:
                checkPosition = [(self.boardPosition[0] - 1), (self.boardPosition[1] + 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 30:
                checkPosition = [(self.boardPosition[0] - 2), (self.boardPosition[1] + 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 31:
                checkPosition = [(self.boardPosition[0] - 3), (self.boardPosition[1] + 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 32:
                checkPosition = [(self.boardPosition[0] - 4), (self.boardPosition[1] + 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 33:
                checkPosition = [(self.boardPosition[0] - 5), (self.boardPosition[1] + 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 34:
                checkPosition = [(self.boardPosition[0] - 6), (self.boardPosition[1] + 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 35:
                checkPosition = [(self.boardPosition[0] - 7), (self.boardPosition[1] + 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 36:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1] + 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 37:
                checkPosition = [(self.boardPosition[0] + 2), (self.boardPosition[1] + 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 38:
                checkPosition = [(self.boardPosition[0] + 3), (self.boardPosition[1] + 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 39:
                checkPosition = [(self.boardPosition[0] + 4), (self.boardPosition[1] + 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 40:
                checkPosition = [(self.boardPosition[0] + 5), (self.boardPosition[1] + 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 41:
                checkPosition = [(self.boardPosition[0] + 6), (self.boardPosition[1] + 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 42:
                checkPosition = [(self.boardPosition[0] + 7), (self.boardPosition[1] + 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 43:
                checkPosition = [(self.boardPosition[0] - 1), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 44:
                checkPosition = [(self.boardPosition[0] - 2), (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 45:
                checkPosition = [(self.boardPosition[0] - 3), (self.boardPosition[1] - 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 46:
                checkPosition = [(self.boardPosition[0] - 4), (self.boardPosition[1] - 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 47:
                checkPosition = [(self.boardPosition[0] - 5), (self.boardPosition[1] - 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 48:
                checkPosition = [(self.boardPosition[0] - 6), (self.boardPosition[1] + - 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 49:
                checkPosition = [(self.boardPosition[0] - 7), (self.boardPosition[1] - 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 50:
                checkPosition = [(self.boardPosition[0] + 1), (self.boardPosition[1] - 1)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 51:
                checkPosition = [(self.boardPosition[0] + 2), (self.boardPosition[1] - 2)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 52:
                checkPosition = [(self.boardPosition[0] + 3), (self.boardPosition[1] - 3)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 53:
                checkPosition = [(self.boardPosition[0] + 4), (self.boardPosition[1] - 4)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 54:
                checkPosition = [(self.boardPosition[0] + 5), (self.boardPosition[1] - 5)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 55:
                checkPosition = [(self.boardPosition[0] + 6), (self.boardPosition[1] - 6)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return
            if pos == 56:
                checkPosition = [(self.boardPosition[0] + 7), (self.boardPosition[1] - 7)]
                checkCorner = self.screenshotDictionary[','.join(str(e) for e in checkPosition)]
                if pyautogui.locateCenterOnScreen("queen_" + str(self.color) + ".png", region=(checkCorner[0], checkCorner[1], 95,95), confidence=0.6, grayscale=True) == None:
                    pass
                else:
                    self.boardPosition = checkPosition
                    self.updatePositions()
                    self.determineCapture(playerPieceList)
                    return