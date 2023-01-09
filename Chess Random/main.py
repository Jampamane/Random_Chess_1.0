import pyautogui
import keyboard
import winsound
import chess
import random
import queen

def sound():
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

#Takes a screenshot of the time clock to determine what color the player is
def color():
    if pyautogui.locateCenterOnScreen("clock_black.png", region=(955,974,30,30), confidence=0.8, grayscale=True) != None:
        return "black"
    elif pyautogui.locateCenterOnScreen("clock_white.png", region=(955,974,30,30), confidence=0.8, grayscale=True) != None:
        return "white"
    else:
        return color()

def findPiece(pieceList, playerPiecePositions, enemyPiecePositions, enemyPieceList):
    if len(pieceList) == 0:
        print("You lose!")
        quit()
    randomPiece = random.choice(pieceList)
    pieceBool = randomPiece.movePiece(playerPiecePositions, enemyPiecePositions, enemyPieceList)
    if pieceBool == False:
        pieceList.remove(randomPiece)
        findPiece(pieceList, playerPiecePositions, enemyPiecePositions, enemyPieceList)
    elif pieceBool == "Queen":
        a = queen.Queen(randomPiece.boardPosition, randomPiece.tipe, randomPiece.mouseDictionary, randomPiece.screenshotDictionary, randomPiece.color)
        pieceList.remove(randomPiece)
        randomPiece.boardPosition = [0,0]
        pieceList.append(a)
        return True
    elif pieceBool == True:
        return True


def main():
    #Calls the color class to create a player object and an enemy object of the appropriate color
    PlayerCol = color()
    a = chess.Player("Player", PlayerCol)
    if PlayerCol == "black":
        b = chess.Player("Opponent", "white")
        b.determineEnemyMove(a.getPiecePositions(), b.getPiecePositions(), a.pieceList)
    else:
        b = chess.Player("Opponent", "black")
    findPiece(a.pieceList, a.getPiecePositions(), b.getPiecePositions(), b.pieceList)
    a.updatePieceList()
    while True:
        if keyboard.is_pressed("p"):
            quit()
        if keyboard.is_pressed("l"):
            b.determineEnemyMove(a.getPiecePositions(), b.getPiecePositions(), a.pieceList)
            findPiece(a.pieceList, a.getPiecePositions(), b.getPiecePositions(), b.pieceList)
            a.updatePieceList()
        if a.turn() == True:
            b.determineEnemyMove(a.getPiecePositions(), b.getPiecePositions(), a.pieceList)
            findPiece(a.pieceList, a.getPiecePositions(), b.getPiecePositions(), b.pieceList)
            a.updatePieceList()

if __name__ == "__main__":
    main()