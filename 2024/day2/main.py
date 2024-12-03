def is_safe(report):
    increase = True
    for i in range(len(report)):
        if i == 0:
            continue
        cur, prev = report[i], report[i - 1]
        if cur == prev:
            # Not increasing nor decreasing
            return False
        if i == 1:
            # Establish direction
            increase = cur > prev
        elif (cur > prev) != increase:
            # Change in direction
            return False
        diff = abs(cur - prev)
        if diff < 1 or diff > 3:
            # Wrong difference
            return False
    return True


safe_no = 0
with open("input.txt", "r", encoding="utf8") as file:
    for line in file:
        report = line.strip().split()
        report = list(map(int, report))
        if is_safe(report):
            safe_no += 1
            continue
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            if is_safe(report_copy):
                safe_no += 1
                break

print("Safe reports: %s" % safe_no)
