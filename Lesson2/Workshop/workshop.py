# A simple program that takes the age of all passengers on a flight.
# The cost of a child's ticket is PLN 200, the cost of an adult ticket is PLN 400.
# If the passenger is an adult, he can also order alcohol (maximum 3 glasses of wine, each for PLN 10).
# There can be a maximum of 20 passengers. The program calculates the total revenue from tickets.
# If the age of the passenger is 0 or the maximum number of passengers has been reached,
# the program exits printing the summary:
# Total revenue, Number of Adult Passengers, Number of Children, Number of Wine Glasses.

wine_count = 0
children_count = 0
adult_count = 0
passengers_count = 0

while passengers_count < 20:
    print("Enter passenger age:")
    age = int(input())

    if age == 0:
        break
    elif age < 18:
        children_count += 1
        passengers_count += 1
        continue

    print("enter the number of glasses of wine")
    wine_current = int(input())
    if wine_current < 0 or wine_current > 3:
        print("wrong number of glasses of wine")
        continue

    wine_count += wine_current
    adult_count += 1
    passengers_count += 1

print("Adults: {}, Children: {}, Glasses of wine: {}, Revenue: {}".format(
  adult_count,
    children_count,
    wine_count,
    adult_count * 400 + children_count * 200 + wine_count * 10
))
