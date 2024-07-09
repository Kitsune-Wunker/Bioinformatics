startPos = 4822
endPos = 9721
result = 0

for x in range(startPos, endPos + 1):
    if x % 2 != 0:
        result += x

print(result)
