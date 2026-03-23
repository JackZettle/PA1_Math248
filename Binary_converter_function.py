##################################################
#Part 2 program
#Take input of base 10 numbers, convert them to binary, be able to add the numbers
##################################################

def binary_converter(integer_1,integer_2):
    result_1 = []
    if integer_1 == 0:
        result_1.append(0)

    while integer_1 > 0:
        if integer_1 % 2 == 1:
            result_1.append(1)
        else:
            result_1.append(0)
        integer_1 = integer_1 // 2
    result_1.reverse()
    result_1 = int("".join(map(str,result_1)))


    result_2 = []
    if integer_2 == 0:
        result_2.append(0)

    while integer_2 > 0:
        if integer_2 % 2 == 1:
            result_2.append(1)
        else:
            result_2.append(0)
        integer_2 = integer_2 // 2
    result_2.reverse()
    result_2 = int("".join(map(str,result_2)))
    return result_1, result_2

#-----------------------------------------------------------------------------

print(binary_converter(18,50))