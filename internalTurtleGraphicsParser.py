# The turtleGraphicsParser was an external domain language, now we implement it as an internal language.

# This approach avoids the sophisticated passing logic by simply writting starightforward functions for  each command and wrapping them in a context (A class in this case).


class TurtleGraphics:
    def __init__(self):
        self.pen = None
        self.pen_is_down = False

    def p(self, pen_number):
        """" select the pen number."""    
        self.pen = pen_number
        print(f"Pen {pen_number} Selected.")

    def d(self):
        """ Put the pen down"""
        self.pen_is_down = True
        print(f"Pen Down")

    def u(self):
        """ Lift the pen up"""
        self.pen_is_down = False
        print('Pen Up')

    def w(self, distance):
        """ Move west for a given distance"""        
        if self.pen_is_down:
            print(f"Drawing west for {distance}cm.")
        else:
            print(f"Moving west for a {distance}cm without drawing.")

    def n(self, distance):
        """ Move north for a given distance"""            
        if self.pen_is_down:
            print(f"Drawing north for {distance}cm.")
        else:
            print(f"moving north for a {distance}cm  without drawing.") 

    def s(self, distance):           
        """ Move south for a given distance """
        if self.pen_is_down:
            print(f"Drawing south for a {distance}cm.")
        else:
            print(f"Moving south for a {distance}cm without drawing")
    
    def e(self, distance):
        """ Move east for a given distance"""
        if self.pen_is_down:
            print(f"Drawing east a {distance}cm")
        else:
            print(f"Moving east a {distance}cm without drawing")

# Example usage                
graphics = TurtleGraphics()
graphics.p(2)   # select pen 2


graphics.d()  #Pen down
graphics.w(5)
graphics.n(1)
graphics.e(5)
graphics.s(1)
graphics.u()    # Pen is up.


