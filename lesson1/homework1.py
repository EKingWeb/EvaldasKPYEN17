# 1. Prompt the user for the required information
print("Enter the recipient's name:")
recipient_name = input()

print("Enter the year of birth:")
year_of_birth = int(input())

print("Enter a short personalized message:")
personalized_message = input()

print("Enter the sender's name:")
sender_name = input()

# 2. Calculate the age based on the current year and year of birth
current_year = 2026
age = current_year - year_of_birth

# 3. Generate the personalized birthday card using the exact requested format
print() # Prints an empty line for spacing
print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!")
print()
print(personalized_message)
print()
print("With love and best wishes,")
print(sender_name)