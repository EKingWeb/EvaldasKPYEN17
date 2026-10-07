print("Hello World")



message = "Hello World"
print(message)

message = message + "World"
print(message)

#======================Basic data types==============
# Integer (number)
counter = 2
print(counter)

#Floating-point (number)
weight_sum = 10.5

print(weight_sum)

#String (text)
message = "Future Collars"
print(message)

#Multiline string
message2= """
line1
line2
line3
"""
print (message2)

#Boolean value - True/False

always_true = True
print(always_true)

always_false = False
print(always_false)

#none - nothing
nothing_here = None
print(nothing_here)

#====================Math operators===============

a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b % a) #Remainder from divide 10 % 3 -> 3+3+3+1 or
print(a ** b) #To power of (2*2*2)

#================Logical operators==================

print(a==b) #Equals to
print(a !=b) # Different to
print(a< b) #Less then
print(a <= b) #Less or equal to
print(a >= b) # Grater or equal
print(a > b) # Grater


#======================== AND, OR, NOT operators=======
# AND - both sides are True
print(False and False) #False
print(True and False) # False
print(False and False) #False
print(True and True) #True


# OR - at least one is true
print( False or False) #False
print(False or True) #True
print(True or False) #True
print(True or True) #True


# NOT - negation
print(not True) #False
print(not False) #True



#======================Variables in boolean context===========
print()
print()
print(bool(-1)) #True
print(bool(0)) #False
print(bool(1)) #True
print(bool(2)) #True
print(bool(0.1)) #True
print(bool("")) #False
print(bool("something")) #True
print(bool(" ")) #True
print(bool(None)) #None


#==============Checking variable type=======
a = "Text"
print(type(a)) #Check variable type








print(1 + 2) #Add like number
print("1"+ "2") #Concatinating the strings







message = "new message"
print(message)
massage = 2
print(massage)



#=====================Text operations=================

print("Hello"+" " + "World") #String concatenation
print("Hello" * 5) # Multiply a string
print("Text for %s formating %i" % ("a",2)) #Deprecated
a = "World"
print("My program prints hello{}".format(a))
print("My program prints hello {} in line {}" .format( a, 135))
print(f"Hello {a}!")


#=============Getting user input===================
print("What's your name?")
user_name = input()
print("Hello {}".format(user_name))

age = int(input("What is your age?"))
print("Your age is: {}".format(age))
print("In ten years you will be {} years old".format(age + 10))

#==================Additional text formating==========

print("1\n2\n3\n4\n5")# \n is to brake a line
print("My favorite book is \"The Alchemist\" John Doe") #Escape character
print("My favourite book is 'The Alchemist' John Doe")



