# Importng packages
import pygame
from pygame.locals import *
import pygwidgets
import sys

PIXELS_PER_MOVE = 5

SOUTH = "south"
NORTH = "north"
WEST = 'west'
EAST = "east"

class Player():
    nPixelsPerMove = 5

    def __init__(self, window, loc):
        self.window = window
        self.loc = loc
        walkSouthTuple = (('images/walkF0.png', .1), ('images/walkF1.png', .1),('images/walkF2.png', .1),('images/walkF3.png', .1),('images/walkF4.png', .1),('images/walkF5.png', .1),('images/walkF6.png', .1),('images/walkF7.png', .1),('images/walkF8.png', .1)) 
        walkNorthTuple =  (('images/walkB0.png', .1), ('images/walkB1.png', .1),('images/walkB2.png', .1),('images/walkB3.png', .1),('images/walkB4.png', .1),('images/walkB5.png', .1),('images/walkB6.png', .1),('images/walkB7.png', .1),('images/walkB8.png', .1)) 
        walkWestTuple = (('images/walkL0.png', .1), ('images/walkL1.png', .1),('images/walkL2.png', .1),('images/walkL3.png', .1),('images/walkL4.png', .1),('images/walkL5.png', .1),('images/walkL6.png', .1),('images/walkL7.png', .1),('images/walkL8.png', .1)) 
        walkEastTuple = (('images/walkR0.png', .1), ('images/walkR1.png', .1),('images/walkR2.png', .1),('images/walkR3.png', .1),('images/walkR4.png', .1),('images/walkR5.png', .1),('images/walkR6.png', .1),('images/walkR7.png', .1),('images/walkR8.png', .1)) 

        self.oWalkAnimations = pygwidgets.AnimationCollection(window, self.loc, {SOUTH:walkSouthTuple, NORTH:walkNorthTuple,WEST:walkWestTuple, EAST:walkEastTuple}, SOUTH, loop=True, autoStart=False)

        self.direction = SOUTH
        self.keysDownList = []
        self.isMoving = False

    def getRect(self):
        return self.oWalkAnimations.getRect()

    def getCenterLoc(self):
        theRect = self.getRect()
        theCenter = theRect.center
        return theCenter
    def getDirections(self):
        return self.direction

    def handelEvent(self, event):
        if event.type == pygame.KEYDOWN:   # Is the player pressed any key?
            if event.key == pygame.K_DOWN:
                self.keysDownList.append(SOUTH)   # adds the SOUTH to the list.
                self.directions = SOUTH
                self.oWalkAnimations.replace(SOUTH)
                self.oWalkAnimations.start()
                self.isMoving = True
            elif event.key == pygame.K_UP:
                self.keysDownList.append(NORTH)
                self.direction = NORTH
                self.oWalkAnimations.replace(NORTH)
                self.oWalkAnimations.start()
                self.isMoving = True
            elif event.key == pygame.K_LEFT:
                self.keysDownList.append(WEST)
                self.direction = WEST
                self.oWalkAnimations.replace(WEST)
                self.oWalkAnimations.start()
                self.isMoving = True
            elif event.key == pygame.K_RIGHT:
                self.keysDownList.append(EAST)
                self.direction = EAST
                self.oWalkAnimations.replace(EAST)
                self.oWalkAnimations.start()
                self.isMoving = True        

        elif event.type == pygame.KEYUP:  # triggers when user releases a  key on the keyboard.
            if event.key == pygame.K_DOWN:
                self.keysDownList.remove(SOUTH)
            elif event.key == pygame.K_UP:
                self.keysDownList.remove(NORTH)
            elif event.key == pygame.K_LEFT:
                self.keysDownList.remove(WEST)
            elif event.key == pygame.K_RIGHT:
                self.keysDownList.remove(EAST)

            if len(self.keysDownList) == 0:
                self.oWalkAnimations.stop()
                self.isMoving = False            
            else:
                self.direction = self.keysDownList[0]  # Just use the first keydown in the list.
                self.oWalkAnimations.replace(self.direction)
                self.oWalkAnimations.start()
                self.isMoving = True

    def update(self):            
        if self.isMoving:
            if self.direction == WEST:
                self.loc[0] = self.loc[0] - Player.nPixelsPerMove  # Moving left means decresing X coord:

            elif self.direction == EAST:
                self.loc[0] = self.loc[0] + Player.nPixelsPerMove  # moving right means increasing X coord:

            elif self.direction == NORTH:
                self.loc[1] = self.loc[1] - Player.nPixelsPerMove # moving Up means decreadig Y coor:

            elif self.direction == SOUTH:
                self.loc[1] = self.loc[1] + Player.nPixelsPerMove  # moving down means increasing Y coord:

            self.oWalkAnimations.update()
        return self.loc[0], self.loc[1]

    def draw(self):
        self.oWalkAnimations.draw()



