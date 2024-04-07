import time

def next(d):
    if d == 2:
        return 3
    else:
        return d + 2

def devides(a,b):
    print(b % a)
    if b % a == 0:
        return True
    else:
        return False

def find_divisor(n, test_d):
    print(n, test_d)
    if (test_d ** 2) > n:
        return n
    elif devides(test_d, n):
        return test_d
    else: 
        print("recursion")
        result = find_divisor(n, next(test_d))
        return result


def smallest_divisor(n):
    #print(n)
    smallest = find_divisor(n,2)
    return smallest

def main():
    start = time.time()

    result = smallest_divisor(7877)
    print(result)
    elapsed_time = time.time() - start

    print(elapsed_time)

print("Hello World")

if __name__ == "__main__":
    main()