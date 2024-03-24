def main():
    def improve(guess, x):
        average_of = (x + guess)/2
        print(x, guess)
        print(average_of)
        return average_of

    def good_enough(guess,x):
        # print(guess**2)
        # print(abs((guess**2) - x))
        if int(abs((guess**2) - x)) < 0.001:
            # print(abs((guess**2) - x))
            return True, abs((guess**2) - x)
        else:
            return False, abs((guess**2) - x)

    def sqrt_iter(guess:int = 1, x=0):
        # print(guess)
        # print(type(guess))
        # print(x)
        good_enough_result, older_guess = good_enough(guess,x)
        #print(older_guess)
        if good_enough_result:
            return guess
        else:
            sqrt_iter(improve(older_guess,x),x)

    def sqrt(x):
        print(x)
        return(sqrt_iter(1,x=x))

    print(sqrt(9))

if __name__ == "__main__":
    main()