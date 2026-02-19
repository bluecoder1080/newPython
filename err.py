def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    average = total / len(numbers)
    return average

nums = [10, 20, 30, 40, 50]
avg = calculate_average(nums)
print("Average is: " + str(avg))
