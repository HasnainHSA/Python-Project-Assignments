# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers)
print(f"The sum of the numbers is: {result}")
