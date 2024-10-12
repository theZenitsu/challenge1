numbers = [1, 2, 5, 7, 10, 4]
odd_numbers = list(filter(lambda x: x % 2 != 0 , numbers))
print(f"new list with odd numbers: {odd_numbers}")