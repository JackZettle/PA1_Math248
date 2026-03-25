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


    result_2 = []
    if integer_2 == 0:
        result_2.append(0)

    while integer_2 > 0:
        if integer_2 % 2 == 1:
            result_2.append(1)
        else:
            result_2.append(0)
        integer_2 = integer_2 // 2

    #if len(result_1) < 32:
       # result_1 = result_1 + [0] * (32 - len(result_1)) 
    #if len(result_2) < 32:
       # result_2 = result_2 + [0] * (32 - len(result_2)) 
#---- Explain to Griffin why you moved this down ---------
    return result_1, result_2

def half_adder(bit_a, bit_b):
        #Returns (sum, carry) for two bits.
        sum_val = bit_a ^ bit_b
        carry_val = bit_a & bit_b
        return (sum_val, carry_val)

def full_adder(bit_a, bit_b, carry_in):
#Returns (sum, carry_out) for three bits.
    sum1, carry1 = half_adder(bit_a, bit_b)
    sum2, carry2 = half_adder(sum1, carry_in)
    carry_out = carry1 | carry2
    return (sum2, carry_out)

def recursive_bit_adder(a_bits, b_bits, index, carry):

    # If the Index (position) = 32 then we return the carry bit
    if index == 32:
        return carry

    # Compute a singular bits position using the carry from the previous position, and return a sum bit and a carry
    sum_bit, new_carry = full_adder(a_bits[index], b_bits[index], carry)

    # Return the bit that was just calculated then call the function again, 
    # running it on the next position returning a new sum bit and another new carry until index == 32
    return str(sum_bit) + str(recursive_bit_adder(a_bits, b_bits, index + 1, new_carry))
#----------------------------------------------------------------------------
bit1, bit2 = binary_converter(Int_1, Int_2)
#----------------------------------------------------------------------------
if Sign == 'subtract': #setting if statement for subtraction
    bit1_reversed = bit1[::-1]
    bit2_reversed = bit2[::-1]
    if len(bit1) > len(bit2_reversed):
        bit2_reversed = [0] + bit2
    bit2_reveresed_composite = list(map(lambda b: 1 - b, bit2_reversed)) #-----------------------------------need to add 1 to this, but how?
    #then you have to reverse them again for the adder
    bit2_composite = bit2_reveresed_composite[::-1]
    
#---------------- Take in 32 bit adder    
    if len(bit1) < 32:
        bit1 = bit1 + [0] * (32 - len(bit1)) 
    if len(bit2_composite) < 32:
        bit2_composite = bit2_composite + [0] * (32 - len(bit2_composite))    
    #-----------------------------------------------------------------------------
    # Call the result using user inputted integer values, position starting at 0 and increasing, and placeholder carry value of 0
    result = recursive_bit_adder(bit1, bit2_composite, 0, 0)


    # Call the Full 32 Bit Adder Result, Adding Error statement accounting for Overflow
    carry_bit = result[-1] # Last character in the bit
    result_bits = result[:-1] # 
    result_bits = result_bits[::-1] # Reverse the result
    print(result_bits) #######----------- THIS IS WHAT WE NEED TO FIX, I NEED TO REMOVE THE FIRST ONE FROM WHATEVER NUMBER IS THE OUTPUT#######
    result_bits = (str(result_bits))[1:]

    # Check for Overflow 
    # Overflow occurs if carry_bit is '1', meaning the result requires a 33rd bit
    # 
    if carry_bit == '1' or result_bits[0] == '1':
        print("Overflow has Occurred.")
        print(f"\nThe Binary Subtraction Result is {result_bits}")
    else:
        result_bits = result_bits.lstrip("0")
        print(f"The Sum of {Int_1} and {Int_2} in Binary is: {result_bits}")


elif Sign == 'add': #setting if statement for addition    
#-----------------------------------------------
    if len(bit1) < 32:
        bit1 = bit1 + [0] * (32 - len(bit1)) 
    if len(bit2) < 32:
        bit2 = bit2 + [0] * (32 - len(bit2))     
    #-----------------------------------------------------------------------------
    

    # Call the result using user inputted integer values, position starting at 0 and increasing, and placeholder carry value of 0
    result = recursive_bit_adder(bit1, bit2, 0, 0)

    # Call the Full 32 Bit Adder Result, Adding Error statement accounting for Overflow
    carry_bit = result[-1] # Last character in the bit
    result_bits = result[:-1] # 
    result_bits = result_bits[::-1] # Reverse the result 

    # Check for Overflow 
    # Overflow occurs if carry_bit is '1', meaning the result requires a 33rd bit
    # 
    if carry_bit == '1' or result_bits[0] == '1':
        print("Overflow has Occurred.")
        print(f"\nThe Binary Additive Result is {result_bits}")
    else:
        result_bits = result_bits.lstrip("0")
        print(f"The Sum of {Int_1} and {Int_2} in Binary is: {result_bits}")
else:
    print("Please input add or subtract for the last input") # accounting for errors if they don't enter subtract or add