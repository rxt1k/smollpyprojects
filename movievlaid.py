# checks if a person can watch movie or not based on age and permission
age = int(input("Enter your age: "))

if (age<=13):
    permission = input("Do you have your parents permission yes/no: ")
    if (age <= 13 and permission == "yes") or age>=18:
        print("you can watch movie")
    else:
        ("you cannot watch the movie")
else:
    print("invalid")