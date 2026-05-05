def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

num = [1,2,3,4]

total = sum_numbers(num)
print(total)

def sum_numbers2(numbers):
    total = 0
    max_num = numbers[0]

    for num in numbers:
        total += num
        if num > max_num:
            max_num = num
    return total, max_num

num2 = [1,2,3,4]

total2 = sum_numbers2(num2)
print(total2)


