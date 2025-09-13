# We want to implement a mini-language to control a simple turtle-graphics system. The language consists of single-letter commands, some followed by a single number.For EG:
# the following input would draw a rectangle.

# p 2 # select pen 2
# D # Pen down
# W 2 == draw west 2cm
# N 1 == then north 1,
# E 2 === then east 2 ,
#  S 1 = then back to south , U = pen up. Implement the code that parses this language .It should be desingned so that it is simple to add new commands.

# The below python implementation will parse the mini-language for the  above lang:

class TurtleGraphicsParser:
    def __init__(self):
        self.commands = {  # Use a dict: to make adding new commands--this map commanda to their respective funtions.
            "P": self.select_pen, 
            "D": self.pen_down,
            "U": self.pen_up,
            "W": self.draw_west,
            "N": self.draw_north,
            "S": self.draw_south,
            "E": self.draw_east,

        } 
        self.pen = None
        self.pen_is_down = False

    def parse(self, instructions):
        for line in instructions:
            parts = line.split()
            command = parts[0] 
            value = int(parts[1]) if len(parts) > 1 else None
            if command in self.commands:
                self.commands[command](value)
            else:
                print(f"Unknown command: {command}")     

    def select_pen(self, value):
        self.pen = value
        print(f"Pen {value} selected.")

    def pen_down(self, value=None):
        self.pen_is_down = True
        print("Pen down.")

    def pen_up(self, value=None):
        self.pen_is_down = False
        print("Pen up.")

    def draw_west(self, value):
        if self.pen_is_down:
            print(f"Drawing west for {value}cm.")      

    def draw_north(self, value):
        if self.pen_is_down:
            print(f"Drawing North for {value}cm.")

    def draw_east(self, value):
        if self.pen_is_down:
            print(f"Drawing East for {value}cm.")

    def draw_south(self, value):
        if self.pen_is_down:
            print(f"Drawing South for {value}cm.")
#  Exmaple usage :
instructions = [
    "P 2",
    "D",
    "W 2",
    "N 1",
    "E 2",
    "S 1",
    "U"
]         
parser = TurtleGraphicsParser()
parser.parse(instructions)   