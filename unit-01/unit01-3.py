def main():
    print("hello world")
    def procedure (a,b,c):
        user_input_list = [a,b,c]
        user_sorted_input = sorted(user_input_list)
        print(user_sorted_input)
        print(user_sorted_input[-1]**2 + user_sorted_input[-2]**2)

    procedure(2,3,1)

if __name__ == "__main__":
    main()