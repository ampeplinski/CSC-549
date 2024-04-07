def fib(n,fib_list):
    #print(fib_list)
    phi = (1+(5**(1/2)))/2
    #print(f"phi = {phi}")
    psi = (1-(5**(1/2)))/2
    #print((phi**n) / (5**(1/2)))
    #print(f"psi = {psi}")
    #print("{:f}".format((phi ** n - psi ** n ) /  (5**(1/2))))
    fib_number = ("{:f}".format((phi ** n - psi ** n ) /  (5**(1/2))))
    fib_list.append(fib_number)
    n = n+1
    if n == 500:
        print(fib_list[-1])
        #return fib_list
    if n == 995:
        print(fib_list[-1])
        #return fib_list
    if n == 1000:
        print(fib_list[-1])
        return fib_list
    fib(n, fib_list)

def main():

    fibs_list = fib(0,[])
    print(fibs_list)


print("Hello World")

if __name__ == "__main__":
    main()