from typing import Iterable
import time

def cons(x,y):
    return [x,y]

def cdr(pair):
    return pair

def reverse_test4(list):
    print(list)
    newlist = []
    length = len(list)
    count = length
    for a in range(length):
        print(newlist)
        newlist.append(list[count-1])
        count -= 1
    return newlist

def reverse_test3[int](list: Iterable[int]) -> int:
    #print(list)
    def reverse_iter(a):
        time.sleep(1)
        try:
            if a ==[]:
                return []
            newlist = reverse_test3(a[1:])
            print(newlist)
            try:
                return newlist.append[a[0]]
            except Exception as ex:
                #print(a)
                return a

        except Exception as ex:
            print(ex)
    return reverse_iter(list)

def reverse_test2[int](list: Iterable[int]) -> int:
    #print(list)
    def reverse_iter(a:list) -> list:
        #print(a)
        try:
            test = [a[0]].append(reverse_iter(a[1:]))
            print(test)
            return test
        except Exception as ex:
            return a[0]
        if reverse_iter(a[1:]) == []:
            return a[1:].append(a[0])
        if a == []:
            return []
        else:
            return [a[0]].append(reverse_iter(a[1:]))
    
    return reverse_iter(list)


def reverse_test[list](list: list) -> list:
    print(list)
    if list == []:
        return []
    return [list[0]].append(reverse_test(list[1:]))


def reverse_string(string):
    lst = string.split()
    lst.reverse()
    for x in lst:
        print(x)


def main():
    #reverse_string("astring")
    reversed_list = reverse_test4([1,4,9,16,25])
    print(reversed_list)


if __name__ == "__main__":
    main()