SCREEN_WIDTH = 1060
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (220, 220, 220)

def myFunction(theNickname):
    if theNickname is None:
        print("In myFunction, animation ended")
    else:
        print("In myFunction, the animation with the nickname", theNickname,  "ended")

class CallBackTest():
    def myMethod(self, theNickname):
        if theNickname is None:
            print("in myMethod, animation ended")
        else:
            print("In myMethod, the animation with the nickname", theNickname,  "ended")
   
    # Initialize the world.
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

dinosaurAnimList = [('images/f1.png', .1),('images/f2.png', .1),('images/f3.png', .1),('images/f4.png', .1),('images/f5.png', .1),('images/f6.png', .1),('images/f7.png', .1),('images/f8.png', .1),('images/f9.png', .1),('images/f10.png', .1),('images/f11.png', .1), ('images/f12.png', .1),('images/f13.png', .1),('images/f14.png', .1),('images/f15.png', .1),('images/f16.png', .1),('images/f17.png', .1)]

TRexAnimationList = [('images/f1.gif', .1),('images/f2.gif', .1),('images/f3.gif', .1),('images/f4.gif', .1),('images/f5.gif', .1),('images/f6.gif', .1),('images/f7.gif', .1),('images/f8.gif', .1),('images/f9.gif', .1),('images/f10.gif', .1)]

oCallBackTest = CallBackTest() # instantiate a test object
oTitleText = pygwidgets.DisplayText(window, (110, 80), "Animations       spriteSheetAnimations", fontSize=32)

oDinosaurAnimation = pygwidgets.Animation(window, (22, 145),dinosaurAnimList, autoStart=True, loop=False, callBack=myFunction, nickname='Dinosaur')
oPlayButton = pygwidgets.TextButton(window, (20, 240), "play")
oPauseButton =  pygwidgets.TextButton(window, (20, 280), "pause")  
oStopButton = pygwidgets.TextButton(window, (20, 320), "Stop")
oLoopCheckBox =  pygwidgets.TextCheckBox(window, (20, 370), "Loop", value=False)
oShowCheckBox = pygwidgets.TextCheckBox(window, (20, 400), "show", value=True)

oTRexAnimation = pygwidgets.Animation(window, (180, 140), TRexAnimationList, autoStart=False, loop=False, nIterations=3, callBack=oCallBackTest.myMethod)

oInstructionText = pygwidgets.DisplayText(window, (160, 320), "(Click image to activate)")

oEffectAnimation = pygwidgets.SpriteSheetAnimation(window, (400, 150), "images/effect_010.png", 35, 192, 192, .1, autoStart=True, loop=True)

oWalkAnimation = pygwidgets.SpriteSheetAnimation(window, (460, 335), 'images/male_walkcycle.png', 36, 64, 64, (.1, .1, .1, .1, .1, .1, .1,.1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3,.1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3),autoStart=False, loop=False)

