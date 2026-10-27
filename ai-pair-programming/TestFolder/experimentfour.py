def look_and_say(n):
    result = ["1"]
    for _ in range(n - 1):
        prev = result[-1]
        next_num = ""
        i = 0
        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                i += 1
                count += 1
            next_num += str(count) + prev[i]
            i += 1
        result.append(next_num)
    return result

numbers = look_and_say(10)
for num in numbers:
    print(num)
