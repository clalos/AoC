group1 = []
group2 = []
with open("input.txt", "r", encoding="utf8") as file:
    for line in file:
        list = line.strip().split()
        group1.append(int(list[0]))
        group2.append(int(list[1]))

similarity_score = 0
for i in group1:
    occurrence = 0
    for j in group2:
        if i == j:
            occurrence += 1
    similarity_score += i * occurrence

print(similarity_score)
