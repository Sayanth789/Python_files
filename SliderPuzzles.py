# Constants:
import time
import pygame
import random
import pygwidgets
import pyghelpers
import sys
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (200, 0, 200)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)

# Squares and tiles are the same size
SQUARE_HEIGHT = 100
SQUARE_WIDTH = 100
NSQUARES = 16
STARTING_OPEN_SQUARE_NUMBER = NSQUARES - 1

# Tile class.

class Tile():
    """
    A Tile contains a tile number and an associated image.

    """
    font = pygame.font.SysFont(None, 60)

    def __init__(self, window, tileNumber):
        self.window = window
        self.tileNumber = tileNumber

        # Use drawing calls to create a surface for each tile, For the empty tile; just a filled tile. For all others, draw a circle, and center a number in it.
        # Alternatively we could load image tiles from a folder.
        # self.image = pygame.image.load("images/tile" + str(self.tileNumber + 1) + '.png')
         
        surface = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
        if self.tileNumber == STARTING_OPEN_SQUARE_NUMBER: # draw empty image
            surface.fill(GRAY)
            pygame.draw.rect(surface, BLACK, pygame.Rect((0, 0,SQUARE_WIDTH, SQUARE_HEIGHT)) , 2) # black border around everything.
        else:
            surface.fill(PURPLE)
            pygame.draw.rect(surface, BLACK, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)), 2)  # Black border around everything. 
            
            centerX = SQUARE_WIDTH // 2
            centerY = SQUARE_HEIGHT // 2
            pygame.draw.circle(surface, YELLOW, (centerX, centerY), 35)
            numberAsImage = Tile.font.render(str(self.tileNumber + 1), True, BLACK)
            widthOfNumber = numberAsImage.get_width()
            leftPos = (SQUARE_WIDTH - widthOfNumber) // 2
            heightOfNumber = numberAsImage.get_height()
            topPos = (SQUARE_WIDTH - heightOfNumber) // 2
            surface.blit(numberAsImage, (leftPos, topPos))
        
        self.image  = surface    

    def getTileNumber(self):
        return self.tileNumber    
    
    def draw(self, loc):
        self.window.blit(self.image, loc)

# Class Square:
class Square():
    """
    A square is a square area of the game board, in the application window.
    Each square has a location, rectangle, a tuple of legal moves, and a Tile that is drawn on the square.
    For each user move, the game tells  the clicked on Square to exchange its Tile with the blank(empty space).
    
    """
    def __init__(self, window, left, top, squareNumber, legalMovesTuple):
        self.window = window
        self.rect = pygame.Rect(left, top, SQUARE_WIDTH, SQUARE_HEIGHT)
        self.squareNumber = squareNumber
        self.legalMovesTuple = legalMovesTuple
        self.loc = (left, top)
        self.reset()

    def reset(self):
        # Create starting Tile associtated with this square.
        self.oTile = Tile(self.window, self.squareNumber) 

    def isTileInProperPlace(self):
        tileNumber = self.oTile.getTileNumber()    
        return (self.squareNumber == tileNumber)

    def getLegalMoves(self):
        return self.legalMovesTuple
    
    def clickedInside(self, mouseLoc):
        hit = self.rect.collidepoint(mouseLoc)
        return hit
    
    def getSquareNumber(self):
        return self.squareNumber
    
    def switch(self, oOtherSquare):
        # Switch the Tiles associated with two Squre objects.
        self.oTile, oOtherSquare.oTile = oOtherSquare.oTile, self.oTile

    def draw(self):
        # Tell the Tile to draw at the Square's location
        self.oTile.draw(self.loc)


