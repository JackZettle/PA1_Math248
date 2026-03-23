integer = 7


result = []

if integer == 0:
    result.append(0)

while integer > 0:
    if integer % 2 == 1:
        result.append(1)
    else:
        result.append(0)
    integer = integer // 2


result.reverse()
result = int("".join(map(str,result)))
print("The Binary Number is:", result)
