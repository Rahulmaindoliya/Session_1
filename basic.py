
age = 25  # int (integer)
price = 19.99  # float (decimal)
name = "Alex"  # str (string)
is_student = True  # bool (boolean)

print("--- 1. Variables ---")
print(f"Name: {name}, Age: {age}, Price: ${price}, Student: {is_student}")


# 2. DATA STRUCTURES

# List (Ordered, mutable/changeable)
fruits = ["apple", "banana", "cherry"]

# Tuple (Ordered, immutable/cannot change)
coordinates = (10, 20)

# Dictionary (Key-value pairs)
person = {"name": "Alex", "role": "Developer"}

# Set (Unique values only)
unique_numbers = {1, 2, 3, 3, 4}  # Duplicate '3' will be removed

print("\n--- 2. Data Structures ---")
print("List:", fruits)
print("Dictionary Role:", person["role"])


# 3. CONDITIONS (IF / ELIF / ELSE)

print("\n--- 3. Conditions ---")
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")



# 4. LOOPS (FOR & WHILE)

print("\n--- 4. Loops ---")

# For loop through a list
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While loop
count = 1
while count <= 3:
    print(f"Count is: {count}")
    count += 1


# 5. FUNCTIONS

print("\n--- 5. Functions ---")


def calculate_total(item_price, quantity):
    total = item_price * quantity
    return total


# Calling the function
final_cost = calculate_total(10, 3)
print(f"Total Cost: ${final_cost}")