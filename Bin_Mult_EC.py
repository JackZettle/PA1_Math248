##################################################
#Part 2 program - Griffin
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

    if len(result_1) < 64:
        result_1 = result_1 + [0] * (64 - len(result_1)) 
    if len(result_2) < 64:
        result_2 = result_2 + [0] * (64 - len(result_2)) 

    return result_1, result_2

#-----------------------------------------------------------------------------
bit1, bit2 = binary_converter(integer1, integer2)
#-----------------------------------------------------------------------------
# Bit Adder
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

    # If the Index (position) = 64 then we return the carry bit
    # We use 64 because if two 32 bit numbers are multiplies our max result is 64 bits
    if index == 64:
        return carry
    
    # Compute a singular bits position using the carry from the previous position, and return a sum bit and a carry
    sum_bit, new_carry = full_adder(a_bits[index], b_bits[index], carry)

    # Return the bit that was just calculated then call the function again, 
    # running it on the next position returning a new sum bit and another new carry until index == 64
    return str(sum_bit) + str(recursive_bit_adder(a_bits, b_bits, index + 1, new_carry))



def bin_mult(bit1, bit2, index, total):

    # When index(position) is at 64 all of the multiplier bits have been run, so then we return the final total
    if index == 64:
        return total
    
    # Check if the current bit in the bit2 list (Multiplier) is = 1
    # We only use 1 because if the bit was = 0 there is nothing to store or add
    if bit2[index] == 1:
        # Create a copy of bit1 where we add the position number of zeros to the front of bit1
        bit1_shift = [0] * index + bit1

        # Pad the bit1 copy to ensure it is 64 bits long
        # Saying if the bit1 copy is less than 64 add as many needed 0's to the copy to make it 64-bits
        if len(bit1_shift) < 64:
            bit1_shift = bit1_shift + [0] * (64 - len(bit1_shift))
        
        # Run the 64-bit bit1 copy to the current total using the recursive bit adder
        total = recursive_bit_adder(total, bit1_shift, 0, 0)
        total = total[:-1] # Remove the last bit (65th bit) from the total
        total = list(total) # Convert the total which is currently a string into a list
        total = [int(i) for i in total] # Convert that list into a list of integers
    # Run the entire function again but on the next bit position regardless of value because we check for that in said function
    return bin_mult(bit1, bit2, index + 1, total)

# Save the output using previously stated inputs, index position starting at 0 and a total list of 64 zeros since we need 64 bits
bin_mult_output = bin_mult(bit1, bit2, 0, [0] * 64)

# Create a function that will present the multiplication output in the correct form
def bin_mult_display(i):
    # Reverse the list into Most Significant Bit first form or the standard binary format
    i = i[::-1]
    # Join the list of individual entries into a single string
    i = "".join(map(str,i))
    return i

# Run the previous output through the display correction function and save it
bin_mult_result = bin_mult_display(bin_mult_output)

# Print the output of the user inputted integers
print(f"The Binary Result in 64-Bit Form of {integer1} x {integer2} = {bin_mult_result}")