numbers = [10, 15, 22, 33, 40, 55, 60]
even_numbers = [num for num in numbers if num % 2 == 0]
sum_of_evens = sum(even_numbers)
print(f"the numbers are: {numbers}")
print(f"Even Numbers: {even_numbers}")
print(f"Sum of Even Numbers: {sum_of_evens}")