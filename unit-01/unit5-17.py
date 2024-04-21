#type Iterable[int] = list[int]
from typing import Iterable

def first[int](list: Iterable[int])-> int:
    print("test")
    return "test"

#class last_pair[T]:

def length[int](list: Iterable[int]) -> int:
    #print(list)
    def length_iter(a:list ,count:int) -> int:
        #print(a)
        #print(count)
        if a == []:
            return []
        if length_iter(a[1:], count+1) == []:
            return a[0]
        else:
            return length_iter(a[1:], count+1)
    
    return length_iter(list,0)

"""
def cons(1,2):
    def car(x):
        return x
    def cdr(x):
        return x

def fisrt_item(1,2):
    return 1

def rest_of_list(1,2):
    return 2

def last_pair(list):

def length(items):
"""


def main():
    last_item = length([23,72,149,34])
    print(last_item)


if __name__ == "__main__":
    main()