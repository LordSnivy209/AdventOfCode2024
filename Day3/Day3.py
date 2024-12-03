import re

with open("input_day3", "r") as inputs:
    results = []
    content = inputs.read()
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", content)
    for match in matches:
        num1 = int(match[0])
        num2 = int(match[1])

        calc = num1 * num2
        results.append(calc)

result = sum(results)
print(result)

#part 2
with open("input_day3", "r") as inputs:
    content = inputs.read()

    do = True
    results = []
    matches = re.finditer(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", content)

    for match in matches:

        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif do:

            num1 = int(match.group(2))
            num2 = int(match.group(3))
            calc = num1 * num2
            results.append(calc)

result = sum(results)
print(result)