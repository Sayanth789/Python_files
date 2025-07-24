
import pyghelpers
import sys
import math # This is for the pie class.
import random
import pygame 
from pygame import gfxdraw
from pygame.locals import *

import pygwidgets



# Constants 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650

VIEW_BAR_VIEW = "bar"
VIEW_PIE_VIEW = "pie"
VIEW_TEXT_VIEW = "text"

MIN_TOTAL = 2
MAX_TOTAL = 12
MAX_TOTAL_PLUS_1 = MAX_TOTAL + 1

# InputNumber class.     --- This allow the user to only enter numbers.
# Demo of Inheritance.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tuple of legal editing keys
LEGAL_KEYS_TUPLE = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME, 
                    pygame.K_END,pygame.K_DELETE, pygame.K_BACKSPACE,
                    pygame.K_RETURN, pygame.K_KP_ENTER)

# Legal keys to be typed.
LEGAL_UNICODE_CHARS = ('0123456789.-')

# InputNumber inherits from inputText
class InputNumber(pygwidgets.InputText):
    def __init__(self, window, loc, value='', fontName=None, 
                 fontSize=24, width=200, textColor=BLACK, backgroundColor=WHITE,
                 focusColor=BLACK, initialFocus=False, nickName=None,callback=None,
                 mask=None, keepFocusOnSubmit=False, allowFloatingNumber=True,allowNegativeNumber=True):
        
        self.allowFloatingNumber = allowFloatingNumber
        self.allowNegativeNumber = allowNegativeNumber
# _____________________________________________________________________________________________________________________________________________________
        # Note here to add additinoal arguments we mentioned all the other parameters too: The same can be done without this drudgery.
# To do so we use the *args and the *kwargs.
# class InputNumber(pygwidgets.InputText):
#     def __init__(self, allowFloatingNumber=True,allowNegativeNumber=True, *args, **kwargs):
#          self.allowFloatingNumber = allowFloatingNumber
#          self.allowNegativeNumber = allowNegativeNumber 
#          super().___init__(*args, **kwargs)

# Here the args captures the positional arguments passed to the constructor.
# **kwargs captures any keyword arguments

# _______________________________________________________________________________________________________________________________________________________
        # Call the __init__method of our base class.
        super().__init__(window, loc, value, fontName, fontSize,
                         width, textColor, backgroundColor,
                         nickName, callback, mask, keepFocusOnSubmit)
        
        # Override handleEvent so we can filter for proper keys

    def handleEvent(self, event):
        if (event.type == pygame.KEYDOWN):
                # If it's not an editing or numeric key ignore it.
                # Unicode value is only present on key down.
            allowableKey = ((event.key in LEGAL_KEYS_TUPLE) or
                                (event.unicode in LEGAL_UNICODE_CHARS))
            if not allowableKey:
                return False
                
            if event.unicode == "-":  # User typed a minus sign
                if not self.allowNegativeNumber:
                        # If no negative, don't pass it through 
                    return False
                if self.cursorPosition > 0:
                    return False  # Can't put minus sign after 1st char.
                if '-' in self.text:
                        return False  # can't enter a second minus sign
            if event.unicode == ".":
                if not self.allowFloatingNumber:
                        # If no flaots, don't pass the period through
                    return False   
                if "." in self.text:
                    return False  # Can't enter a second period
                
            # Allow the key to go to the  base class
        result = super().handleEvent(event)
        return result

    
    def getValue(self):
        userString = super().getValue()
        try:
            if self.allowFloatingNumber:
                returnValue = float(userString)
            else: returnValue = int(userString)  # if floating is not supported we convert the user input to integer.
        except ValueError:
            raise ValueError("Entry is not a number, needs to have atleast one digit.")        
        return returnValue


# Model class
SIDES_PER_DIE = 6
SIDES_PER_DIE_PLUS_ONE  = SIDES_PER_DIE + 1

