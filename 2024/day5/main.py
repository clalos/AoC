from functools import cmp_to_key

rules = []


# Compare checks if the pair is in the rules list
def compare(a, b):
    if (a, b) in rules:
        return -1
    if (b, a) in rules:
        return 1
    return 0


correct_update_sum = 0
incorrect_update_sum = 0
is_update = False
with open("input.txt", "r", encoding="utf8") as file:
    for line in file:
        # Start of update section
        if line.strip() == "":
            is_update = True
            continue
        # Update section
        if is_update:
            update = list(map(int, line.strip().split(",")))
            update_sorted = sorted(update, key=cmp_to_key(compare))
            if update == update_sorted:
                correct_update_sum += update[len(update) // 2]
            else:
                incorrect_update_sum += update_sorted[len(update_sorted) // 2]
            continue
        # Rules section
        first, second = map(int, line.strip().split("|"))
        rules.append((first, second))

print("Correct update sum: %s" % correct_update_sum)
print("Incorrect update sum: %s" % incorrect_update_sum)
