with open("input_day1", "r") as inputs:
    location_id_left = []
    location_id_right = []
    location_difference = []
    calc = 0
    outcome = 0
    i = 0

    for line in inputs:
        left, right = map(int, line.split())
        location_id_left.append(left)
        location_id_right.append(right)

location_id_left.sort()
location_id_right.sort()
for line in location_id_left:
    if location_id_right[i] < location_id_left[i]:
        calc = location_id_left[i] - location_id_right[i]
        location_difference.append(calc)
        i +=1
    elif location_id_right[i] > location_id_left[i]:
        calc = location_id_right[i] - location_id_left[i]
        location_difference.append(calc)
        i += 1
    else:
        calc = 0
        i += 1

outcome = sum(location_difference)
print(outcome)

#part 2
i = 0
outcome = 0
similarities = []
calculated_list = []

for number in location_id_left:
    similarities.append(location_id_right.count(location_id_left[i]))
    calculated_list.append(similarities[i] * location_id_left[i])
    i +=1
outcome = sum(calculated_list)
print(outcome)