class Model():
    def __init__(self):
        self.nRounds = 0
        self.rollsDict = {} # an empty dict!
        self.percentsDict = {}  # Another empty dict.

    def generateRolls(self, nRounds):
        self.nRounds = nRounds
        self.rollsDict = {}  # an empty dict:
        for total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):   # Initialize all to zero.
            self.rollsDict[total] = 0

        # Roll two dice, add them up, increment the count in the dict.
        for roundNumber in range(0, self.nRounds):
            die1 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)  # dies generating random output.
            die2 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            theSum = die1 + die2

            self.rollsDict[theSum] = self.rollsDict[theSum] + 1
            # This line updates the dict: that keeps count of how many times each possible total(from rolling 2 dice) has occurred. 
            # The updated value is stored back into the dictionary at the key theSum.

        # Calculate and save percentage in a dict:
        self.percentsDict = {}
        for rollTotal , count in self.rollsDict.items():
            thisPercent = count / self.nRounds 
            self.percentsDict[rollTotal] = thisPercent

    # All current views call this method to get all the data.
    def getRoundsRollPercents(self):
        return self.nRounds, self.rollsDict, self.percentsDict
    
    # The methods below aren't used right now, but are available for new views
    def getNumberOfRounds(self):
        return self.nRounds
    def getRolls(self):
        return self.rollsDict
    def getPercents(self):
        return self.percentsDict
    
# Piechart class.
# -----------------------------------------------------------------------------
CENTER_X = 300
CENTER_Y = 300
RADIUS = 200
RADIUS_MINUS_1 = RADIUS - 1
BLACK = (0, 0, 0)

class pieView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel
        self.legendFieldsDict = {}
        y = 160 
        # create the legend fields
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            gray = (index * 20, index * 20, index * 20)
            oLegendField = pygwidgets.DisplayText(window, (550, y), value=str(index), fontSize=32, textColor=gray)
            self.legendFieldsDict[index] = oLegendField
            y = y + 25  # vertical spacing

    def update(self, ):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollPercents()        

        self.nRounds = nRounds
        self.percentsDict = percentsDict
        self.resultsDict = resultsDict
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            # Could use if we want to display it later.
            # ṛollCount = resultsDict[index]
            percent = percentsDict.get(index, 0)

            oLegendField = self.legendFieldsDict[index]

            # Build percent as a string with one decimal digit
            percent = '{:.1%}'.format(percent)
            oLegendField.setValue(str(index) + ': ' + percent)

    def drawFilledArc(self, centerX, centerY, radius, degrees1, degrees2, color):
        """ This method generates a list of points that are used to create
        a filled polygon representing an arc in the circle. We'll use the
        angles passed in and a little trig to figure out the points in the arc.
        """        
        centerTuple = (centerX, centerY)
        nPointsToDraw = int(degrees2 - degrees1)
        if nPointsToDraw == 0:
            return # nothing to draw
        # Both degrees parameters need to be converted to radians for calculating points
        radians1 = math.radians(degrees1)
        radians2 = math.radians(degrees2)
        radiansDiff = (radians2 - radians1) / nPointsToDraw

        # Start and end with the center point of the circle.
        pointsList = [centerTuple]
        # Determine the points on the edge of the arc.
        for pointNumber in range(nPointsToDraw + 1):
            offset = pointNumber * radiansDiff
            x = centerX + (radius * math.cos(radians1 + offset))
            y = centerY + (radius * math.sin(radians1 + offset))
            pointsList.append((x, y))

        pointsList.append(centerTuple)

        pygame.gfxdraw.filled_polygon(self.window, pointsList, color)
        # if one like black lines around the each arc, uncommend the next line.
        #pygame.gfxdraw.polygon(self.window, pointsList, BLACK)

# Draw the slice of the pie (arc) for every roll total
    def draw(self):
        startAngle = 0.0
        for index in range(MIN_TOTAL,MAX_TOTAL_PLUS_1):
            percent = self.percentsDict.get(index, 0)    
            endAngle = startAngle + (percent * 360)
            gray = (index * 20, index * 20, index * 20)
            self.drawFilledArc(CENTER_X, CENTER_Y, RADIUS_MINUS_1, startAngle, endAngle, gray)
            self.legendFieldsDict[index].draw()

            startAngle = endAngle # set up for next wedge
        pygame.draw.circle(self.window, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)


