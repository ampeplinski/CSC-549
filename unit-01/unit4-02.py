from random import randint
class Fraction[T]:
    def __init__(self, numerator:int, denominator:int, /) -> T:
        self._numerator = numerator
        self._denominator = denominator

    def display(self):
        print(f"{self._numerator}/{self._denominator}")
    
    def add(self, fraction):
        self._num = self._numerator * fraction.getdenom() + fraction.getnum() * self._denominator
        self._dom = self._denominator * fraction.getdenom()
        print(f"{self._num}/{self._dom}")
        
    def getdenom(self):
        return self._denominator

    def getnum(self):
        return self._numerator

def main():
    choice = None
    F1 = Fraction(1,2)
    F1.display()
    F2 = Fraction(1,4)
    F2.display()
    F3 = F1.add(F2)
    
if __name__ == "__main__":
    main()