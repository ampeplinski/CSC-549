def main():
    print("hello world")
    
    expressions = [
        10,
        5 + 3 + 4,
        9 - 1,
        6 / 2,
        (2 * 4) + (4 - 6)
    ]
    for i, result in enumerate(expressions, start=1):
        print(result)
    a = 3
    b = a + 1
    expressions_variables = [
        a,
        b,
        a + b + (a *b),
        a == b,
    ]

    for result in expressions_variables:
        print(result)

    if b > a and b < ( a * b):
        b
    else:
        a
    
    if a == 4:
        6
        if b == 4:
            6 + 7 + a
    else:
        25

    if b > a:
        b + 2
    else:
        a + 2

    if a > b:
        print("I surrender")

if __name__ == "__main__":
    main()