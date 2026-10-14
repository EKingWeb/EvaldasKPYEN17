import sys

a = 4
if a % 2 == 1:
    print ("a is odd")


if a % 2 == 0:
    print ("a is even")

a = True
b = False
c = a or b
if c:
    print ("This line will be executed")


c = ""
if c:
    print ("This line will be skipped")











a = 4
if a % 2 == 1:
    print("a is odd")

if a % 2 == 0:
    print("a is even")

    if a % 2 == 1:
        print("a is odd")
    else:
        print("a is even")


# Fizz  Buzz  FizzBuzz v1

    number = 9

    if number % 5 and number % 3:
        print(number)
    else:
        result = ""
        if number % 5 == 0:
            result += "Buzz"
        if number % 3 == 0:
            result += "Fizz"
        print(result)


#FizzBuzz v2

number = 9

if number % 5 == 0 or number % 3 == 0:
    result = ""
    if number % 5 == 0:
        result += "Buzz"
    if number % 3 == 0:
        result += "Fizz"
    print(result)
else:
    print(number)

#Fizzbuzz v3

if number % 15 == 0:
    print ("FizzBuzz")
elif number % 5 == 0:
    print ("Fizz")
elif number % 3 == 0:
    print ("Buzz")
else:
    print (number)

    # while (condition)
        # print the code
i = 0
while i < 10:
    print(f"Interation: {i}")
    i += 1

    #Prime numbers v1
number = 24
x = number // 2
factor = 0

while x > 1:
    if number % x == 0:
        print(f"{number} has factor  {x}")
    factor = x
    x = x - 1

if not factor:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")


    #Factorial
    counter = 0
    product = 1
    while counter < 10:
        counter += 1 #counter = counter + 1
        print("I'm calculating {}".format(counter))
        product *= counter #product = product  * counter
        if product > 1000:
            break#If condition satysfyed brakes the loop
        print("{}: {}".format(counter, product))

#Prime numbers v2
number = 24
x = number // 2
factor = 0

while x > 1:
    if number % x == 0:
        print(f"{number} is not prime")
        break
        x -= 1
    else:
        print(f"{number} is prime")


        #For loop - given number of times
        #line1
        #line2
        #line3


for i in range(10): #<10 not <=10
    print(i)


    for i in range(5, 10): #start, stop
        print(i)
print()
print()

for i in range(0, 10, 2): #start, stop , step
    print(i)

    for i in range(10, 0, -1): #Reverse steps
        print(i)


    print()
    print()


    for i in range(0, 10):
        if i ==5:
            continue #skipping rest of current interation
        if i != 7:
            pass
        else:
            continue
    print(i)


print(sys.argv[0]) #Reserved for program name
print(sys.argv[1]) #Argument from terminal (works only in terminal)
print(sys.argv[2]) #
print(sys.argv[3])

#db_password = "123"
