from random import randint
class Dice[T]:
    def __init__(self, sides:int, /) -> T:
        self._sides = sides

    def roll(self):
        print(randint(1,self._sides))

def main():

    D6 = Dice(6)
    print("rolling D6")
    D6.roll()
    D6.roll()
    D6.roll()
    D10 = Dice(10)
    print("rolling D10")
    D10.roll()
    D10.roll()
    D10.roll()
print("Hello World")

if __name__ == "__main__":
    main()