# Text view class.
class TextView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel

        totalText = ["Roll total", ""]
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            totalText.append(rollTotal)
        self.oTotalDisplay = pygwidgets.DisplayText(self.window, (200, 135), totalText,fontSize=36, width=120, justified="right")
        self.oCountDisplay = pygwidgets.DisplayText(self.window, (320, 135), fontSize=36, width=120, justified="right")
        self.oPercentDisplay = pygwidgets.DisplayText(self.window, (440, 135), fontSize=36, width=120, justified="right")

    def update(self):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()       
        # The precentDict will return the percentage of the dice occurence 

        countList = ["Count", ""]  # extra empty string for a blank line.
        percentList = ["Percent", ""]
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            count = resultsDict[rollTotal]
            percent = percentsDict[rollTotal]

            countList.append(count)

            # Build percent as a string with one decimal digit.
            percent = '{:.1%}'.format(percent)
            percentList.append(percent)

        self.oCountDisplay.setValue(countList)    
        self.oPercentDisplay.setValue(percentList)

    def draw(self):
        self.oTotalDisplay.draw()
        self.oCountDisplay.draw() 
        self.oPercentDisplay.draw()

MAX_BAR_HEIGHT = 300
BAR_BOTTOM = 390
BAR_WIDTH = 30
BAR_CLOLR = (128, 128, 128)
COLUMN_LEFT_START  = 30
COLUMN_OFFSET = 55

# Bin class (note: It is necessary for the Bar class to implement.)
class Bin():
    def __init__(self, window, binNumber):
        self.window = window
        self.pixelsPerCount = MAX_BAR_HEIGHT

        self.left = COLUMN_LEFT_START + (binNumber * COLUMN_OFFSET)
        self.oBinLabel = pygwidgets.DisplayText(window, (self.left + 3,BAR_BOTTOM + 12), binNumber, fontName='arial', fontSize=24, width=25, justified="center") 
        self.oBinCount = pygwidgets.DisplayText(window, (self.left - 5, BAR_BOTTOM +  50), '', fontName='arial', fontSize=18, width=50, justified='center')
        self.oBinPercent = pygwidgets.DisplayText(window, (self.left - 5, BAR_BOTTOM + 80), '', fontName='arial', fontSize=18, width=50,justified="center")

    def update(self, nRounds, count, percent):
        self.oBinCount.setValue(count)
        percent = '{:.1%}'.format(percent)
        self.oBinPercent.setValue(percent)

        # Force float here, use int when drawing rects.
        # calculate the real height, multiply by 2 to make it look better.ALl bars will certainly be less than 50%.
        if nRounds > 0:
            self.nPixelsPerTrial = float(MAX_BAR_HEIGHT) / nRounds
        else:
            self.nPixelsPerTrial = 0
            print("Warning: nRounds is zero.No trials have been run yet.")    
        barHeight = int(count * self.nPixelsPerTrial) * 2
        self.rect = pygame.Rect(self.left, BAR_BOTTOM - barHeight, BAR_WIDTH, barHeight)

    def draw(self):
        pygame.draw.rect(self.window, BAR_CLOLR, self.rect, 0)
        self.oBinLabel.draw()
        self.oBinCount.draw()
        self.oBinPercent.draw()

# The BarView class.
class BarView():
    def __init__(self, window, oModel):
        self.window = window 
        self.oModel = oModel

        self.oRollTotal = pygwidgets.DisplayText(self.window, (50, 406),"Roll total:", fontName='arial', fontSize=16, justified="right",width=80)
        self.oCount = pygwidgets.DisplayText(self.window, (50, 441), 'Count:',fontName='arial', fontSize=16, justified='right',width=80)
        self.oPercent = pygwidgets.DisplayText(self.window, (50, 471), 'Percent:', fontName='arial',fontSize=16, justified='right', width=80)

        self.oBinsDict = {}
        # possible rolls go from 2 to 12
        for rollTotal in range(MIN_TOTAL,MAX_TOTAL_PLUS_1):  # + 1 to get the correct range
            oBin = Bin(self.window, rollTotal)
            self.oBinsDict[rollTotal] = oBin

    def update(self):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollPercents()       
        for rollTotal in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
           thisResult = resultsDict.get(rollTotal, 0)
           thisPercent = percentsDict.get(rollTotal, 0.0)
           oBin = self.oBinsDict[rollTotal]
           oBin.update(nRounds, thisResult, thisPercent)

    def draw(self):
        self.oRollTotal.draw()
        self.oCount.draw()
        self.oPercent.draw()
        for oBin in self.oBinsDict.values():
            oBin.draw()        


# The controller class. Which has dependecy on  pieView, TextView,  BarView, InputNumber,and Constants.
BACKGROUND_COLOR = (0, 222, 222)
N_ROUNDS_AT_START = 2500
LIGHT_GRAY = (255, 255, 255)


