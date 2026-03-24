print("Please do not input numbers in scientific notation") #accounting for scientific notation error
Int_1 = int(input("Input larger number here: ")) #getting larger int value
Int_2= int(input("Input smaller number value here: ")) #getting smaller int value
Sign = input("Do you wish to add or subtract these two numbers:") # getting if they want to add or subtract
#--------------------------------------------------------------------------------------------------
if Int_1 > (2**31)-1: #Accounting for the error that the int inputted is larger than a int 32 integer
    print("Error, the input is larger than an int32 integer")
if Int_2 > (2**31)-1: #Accounting for the error that the int inputted is larger than a int 32 integer
    print("Error, the input is larger than an int32 integer")
#--------------------------------------------------------------------------------------------------------------
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
    result_1 = ("".join(map(str,result_1)))


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
    result_2 = ("".join(map(str,result_2)))
    return result_1, result_2
num1_bits, num2_bits = binary_converter(Int_1, Int_2)

if Sign == 'subtract': #setting if statement for subtraction
    print('hi')#placeholder


elif Sign == 'add': #setting if statement for addition
    def half_adder(bit_a, bit_b):
        #Returns (sum, carry) for two bits
        sum_val = bit_a ^ bit_b
        carry_val = bit_a & bit_b
        return (sum_val, carry_val)

    def full_adder(bit_a, bit_b, carry_in):
        #Returns (sum, carry_out) for three bits
        sum1, carry1 = half_adder(bit_a, bit_b)
        sum2, carry2 = half_adder(sum1, carry_in)
        carry_out = carry1 | carry2
        return (sum2, carry_out)


    def two_bit_adder_logic(a_bits, b_bits):
        
        #Adds two 2-bit numbers (strings like '10', '01')
        #Returns (carry, s1, s0)
        

        # Convert to list of ints
        a = list(map(int, str(a_bits)))###### FIGURE OUT HOW TO CONVERT TO A LIST OF INTS WITHOUT A FOR LOOP
        b = list(map(int, str(b_bits)))

        # Reverse so index 0 = LSB
        a = b.reverse()
        b = b.reverse()

        # LSB addition
        s0, c0 = half_adder(a[0], b[0])

        # MSB addition (with carry)
        s1, c1 = full_adder(a[1], b[1], c0)

        return (c1, s1, s0)

    carry_out, sum1, sum0 = two_bit_adder_logic(num1_bits, num2_bits)

    print(f"The sum of {num1_bits} and {num2_bits} in binary is: {carry_out}{sum1}{sum0}") 
else:
    print("Please input add or subtract for the last input") # accounting for errors if they don't enter subtract or add

