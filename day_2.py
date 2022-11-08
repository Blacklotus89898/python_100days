# tip calculator
#f string
"""height, score = 2, 24
string = f"your score is {score} , your height is {height}"
print(string)"""

def tip_calculator(bill, people, tips):
    tax = 1.15
    total = int(bill)*tax
    share = total*(1+int(tips)/100)/int(people)
    tip = round(share, 2)
    print(f"Each person should pay {tip}")

#tip_calculator(input("Bill?"),input("NUmber of people?"), input("Percentae of tip?"))
"""x = "heka world"
y = input("enter y:")
print(x>y)"""

"""number = [0, 32,3224,0,242]
number = number.pop()
print(number)
print(number + [5])"""
"""
numbers = [1]
print(numbers[-1])
print(numbers[0])
x = numbers[-1] + numbers[0]
print(x+4)"""

"""numbers = [1,4-1,0,2,0]
for i in range(len(numbers)):
    print(numbers[i] <  numbers[i+1])"""

"""def no_return():
    print("return none")
    return 
print(no_return())"""

"""sumi = 0
for x in range(1,5,2):
    for y in range(x, x+10, 2):
        sumi += 1 
print(sumi)"""

"""def s(x, y, z):
    if not(x==3 or y ==4):
        print("osnvs")
    else:
        print("advks")"""

"""def jack(s):
    print(x)

x = input("gearif")
jack(x)"""

numbers = [1,2,3,4,5]
for i in numbers:
    i*=5
numbers[2] = 9001
numbers.sort()

numbers = numbers + [numbers[-2]]
print(numbers)