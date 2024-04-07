def f(n):
    print(n)
    if n < 3:
       return n
    if n >= 3:
        result = f(n-1) + 2 * f(n-2) + 3 * f(n-3)
        return result



def main():
    f(10)
    
print("Hello World")

if __name__ == "__main__":
    main()