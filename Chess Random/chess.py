import pyautogui
import random
import ctypes
import time
import pawn
import knight
import rook
import bishop
import king
import queen

def click():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # Left mouse down
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # Left mouse up

class Player():
    def __init__(self, tipe, color):
        self.m ={"1,1": [377,888], "2,1": [472,888], "3,1": [564,888], "4,1": [658,888], "5,1": [753,888], "6,1": [849,888], "7,1": [948,888], "8,1": [1041,888],
                 "1,2": [377,794], "2,2": [472,794], "3,2": [564,794], "4,2": [658,794], "5,2": [753,794], "6,2": [849,794], "7,2": [948,794], "8,2": [1041,794],
                 "1,3": [377,686], "2,3": [472,686], "3,3": [564,686], "4,3": [658,686], "5,3": [753,686], "6,3": [849,686], "7,3": [948,686], "8,3": [1041,686],
                 "1,4": [377,592], "2,4": [472,592], "3,4": [564,592], "4,4": [658,592], "5,4": [753,592], "6,4": [849,592], "7,4": [948,592], "8,4": [1041,592],
                 "1,5": [377,498], "2,5": [472,498], "3,5": [564,498], "4,5": [658,498], "5,5": [753,498], "6,5": [849,498], "7,5": [948,498], "8,5": [1041,498],
                 "1,6": [377,404], "2,6": [472,404], "3,6": [564,404], "4,6": [658,404], "5,6": [753,404], "6,6": [849,404], "7,6": [948,404], "8,6": [1041,404],
                 "1,7": [377,318], "2,7": [472,318], "3,7": [564,318], "4,7": [658,318], "5,7": [753,318], "6,7": [849,318], "7,7": [948,318], "8,7": [1041,318],
                 "1,8": [377,222], "2,8": [472,222], "3,8": [564,222], "4,8": [658,222], "5,8": [753,222], "6,8": [849,222], "7,8": [948,222], "8,8": [1041,222]}
        self.s ={"1,1": [329,824], "2,1": [425,824], "3,1": [520,824], "4,1": [615,824], "5,1": [709,824], "6,1": [805,824], "7,1": [900,824], "8,1": [995,824],
                 "1,2": [329,739], "2,2": [425,739], "3,2": [520,739], "4,2": [615,739], "5,2": [709,739], "6,2": [805,739], "7,2": [900,739], "8,2": [995,739],
                 "1,3": [329,644], "2,3": [425,644], "3,3": [520,644], "4,3": [615,644], "5,3": [709,644], "6,3": [805,644], "7,3": [900,644], "8,3": [995,644],
                 "1,4": [329,549], "2,4": [425,549], "3,4": [520,549], "4,4": [615,549], "5,4": [709,549], "6,4": [805,549], "7,4": [900,549], "8,4": [995,549],
                 "1,5": [329,453], "2,5": [425,453], "3,5": [520,453], "4,5": [615,453], "5,5": [709,453], "6,5": [805,453], "7,5": [900,453], "8,5": [995,453],
                 "1,6": [329,359], "2,6": [425,359], "3,6": [520,359], "4,6": [615,359], "5,6": [709,359], "6,6": [805,359], "7,6": [900,359], "8,6": [995,359],
                 "1,7": [329,265], "2,7": [425,265], "3,7": [520,265], "4,7": [615,265], "5,7": [709,265], "6,7": [805,265], "7,7": [900,265], "8,7": [995,265],
                 "1,8": [329,170], "2,8": [425,170], "3,8": [520,170], "4,8": [615,170], "5,8": [709,170], "6,8": [805,170], "7,8": [900,170], "8,8": [995,170]}
        self.color = color
        self.tipe = tipe
        if self.tipe == "Player":
            positionList = [[1,2], [2,2], [3,2], [4,2], [5,2], [6,2], [7,2], [8,2], #Player pawns on the second row
                            [1,1], [2,1], [3,1], [4,1], [5,1], [6,1], [7,1], [8,1]] #Player pieces on the first row
            if self.color == "black":
                positionList[12] = [5,1]
                positionList[11] = [4,1]
            elif self.color == "white":
                positionList[12] = [4,1]
                positionList[11] = [5,1]
        elif self.tipe == "Opponent":
            positionList = [[1,7], [2,7], [3,7], [4,7], [5,7], [6,7], [7,7], [8,7], #Enemy pawns on the seventh row
                            [1,8], [2,8], [3,8], [4,8], [5,8], [6,8], [7,8], [8,8]] #Enemy pieces on the eighth row
            if self.color == "black":
                positionList[12] = [4,8]
                positionList[11] = [5,8]
            elif self.color == "white":
                positionList[12] = [5,8]
                positionList[11] = [4,8]
        self.pawn1 = pawn.Pawn(positionList[0], self.tipe, self.m, self.s, self.color)
        self.pawn2 = pawn.Pawn(positionList[1], self.tipe, self.m, self.s, self.color)
        self.pawn3 = pawn.Pawn(positionList[2], self.tipe, self.m, self.s, self.color)
        self.pawn4 = pawn.Pawn(positionList[3], self.tipe, self.m, self.s, self.color)
        self.pawn5 = pawn.Pawn(positionList[4], self.tipe, self.m, self.s, self.color)
        self.pawn6 = pawn.Pawn(positionList[5], self.tipe, self.m, self.s, self.color)
        self.pawn7 = pawn.Pawn(positionList[6], self.tipe, self.m, self.s, self.color)
        self.pawn8 = pawn.Pawn(positionList[7], self.tipe, self.m, self.s, self.color)
        self.rook1 = rook.Rook(positionList[8], self.tipe, self.m, self.s, self.color)
        self.knight1 = knight.Knight(positionList[9], self.tipe, self.m, self.s, self.color)
        self.bishop1 = bishop.Bishop(positionList[10], self.tipe, self.m, self.s, self.color)
        self.king = king.King(positionList[11], self.tipe, self.m, self.s, self.color)
        self.queen = queen.Queen(positionList[12], self.tipe, self.m, self.s, self.color)
        self.bishop2 = bishop.Bishop(positionList[13], self.tipe, self.m, self.s, self.color)
        self.knight2 = knight.Knight(positionList[14], self.tipe, self.m, self.s, self.color)
        self.rook2 = rook.Rook(positionList[15], self.tipe, self.m, self.s, self.color)
        self.pieceList = [self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7, self.pawn8,
                          self.king, self.rook1, self.knight1, self.bishop1, self.queen, self.bishop2, self.knight2, self.rook2]
        
    def turn(self):
        if pyautogui.locateCenterOnScreen("clock_" + str(self.color) + ".png", region=(955,974,30,30), confidence=0.8) == None:
            return False
        else:
            return True

    def getPiecePositions(self):
        pos = []
        for piece in self.pieceList:
            pos.append(piece.boardPosition)
        return pos

    def determineEnemyMove(self, playerPiecePositions, enemyPiecePositions, playerPieceList):
        for piece in self.pieceList:
            if piece.checkForPiece() == False:
                q = piece.enemyFind(playerPiecePositions, enemyPiecePositions, playerPieceList)
                if self.tipe == "Opponent":
                    if q == "Queen":
                        a = queen.Queen(piece.boardPosition, self.tipe, self.m, self.s, self.color)
                        piece.boardPosition = [0,0]
                        self.pieceList.remove(piece)
                        self.pieceList.append(a)
                    if q == "Castle Right":
                        self.rook2.boardPosition = [(self.king.boardPosition[0] - 1), self.king.boardPosition[1]]
                        self.rook2.updatePositions()
                    if q == "Castle Left":
                        self.rook1.boardPosition = [(self.king.boardPosition[0] + 1), self.king.boardPosition[1]]
                        self.rook1.updatePositions()
                print(piece.detectionMessage)
                return True
        return False

    def updatePieceList(self):
        if self.pawn1.boardPosition != [0, 0]:
            if self.pawn1 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn1)
        if self.pawn2.boardPosition != [0, 0]:
            if self.pawn2 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn2)
        if self.pawn3.boardPosition != [0, 0]:
            if self.pawn3 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn3)
        if self.pawn4.boardPosition != [0, 0]:
            if self.pawn4 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn4)
        if self.pawn5.boardPosition != [0, 0]:
            if self.pawn5 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn5)
        if self.pawn6.boardPosition != [0, 0]:
            if self.pawn6 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn6)
        if self.pawn7.boardPosition != [0, 0]:
            if self.pawn7 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn7)
        if self.pawn8.boardPosition != [0, 0]:
            if self.pawn8 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.pawn8)
        if self.rook1.boardPosition != [0, 0]:
            if self.rook1 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.rook1)
        if self.rook2.boardPosition != [0, 0]:
            if self.rook2 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.rook2)
        if self.knight1.boardPosition != [0, 0]:
            if self.knight1 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.knight1)
        if self.knight2.boardPosition != [0, 0]:
            if self.knight2 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.knight2)
        if self.bishop1.boardPosition != [0, 0]:
            if self.bishop1 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.bishop1)
        if self.bishop2.boardPosition != [0, 0]:
            if self.bishop2 in self.pieceList:
                pass
            else:
                self.pieceList.append(self.bishop2)
        if self.queen.boardPosition != [0, 0]:
            if self.queen in self.pieceList:
                pass
            else:
                self.pieceList.append(self.queen)
        if self.king.boardPosition != [0, 0]:
            if self.king in self.pieceList:
                pass
            else:
                self.pieceList.append(self.king)
