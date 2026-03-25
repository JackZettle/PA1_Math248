##################################################
#Part 2 program
#Take input of base 10 numbers, convert them to binary, be able to add the numbers
##################################################

integer1 = int(input("Enter the Larger Integer:"))
integer2 = int(input("Enter the Smaller Integer:"))

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

    if len(result_1) < 32:
        result_1 = result_1 + [0] * (32 - len(result_1)) 
    if len(result_2) < 32:
        result_2 = result_2 + [0] * (32 - len(result_2)) 

    return result_1, result_2

#-----------------------------------------------------------------------------
bit1, bit2 = binary_converter(integer1, integer2)
#-----------------------------------------------------------------------------
# 32 Bit Adder

def half_adder(bit_a, bit_b):
    """Returns (sum, carry) for two bits."""
    sum_val = bit_a ^ bit_b
    carry_val = bit_a & bit_b
    return (sum_val, carry_val)

def full_adder(bit_a, bit_b, carry_in):
    """Returns (sum, carry_out) for three bits."""
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

# Call the result using user inputted integer values, position starting at 0 and increasing, and placeholder carry value of 0
result = recursive_bit_adder(bit1, bit2, 0, 0)

# Create a function to properly display the result and check for overflow
def binary_add_display(result):

    # Call the Full 32 Bit Adder Result, Adding Error statement accounting for Overflow
    carry_bit = result[-1] # Last character in the bit
    result_bits = result[:-1] # 
    result_bits = result_bits[::-1] # Reverse the result 

    # Check for Overflow 
    # Overflow occurs if carry_bit is '1', meaning the result requires a 33rd bit
    # 
    if carry_bit == '1' or result_bits[0] == '1':
        print("!!Overflow has Occurred!!")
    else:
        result_bits = result_bits.lstrip("0")
    return result_bits

binary_add_display_result = binary_add_display(result)
print(f"The Sum of {integer1} and {integer2} in Binary is: {binary_add_display_result}")

# Create a function the takes the result and converts it back into base 10
def base_10_converter(result, index):  
    if index == 32:   
        return 0  
    raised_bit = int(result[index]) * 2 ** index  
    return int(raised_bit) +  base_10_converter(result, index + 1)

base_10_result = base_10_converter(result, 0)
print(f"{binary_add_display_result} in Base 10 is Equal to {base_10_result}, which is equal to {integer1} + {integer2}")

