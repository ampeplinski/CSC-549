

def main():
    someset = {1,2,3}
    set_test = set([4,2,6])
    print(someset)
    print(type(someset))

    print(set_test)
    print(type(set_test))
    print(someset.union(set_test))


if __name__ == "__main__":
    main()  