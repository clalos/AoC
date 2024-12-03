import re

pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
with open("input.txt", "r", encoding="utf8") as file:
    matches = re.findall(pattern, file.read())
    result = 0
    ignore = False
    for match in matches:
        if match[3]:
            # Don't
            ignore = True
            continue
        elif match[2]:
            # Do
            ignore = False
            continue
        if not ignore:
            result += int(match[0]) * int(match[1])
print(result)
