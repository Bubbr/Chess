import pygame, sys
from pygame.locals import *
from chess import *

width, height = 416, 416
turn = 0

sprites = {
    "sqrW":pygame.image.load("./images/squareW.png"),
    "sqrB":pygame.image.load("./images/squareB.png"),
    "pawnW":pygame.image.load("./images/pawnW.png"),
    "pawnB":pygame.image.load("./images/pawnB.png"),
    "knightW":pygame.image.load("./images/knightW.png"),
    "knightB":pygame.image.load("./images/knightB.png"),
    "bishopW":pygame.image.load("./images/bishopW.png"),
    "bishopB":pygame.image.load("./images/bishopB.png"),
    "rookW":pygame.image.load("./images/rookW.png"),
    "rookB":pygame.image.load("./images/rookB.png"),
    "kingW":pygame.image.load("./images/kingW.png"),
    "kingB":pygame.image.load("./images/kingB.png"),
    "queenW":pygame.image.load("./images/queenW.png"),
    "queenB":pygame.image.load("./images/queenB.png"),
    "icon":pygame.image.load("./images/icon.png")
           }

pieces = {
    "pW1":piece(2, "pW1", sprites["pawnW"]), "pW2":piece(2, "pW2", sprites["pawnW"]), "pW3":piece(2, "pW3", sprites["pawnW"]), "pW4":piece(2, "pW4", sprites["pawnW"]), "pW5":piece(2, "pW5", sprites["pawnW"]), "pW6":piece(2, "pW6", sprites["pawnW"]), "pW7":piece(2, "pW7", sprites["pawnW"]), "pW8":piece(2, "pW8", sprites["pawnW"]),
    "pB1":piece(3, "pB1", sprites["pawnB"]), "pB2":piece(3, "pB2", sprites["pawnB"]), "pB3":piece(3, "pB3", sprites["pawnB"]), "pB4":piece(3, "pB4", sprites["pawnB"]), "pB5":piece(3, "pB5", sprites["pawnB"]), "pB6":piece(3, "pB6", sprites["pawnB"]), "pB7":piece(3, "pB7", sprites["pawnB"]), "pB8":piece(3, "pB8", sprites["pawnB"]),
    "kW1":piece(4, "kW1", sprites["knightW"]), "kW2":piece(4, "kW2", sprites["knightW"]),
    "kB1":piece(5, "kB1", sprites["knightB"]), "kB2":piece(5, "kB2", sprites["knightB"]),
    "bW1":piece(6, "bW1", sprites["bishopW"]), "bW2":piece(6, "bW2", sprites["bishopW"]),
    "bB1":piece(7, "bB1", sprites["bishopB"]), "bB2":piece(7, "bB2", sprites["bishopB"]),
    "rW1":piece(8, "rW1", sprites["rookW"]), "rW2":piece(8, "rW2", sprites["rookW"]),
    "rB1":piece(9, "rB1", sprites["rookB"]), "rB2":piece(9, "rB2", sprites["rookB"]),
    "kW":piece(10, "kW", sprites["kingW"]),
    "kB":piece(11, "kB", sprites["kingB"]),
    "qW":piece(12, "qW", sprites["queenW"]),
    "qB":piece(13, "qB", sprites["queenB"])
           }

