"""print('Hello\nWorld') #swtiching variable
city = input("Which city were you born in? ")
date = input("What was your birthdate? ")
print("You are born in "+city+"the "+date)
city, date = date, city"""

i, j = int(input("col")), int(input("rol"))
#j = int(input("rol"))

for n in range(1, i+1):
    for m in range(1,j+1):
        print(m*n, end = "\t")
    print("\n")