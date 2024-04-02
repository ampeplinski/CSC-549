from datetime import datetime
from datetime import timedelta

def main():
    
    years_old = int(input("How old are you?: "))
    birth_year = int(input("what year were you born?:"))
    day_of_birth = int(input("What day were you born?:"))
    month_of_birth = int(input("what month were you born?:"))
    
    
    dob = datetime(year=birth_year, month=month_of_birth, day=day_of_birth)
    print(f"you said you were born on {dob:%B %d, %Y}")
    print(f"You said you are {years_old}.")

    now_time = datetime.now()
    difference_age = now_time - dob
    print(difference_age.days)
    print(difference_age.seconds)
    
print("Hello World")

if __name__ == "__main__":
    main()