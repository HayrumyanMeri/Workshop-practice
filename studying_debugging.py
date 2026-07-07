def find_largest(numbers):
    largest = numbers[0]  # <-- There is a bug here

    for number in numbers:
        if number > largest:
            largest = number

    return largest


nums = [-8, -12, -3, -20]

result = find_largest(nums)
print("Largest number:", result)