if hasattr(pygwidgets, 'getVersion'):
    version_info = pygwidgets.getVersion()
    if isinstance(version_info, str) and '1.0.3' in version_info:
        oPlayer = pygwidgets.DisplayText(window, (740, SCREEN_HEIGHT * .333), "Available in pygwidgets 1.1", fontSize=24)
        oRunningAnimation = pygwidgets.DisplayText(window, 740, SCREEN_HEIGHT * .666, "Availble in pygwidgets 1.1", fontSize=24)
        oCollectionsInstructionText1 = pygwidgets.DisplayText(window, (750, 300), "")
        oCollectionsInstructionText2 = pygwidgets.DisplayText(window, (750, 500), "")
        animCollectionsAvailable = False


else:
    oPlayer = Player(window, (800, SCREEN_HEIGHT * .333))
    # Build a dictionary of SpriteSheet animations, Each key value pair looks like this:
    # <someLey>: (<imagePath>, <nImages>, <width>, <height>, <durationOrDurationList>)     
    animationCollectionDict = {"right": ('images/runRight.png', 10, 30, 40, .1), "left": ("images/runLeft.png", 10, 30, 40, .1 )}

    # Create a SpriteAnimationCollection object with multiple sprite sheet animations
    oRunAnimation = pygwidgets.SpriteSheetAnimationCollection(window, (810, SCREEN_HEIGHT * .75), animationCollectionDict, "right", autoStart=True, loop=True)
    oCollectionsInstructionText1 = pygwidgets.DisplayText(window, (750, 250), '(Press left, up, right, down to move)')
    oCollectionsInstructionText2 = pygwidgets.DisplayText(window, (750, 420), '(Press "l" to run left, or "r" to run right)')
    animCollectionsAvailable = True

    oStartButton = pygwidgets.TextButton(window, (440, 400), "Start")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if oPlayButton.handleEvent(event):
                oDinosaurAnimation.start()
            if oPauseButton.handleEvent(event):
                oDinosaurAnimation.pause()
            if oStopButton.handleEvent(event):
                oDinosaurAnimation.stop()
            if oLoopCheckBox.handleEvent(event):
                currentLoopState = oDinosaurAnimation.getLoop()
                oDinosaurAnimation.setLoop(not currentLoopState)
            if oShowCheckBox.handleEvent(event):
                showState = oDinosaurAnimation.getVisible()
                if showState:
                    oDinosaurAnimation.hide()
                else:
                    oDinosaurAnimation.show()
            if oStartButton.handleEvent(event):
                oWalkAnimation.start()
            if oDinosaurAnimation.handleEvent(event):
                oDinosaurAnimation.start()
            if oTRexAnimation.handleEvent(event):
                oTRexAnimation.start()

            if event.type == pygame.KEYDOWN:
                # Allow the user to press left and right keys to switch animations.
                if event.key == pygame.K_1 and animCollectionsAvailable:
                    oRunAnimation.replace('left')
                elif event.key == pygame.K_r and animCollectionsAvailable:
                    oRunAnimation.replace("right")
                else:
                    oPlayer.handelEvent(event)  # sent it the player animation.
                      
            elif event.type == pygame.KEYUP:   
                oPlayer.handelEvent(event)

        if oTRexAnimation.update():
            print('In main code - TRex animation  ended')
        if oDinosaurAnimation.update():
            print("In main code - Dinauser animation ended")
        if oEffectAnimation.update():
            print('In main code - Effect animation  ended')
        if oWalkAnimation.update():
            print("In main code - Walk  animation ended")

        if animCollectionsAvailable:
            playerX, playerY = oPlayer.update()
            oRunAnimation.update()                

        window.fill(BGCOLOR)

        # Drawing all window events.
        oTitleText.draw()
        oDinosaurAnimation.draw()
        oPlayButton.draw()
        oPauseButton.draw()
        oStopButton.draw()
        oLoopCheckBox.draw()
        oShowCheckBox.draw()
        oTRexAnimation.draw()
        oInstructionText.draw()
        oEffectAnimation.draw()
        oWalkAnimation.draw()
        oStartButton.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)





