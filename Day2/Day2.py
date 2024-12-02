#defs
def is_safe(list_of_numbers):
    increasing = all(
        list_of_numbers[i] < list_of_numbers[i + 1] and 1 <= list_of_numbers[i + 1] - list_of_numbers[i] <= 3 for i in range(len(list_of_numbers) - 1))

    decreasing = all(
        list_of_numbers[i] > list_of_numbers[i + 1] and 1 <= list_of_numbers[i] - list_of_numbers[i + 1] <= 3 for i in range(len(list_of_numbers) - 1))

    return increasing or decreasing

#part 2
def is_safe_buffer(list_of_numbers):

    if is_safe(list_of_numbers):
        return True
    else:
        for i in range(len(list_of_numbers)):
            modified_list_of_numbers = list_of_numbers[:i] + list_of_numbers[i + 1:]
            if is_safe(modified_list_of_numbers):
                return True
        return False

    return (is_increasing or is_decreasing) and buffer <= 1


#part 1
with open("input_day2", "r") as inputs:
    lists = []
    for line in inputs:
        numbers = list(map(int, line.split()))
        lists.append(numbers)


    safe_count = sum(is_safe(list_of_numbers) for list_of_numbers in lists)
    print(safe_count)

#part 2
with open("input_day2", "r") as inputs:
    lists = []
    for line in inputs:
        numbers = list(map(int, line.split()))
        lists.append(numbers)


    safe_count = sum(is_safe_buffer(list_of_numbers) for list_of_numbers in lists)
    print(safe_count)
