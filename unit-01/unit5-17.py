#type Iterable[int] = list[int]
from typing import Iterable

def first[int](list: Iterable[int])-> int:
    print("test")
    return "test"

#class last_pair[T]:

def last_pair[int](list: Iterable[int]) -> int:
    #print(list)
    def last_pair_iter(a:list ,count:int) -> int:
        #print(a)
        #print(count)
        if a == []:
            return []
        if last_pair_iter(a[1:], count+1) == []:
            return a[0]
        else:
            return last_pair_iter(a[1:], count+1)
    
    return last_pair_iter(list,0)

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
    last_item = last_pair([23,72,149,34])
    print(last_item)


if __name__ == "__main__":
    main()