board = {
    "a8":boardTile("a8", [0, 0], piece=pieces["rB1"], sprite=sprites["sqrW"]),
    "a7":boardTile("a7", [0, 52], piece=pieces["pB1"], sprite=sprites["sqrB"]),
    "a6":boardTile("a6", [0, 104], sprite=sprites["sqrW"]),
    "a5":boardTile("a5", [0, 156], sprite=sprites["sqrB"]),
    "a4":boardTile("a4", [0, 208], sprite=sprites["sqrW"]),
    "a3":boardTile("a3", [0, 260], sprite=sprites["sqrB"]),
    "a2":boardTile("a2", [0, 312], piece=pieces["pW1"], sprite=sprites["sqrW"]),
    "a1":boardTile("a1", [0, 364], piece=pieces["rW1"], sprite=sprites["sqrB"]),

    "b8":boardTile("b8", [52, 0], piece=pieces["kB1"], sprite=sprites["sqrB"]),
    "b7":boardTile("b7", [52, 52], piece=pieces["pB2"], sprite=sprites["sqrW"]),
    "b6":boardTile("b6", [52, 104], sprite=sprites["sqrB"]),
    "b5":boardTile("b5", [52, 156], sprite=sprites["sqrW"]),
    "b4":boardTile("b4", [52, 208], sprite=sprites["sqrB"]),
    "b3":boardTile("b3", [52, 260], sprite=sprites["sqrW"]),
    "b2":boardTile("b2", [52, 312], piece=pieces["pW2"], sprite=sprites["sqrB"]),
    "b1":boardTile("b1", [52, 364], piece=pieces["kW1"], sprite=sprites["sqrW"]),

    "c8":boardTile("c8", [104, 0], piece=pieces["bB1"], sprite=sprites["sqrW"]),
    "c7":boardTile("c7", [104, 52], piece=pieces["pB3"], sprite=sprites["sqrB"]),
    "c6":boardTile("c6", [104, 104], sprite=sprites["sqrW"]),
    "c5":boardTile("c5", [104, 156], sprite=sprites["sqrB"]),
    "c4":boardTile("c4", [104, 208], sprite=sprites["sqrW"]),
    "c3":boardTile("c3", [104, 260], sprite=sprites["sqrB"]),
    "c2":boardTile("c2", [104, 312], piece=pieces["pW3"], sprite=sprites["sqrW"]),
    "c1":boardTile("c1", [104, 364], piece=pieces["bW1"], sprite=sprites["sqrB"]),

    "d8":boardTile("d8", [156, 0], piece=pieces["qB"], sprite=sprites["sqrB"]),
    "d7":boardTile("d7", [156, 52], piece=pieces["pB4"], sprite=sprites["sqrW"]),
    "d6":boardTile("d6", [156, 104], sprite=sprites["sqrB"]),
    "d5":boardTile("d5", [156, 156], sprite=sprites["sqrW"]),
    "d4":boardTile("d4", [156, 208], sprite=sprites["sqrB"]),
    "d3":boardTile("d3", [156, 260], sprite=sprites["sqrW"]),
    "d2":boardTile("d2", [156, 312], piece=pieces["pW4"], sprite=sprites["sqrB"]),
    "d1":boardTile("d1", [156, 364], piece=pieces["qW"], sprite=sprites["sqrW"]),

    "e8":boardTile("e8", [208, 0], piece=pieces["kB"], sprite=sprites["sqrW"]),
    "e7":boardTile("e7", [208, 52], piece=pieces["pB5"], sprite=sprites["sqrB"]),
    "e6":boardTile("e6", [208, 104], sprite=sprites["sqrW"]),
    "e5":boardTile("e5", [208, 156], sprite=sprites["sqrB"]),
    "e4":boardTile("e4", [208, 208], sprite=sprites["sqrW"]),
    "e3":boardTile("e3", [208, 260], sprite=sprites["sqrB"]),
    "e2":boardTile("e2", [208, 312], piece=pieces["pW5"], sprite=sprites["sqrW"]),
    "e1":boardTile("e1", [208, 364], piece=pieces["kW"], sprite=sprites["sqrB"]),

    "f8":boardTile("f8", [260, 0], piece=pieces["bB2"], sprite=sprites["sqrB"]),
    "f7":boardTile("f7", [260, 52], piece=pieces["pB6"], sprite=sprites["sqrW"]),
    "f6":boardTile("f6", [260, 104], sprite=sprites["sqrB"]),
    "f5":boardTile("f5", [260, 156], sprite=sprites["sqrW"]),
    "f4":boardTile("f4", [260, 208], sprite=sprites["sqrB"]),
    "f3":boardTile("f3", [260, 260], sprite=sprites["sqrW"]),
    "f2":boardTile("f2", [260, 312], piece=pieces["pW6"], sprite=sprites["sqrB"]),
    "f1":boardTile("f1", [260, 364], piece=pieces["bW2"], sprite=sprites["sqrW"]),

    "g8":boardTile("g8", [312, 0], piece=pieces["kB2"], sprite=sprites["sqrW"]),
    "g7":boardTile("g7", [312, 52], piece=pieces["pB7"], sprite=sprites["sqrB"]),
    "g6":boardTile("g6", [312, 104], sprite=sprites["sqrW"]),
    "g5":boardTile("g5", [312, 156], sprite=sprites["sqrB"]),
    "g4":boardTile("g4", [312, 208], sprite=sprites["sqrW"]),
    "g3":boardTile("g3", [312, 260], sprite=sprites["sqrB"]),
    "g2":boardTile("g2", [312, 312], piece=pieces["pW7"], sprite=sprites["sqrW"]),
    "g1":boardTile("g1", [312, 364], piece=pieces["kW2"], sprite=sprites["sqrB"]),

    "h8":boardTile("h8", [364, 0], piece=pieces["rB2"], sprite=sprites["sqrB"]),
    "h7":boardTile("h7", [364, 52], piece=pieces["pB8"], sprite=sprites["sqrW"]),
    "h6":boardTile("h6", [364, 104], sprite=sprites["sqrB"]),
    "h5":boardTile("h5", [364, 156], sprite=sprites["sqrW"]),
    "h4":boardTile("h4", [364, 208], sprite=sprites["sqrB"]),
    "h3":boardTile("h3", [364, 260], sprite=sprites["sqrW"]),
    "h2":boardTile("h2", [364, 312], piece=pieces["pW8"], sprite=sprites["sqrB"]),
    "h1":boardTile("h1", [364, 364], piece=pieces["rW2"], sprite=sprites["sqrW"]),
    }




palette = [pygame.Color(255, 69, 0), pygame.Color(255, 255, 255)]

pygame.init()
#pygame.mixer.music.load("./music/prueba.mp3")
#pygame.mixer.music.play()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ajedrez")


#pygame.draw.polygon(win, palette[0], ((200, 175), (175, 200), (190, 200), (190, 225), (210, 225), (210, 200), (225, 200), (200, 175)))

def move(a, b):
    a2 = a.piece
    b2 = b.piece
    a.piece = b2
    b.piece = a2

def update():
    global moves
    for tile in board:
        board[tile].update()
        win.blit(board[tile].sprite, board[tile].pos)
        if board[tile].piece:
            win.blit(board[tile].piece.sprite, board[tile].pos)
        try:
            if board[tile].moved:
                print(moves[-2].piece.team)
                print("[*]", moves[-2].name, "to", moves[-1].name)
                move(moves[-2], moves[-1])
        except:
            pass



while True:
    update()
    
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
