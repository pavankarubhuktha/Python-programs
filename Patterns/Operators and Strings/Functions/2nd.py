def unique_list(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list


sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

print("Unique List:", unique_list(sample_list))
