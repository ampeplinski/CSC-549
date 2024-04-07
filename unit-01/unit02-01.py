def A(x,y):
    if y == 0:
        #print("if y == 0:")
        return int(0)
    elif x == 0:
        #print("if x == 0:")
        #print(y)
        return int(2 * y)
    elif y == 1:
        #print("if y == 1:")
        return int(2)
    else:
        #print(x,y)
        result = A(int(x-1), A(x,int(y-1)))
        return result

def main():
    print("if x =0 and y = 20")
    print(A(0,20))
    print("if x =1 and y = 6")
    print(A(1,6))
    print("if x = 2 and y = 3")
    print(A(2,3))
    print("if x = 3 and y = 3")
    print(A(3,3))
   
    
print("Hello World")

if __name__ == "__main__":
    main()