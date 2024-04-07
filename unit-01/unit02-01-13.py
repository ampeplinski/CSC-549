def prove_fib(n):
    phi = (1+(5**(1/2)))/2
    #print(f"phi = {phi}")
    psi = (1-(5**(1/2)))/2
    #print((phi**n) / (5**(1/2)))
    #print(f"psi = {psi}")
    print((phi ** n - psi ** n ) /  (5**(1/2)))
    n = n+1
    if n == 9:
        return n
    prove_fib(n)

def main():
    prove_fib(0)


print("Hello World")

if __name__ == "__main__":
    main()