from typing import TypedDict, Unpack


class same_parity[T]:
    numners = "something"
    def __getitem__(self, index: int, /) -> T:
        return

    def append(self, element: T) -> None:
        return 1


def same_parity(list):
    if list[0] % 2 == 0:
        new_list = []
        for x, item in enumerate(list):
            if item % 2 ==0:
                new_list.append(item)
        return(new_list)
    else:
        new_list = []
        for x, item in enumerate(list):
            if item % 2 == 1:
                new_list.append(item)
        return(new_list)
    #a_list = kwargs['somelist']
    #return a_list

def main():
    test = same_parity([1,2,3,4,5,10,2])
    print(test)
    #print(test2)
    #reverse_string("astring")
    #parity_list = same_parity(1,2,3,4,5,6,7)
    #print(parity_list)


if __name__ == "__main__":
    main()