class Controller():
    def __init__(self, window):
        self.window = window
        # Instantiating the Model
        self.oModel = Model()

        # Instantiating the world.
        self.oBarView = BarView(self.window, self.oModel)
        self.oPieView = pieView(self.window, self.oModel)
        self.oTextView = TextView(self.window, self.oModel)

        # Defaults to bar view at start.
        self.oView = self.oBarView

        self.oTitleDisplay = pygwidgets.DisplayText(window, (330, 30), "Roll THe Dice!", fontName='monospace', fontSize=34)
        self.oQuitButton = pygwidgets.TextButton(window, (20, 595), "Quit", width=100, height=35)
        self.oRoudsDisplay = pygwidgets.DisplayText(window, (260, 600), "Number of rolls:", fontName='monospace', fontSize=28, width=150, justified='right')
        self.oRoundsInput = InputNumber(window, (430, 600), value=str(N_ROUNDS_AT_START),fontName='monospace',fontSize=28, width=100, initialFocus=True, keepFocusOnSubmit=True, allowFloatingNumber=False, allowNegativeNumber=False)
        self.oRollDiceButton = pygwidgets.TextButton(window, (690, 595), 'Roll Dice', width=100, height=35)
        self.oDiceImage = pygwidgets.Image(window, (650, 15),"images/twoDice.png")
        # This area is reserved for the different views
        self.viewArea = pygame.Rect(45, 70, WINDOW_WIDTH - 90, WINDOW_HEIGHT - 200)
        self.oBarButton =  pygwidgets.TextRadioButton(window, (80, 540), "View", "Bar chart", value=True,fontSize=36)
        self.oPieButton = pygwidgets.TextRadioButton(window, (620, 540), "View", "Pie chart", fontSize=36)
        self.oTextButton = pygwidgets.TextRadioButton(window, (620, 540), "View", "Text", fontSize=36)

        # Generate the starting data, and tell the view about the results.
        self.generateNewData()
        self.oView.update()

    def handleEvent(self, event):
        if self.oQuitButton.handleEvent(event):
            pygame.quit()
            sys.exit()

        if self.oRollDiceButton.handleEvent(event) or self.oRoundsInput.handleEvent(event):
            self.generateNewData()
            self.oView.update()

        if self.oBarButton.handleEvent(event):
            self.oView = self.oBarView
            self.oView.update()
        elif self.oPieButton.handleEvent(event):
            self.oView = self.oPieView
            self.oView.update()
        elif self.oTextButton.handleEvent(event):
            self.oView = self.oTextView
            self.oView.update()

    def generateNewData(self):
        """
        This method gets the no: of rolls from the input field and after checking for errors,
        tells the model to generate new data based on the no: rolls the user asked for.
        
        """            
        try:
            nRounds = self.oRoundsInput.getValue()
        except Exception as msg:
            pyghelpers.textYesNoDialog(self.window, pygame.Rect(170, 180, 430, 170), msg, "OK", None, backgroundColor=LIGHT_GRAY)
            return 
        if nRounds < 100:
            pyghelpers.textYesNoDialog(self.window, pygame.Rect(170, 180, 430, 170), "For meaningful results, \n enter 100 or more.", backgroundColor=LIGHT_GRAY)
            return 
   
    def draw(self):
        # Draw everything the Controller is responsible for (everything outside the black rectangle)
        self.window.fill(BACKGROUND_COLOR)

        self.oBarButton.draw()
        self.oPieButton.draw()
        self.oTextButton.draw()
        self.oRollDiceButton.draw()
        self.oRoundsInput.draw()
        self.oRollDiceButton.draw()
        self.oQuitButton.draw()

        pygame.draw.rect(self.window, BLACK, self.viewArea, 3)
        self.oView.draw()   # tell  the current view to draw itself

FRAMES_PER_SECOND = 30

# Initializing the world
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Roll Them Dice.")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Loading assets: images, sounds ..etc.
# Initializing variables , Initializing the controller object

oController = Controller(window)

# Loop forever
while True:
    # Check for and handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # pass all events to the Controller 
        oController.handleEvent(event)

    # Do any 'frame per' actions
   # clear the window (let the Controller do it) , Draw the window elements
    oController.draw()

        # Update the window
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
    # makes the pygame wait.

# ____________________________________________________________________________________________________________________
