class TurtleGraphicsParser:
    def __init__(self):
        # Use a dict to map commands to their handler functions
        self.commands = {
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
            command = parts[0].upper()   # normalize to uppercase
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
        print("Pen down")

    def pen_up(self, value=None):
        self.pen_is_down = False
        print("Pen up")

    def draw_west(self, value):
        if self.pen_is_down:
            print(f"Drawing west for {value} cm.")

    def draw_north(self, value):
        if self.pen_is_down:
            print(f"Drawing north for {value} cm.")

    def draw_east(self, value):
        if self.pen_is_down:
            print(f"Drawing east for {value} cm.")

    def draw_south(self, value):
        if self.pen_is_down:
            print(f"Drawing south for {value} cm.")


# Example usage
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
