from random import randint

class Segments[T]:
    def __init__(self, start_x:int, start_y:int, end_x:int, end_y:int, /) -> T:
        self._startx = start_x
        self._starty = start_y
        self._endx = end_x
        self._endy = end_y

    def make_segment(self):
        self._make_point("start")
        self._make_point("end")
        
    
    def print_point(self, p):
        print("\n")
        print("(", end="")
        print(self.x_point(p), end="")
        print(",",end="")
        print(self.y_point(p), end="")
        print(")")
        
    def _start_segment(self):
        self._startx = randint(0,10)
        self._starty = randint(0,10)

    def _end_segment(self):
        self._endx = randint(0,10)
        self._endy = randint(0,10)

    def _make_point(self, order):
        if order == "start":
            self._start_segment()
        if order == "end":
            self._end_segment()

    def x_point(self, x):
        if x == "start":
            return self._startx
        if x == "end":
            return self._endx

    def y_point(self, y):
        if y == "start":
            return self._starty
        if y == "end":
            return self._endy

    def mid_point(self):
        midx = (self._startx + self._endx) / 2
        midy = (self._starty + self._endy) / 2
        return mid_point

def main():
    segment = Segments(1,2,7,8)
    segment.print_point("start")
    segment.print_point("end")
    segment.make_segment()
    segment.print_point("start")
    segment.print_point("end")

if __name__ == "__main__":
    main()