def numbers(numbers):
    for number in numbers:
        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print(f"{number} is zero.")






nums = [10, -1, 0, 5, -3]
numbers(nums)
