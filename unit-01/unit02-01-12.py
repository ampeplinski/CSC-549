def f(a,b):
    print()

    if n[-1] == 1:
        print("\n")
        n.append(1)

    print(n)
    n.append(
        f(n))
        
#def main():
#    n= [1]
#    f(1,0)

def pascals_triangle(x):
    print(11 ** x)
    x +=1
    if x == 7:
        return x
    pascals_triangle(x)

def main():
    pascals_triangle(0)

    
print("Hello World")

if __name__ == "__main__":
    main()