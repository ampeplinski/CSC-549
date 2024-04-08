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


def isPrime(p):

    smallest_div = smallest_divisor(p)

    if p == smallest_div:
        return True
    else:
        return False

def areOfACircle(r):
    pie = 3.14

    area_num = pie * (r ** 2)

    return area_num



def genCircleInfo(r):
    circle_dict = {}

    area_num = areOfACircle(r)

    p_result = isPrime(r)
    
    circle_dict['radius'] = r
    circle_dict['area'] = area_num
    circle_dict['calPrime'] = p_result

    return circle_dict 

def main():
    result = genCircleInfo(7877)
    for k, v in result.items():
        print(k,v)


print("Hello World")

if __name__ == "__main__":
    main()