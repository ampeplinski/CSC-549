
def main():
    temp_outside = int(input("what is the temperature: "))

    if temp_outside < 50:
        print("heavy jacket required")
    elif temp_outside < 67:
        print("light jacket required")
    else:
        print("no jacket required")


print("Hello World")

if __name__ == "__main__":
    main()