class Game():
    START_LEFT = 35
    START_TOP = 30

    def __init__(self, window):   # This is the constructor.
        self.window = window
        """
        The game board is made up of 4 rows and 4 colomns - 16 squars, with 15 labelled images
        (1 to 15) and a blank square image. However, because python lists and tuples start at zero, the sqaures are 
        internally numaberd (indexed) 0 to 15:

        (A square is an area of the window, each contains a tile, which is movable.)
        The following is a dict of squareNumber:tuple. Each tuple contains all moves (vartical and horizontal neighbors) that can  switch with this square.
        For eg: for square 0, only Squares 1 and 4 are the legal moves.
        
        """
        LEGAL_MOVES_DICT = {
            0:(1, 4), 
            1:(0, 2, 5),
            2:(1, 3, 6),
            3:(2, 7),
            4:(0, 5, 8),
            5:(1, 4, 6, 9),
            6:(2, 5, 7, 10),
            7:(3, 6, 11),
            8:(4, 9 ,12),
            9:(5, 8, 10, 13),
            10:(6, 9, 11, 14),
            11:(7, 10, 15),
            12:(8, 13),
            13:(9, 12, 14),
            14:(10, 13, 15),
            15:(11, 14)

        }
        yPos = Game.START_TOP 
        self.squaresList = []

        # creating a list of Square objects.
        for row in range(0, 4):
            xPos = Game.START_LEFT
            for col in range(0, 4):
                squareNumber = (row * 4) + col # Computes the position of the individual grid( eg: for row 3, and col3: the squareNumber is 3 * 4 + 3 = 15):It represent the position of the sqaure in a flattened 1D list.
                legalMovesTuple = LEGAL_MOVES_DICT[squareNumber]
                oSquare = Square(self.window, xPos, yPos, squareNumber , legalMovesTuple)
                # here the top -> yPos, left-> xPos, squareNumber == squareNumber, legalMovesTuple == legalMovesTuple.
                self.squaresList.append(oSquare)
                xPos = xPos + SQUARE_WIDTH
            yPos = yPos + SQUARE_HEIGHT
        self.soundTick = pygame.mixer.Sound("Sounds/tick.wav")      
        self.soundApplause = pygame.mixer.Sound("Sounds/applause.wav")
        self.soundNope = pygame.mixer.Sound("Sounds/nope.wav")

        self.playing = False
        self.startNewGame()

    def startNewGame(self):
        # Tell all Sqares to reset themselves.
        for oSquare in self.squaresList:
            oSquare.reset()

        self.oOpenSquare = self.squaresList[STARTING_OPEN_SQUARE_NUMBER]       

        for i in range(0,  200): # make 200 arbitrary moves to randomize.
            legalMovesForThisTile = self.oOpenSquare.getLegalMoves()

            nextMoveNumber = random.choice(legalMovesForThisTile)
            oSquare = self.squaresList[nextMoveNumber]

            #  switch the randomly chosen Square & open Square.
            self.switch(oSquare, playMoveSound=False)
        self.playing = True

    def getClick(self, clickLoc):
        if  not self.playing:
            return  # Game is over, waiting for Restart button.

        for oSquare in self.squaresList:
            if oSquare.clickedInside(clickLoc):
                sqaureNumber = oSquare.getSquareNumber()
                # Print("Got a mouseDown on square number:", squareNumber)
                legalMovesForOpenSqaureTuple = self.oOpenSquare.getLegalMoves()
                legalMove = sqaureNumber in legalMovesForOpenSqaureTuple

                if legalMove:
                    self.switch(oSquare, playMoveSound=True)
                else:# Illegal move (not next to the open space)
                    self.soundNope.play()
                return
                
    # Switch the Tile  of a given Square with the open square.
    def switch(self, oSquareToSwitch, playMoveSound=False):
        oSquareToSwitch.switch(self.oOpenSquare)
        # Re-assign the open square.
        self.oOpenSquare = oSquareToSwitch

        if playMoveSound:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False
        
        for oSquare in self.squaresList:
            if not oSquare.isTileInProperPlace():
                return False

        # All in proper place, game over.
        self.playing = False
        self.soundApplause.play()
        return True
    def getGamePlaying(self):
        return self.playing
    
    def stopPlaying(self):
        self.playing = False
    
    def draw(self):
        for oSquare in self.squaresList:
            oSquare.draw()    
        


# Main_SliderPuzzleCountDown

WINDOW_WIDTH = 470
WINDOW_HEIGHT = 560
FRAMES_PER_SECOND = 30

# import pygame


class CountDownTimer:
    def __init__(self, totalSeconds):
        self.totalSeconds = totalSeconds
        self.startTime = None
        self.running = False

    def start(self):
        self.startTime = time.time()
        self.running = True

    def stop(self):
        self.running = False

    def getTimeLeft(self):
        if not self.running:
            return max(0, self.totalSeconds - int(time.time() - self.startTime))
        return max(0, self.totalSeconds - int(time.time() - self.startTime))

    def getTimeInHHMMSS(self, numDigits=2):
        secondsLeft = self.getTimeLeft()
        minutes = secondsLeft // 60
        seconds = secondsLeft % 60
        if numDigits == 1:
            return f"{minutes}:{seconds}"
        return f"{minutes:02}:{seconds:02}"

    def ended(self):
        return self.getTimeLeft() <= 0


class CountUpTimer:
    def __init__(self):
        self.startTime = None
        self.running = False

    def start(self):
        self.startTime = time.time()
        self.running = True

    def stop(self):
        self.running = False

    def getElapsedTime(self):
        if not self.running:
            return 0
        return int(time.time() - self.startTime)

    def getTimeInHHMMSS(self):
        elapsed = self.getElapsedTime()
        minutes = elapsed // 60
        seconds = elapsed % 60
        return f"{minutes:02}:{seconds:02}"

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Slider puzzle")

    clock = pygame.time.Clock()
    oGame = Game(window)

    timer = CountUpTimer()
    timer.start()

    font = pygame.font.SysFont(None, 50)
    gameOver = False 

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and not gameOver:    
                oGame.getClick(event.pos)
                if oGame.checkForWin():
                    timer.stop()
                    gameOver = True
        window.fill(GRAY)
        oGame.draw()

            # Timer text display
        if isinstance(timer, CountDownTimer):
            timeStr = timer.getTimeInHHMMSS()
            if timer.ended():
                timeStr = "Time's Up!"
                oGame.stopPlaying()
                gameOver = True
        else:
            timeStr = timer.getTimeInHHMMSS()
        timerText = font.render(timeStr, True, WHITE)
        window.blit(timerText, (WINDOW_WIDTH// 2 - timerText.get_width() // 2,WINDOW_HEIGHT - 50))

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)

if __name__ == "__main__":
    main() 
            



    