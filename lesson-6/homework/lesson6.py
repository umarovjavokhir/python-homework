# 1. Modify String with Underscores
def modify_string_with_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0
    for i, char in enumerate(txt):
        if char in vowels or (i > 0 and txt[i - 1] == "_"):
            result.append(char)
        else:
            count += 1
            result.append(char)
            if count == 3:
                result.append("_")
                count = 0
    if result[-1] == "_":
        result = result[:-1]
    return "".join(result)

# 2. Integer Squares Exercise
def integer_squares(n):
    for i in range(n):
        print(i**2)

# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop
def print_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1

# Exercise 2: Print the following pattern
def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number
def calculate_sum_of_numbers(n):
    sum_result = sum(range(1, n + 1))
    print(f"Sum is: {sum_result}")

# Exercise 4: Print multiplication table of a given number
def print_multiplication_table(num):
    for i in range(1, 11):
        print(num * i)

# Exercise 5: Display numbers from a list using a loop
def display_numbers_from_list():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for number in numbers:
        if number % 5 == 0 and number % 3 == 0:
            print(number)

# Exercise 6: Count the total number of digits in a number
def count_digits_in_number(n):
    print(len(str(n)))

# Exercise 7: Print reverse number pattern
def print_reverse_number_pattern():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Exercise 8: Print list in reverse order using a loop
def print_list_in_reverse():
    list1 = [10, 20, 30, 40, 50]
    for item in reversed(list1):
        print(item)

# Exercise 9: Display numbers from -10 to -1 using a for loop
def display_negative_numbers():
    for i in range(-10, 0):
        print(i)

# Exercise 10: Display message “Done” after successful loop execution
def display_done_message():
    for i in range(5):
        print(i)
    print("Done!")

# Exercise 11: Print all prime numbers within a range
def print_prime_numbers_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

# Exercise 12: Display Fibonacci series up to 10 terms
def print_fibonacci_series():
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Exercise 13: Find the factorial of a given number
def factorial_of_number(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! = {result}")

# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    return list(set(list1) ^ set(list2))

