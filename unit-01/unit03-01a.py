def sum_ints(a,b):
    #print(a,b)
    if a > b:
        return 0
    else:
        sum = (a + sum_ints(a + 1, b))
        print(sum)
        return sum

def cube(x):
    return x * x * x

def sum_cubes(a,b):
    #print(a,b)
    if a > b:
        return 0
    else:
        sum = (cube(a) + sum_cubes(a + 1, b))
        print(sum)
        return sum


def inc(n):
    return n + 1

def product_bak(term, a, next, b):
    if a > b:
        return 0
    else:
        term + a
        produc(term,inc(a), b) 


def product(x):
    return x * x

def sum_product(a,b):
    #print(a,b)
    if a > b:
        return 1
    else:
        sum = (a * (sum_product(a + 1, b)))
        print(sum)
        return sum

def main():
    sum_product(1,10)


print("Hello World")

if __name__ == "__main__":
    main()