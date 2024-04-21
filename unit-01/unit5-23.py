def add_two(x):
    #print(x)
    return x + 2

def cdr(list):
    try:
        item = list[1:]
    except Exception as ex:
        item = list[0]
    return item

def map(proc, items):

    if items == []:
        return []
        #return 0

    #print(items[0])
    list_of_lists = [proc(items[0]), map(proc,items[1:])]

    return list_of_lists
    #try:
    #    items[1:]
    #except Exception as ex:
    #    items[0])]

def test():
    print("test")

#def for_each(test(x)):
#   print("test2")

def main():
    print(map(add_two,[1,2,3]))
    


if __name__ == "__main__":
    main()