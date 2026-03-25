
print("Please do not input numbers in scientific notation") #accounting for scientific notation error
Int_1 = int(input("Input larger number here: ")) #getting larger int value
Int_2= int(input("Input smaller number value here: ")) #getting smaller int value
Sign = input("Do you wish to 'add', 'subtract', or 'multiply' these two numbers:") # getting if they want to add, subtract or multiply
#----------------------------------------------------------------------------------------------------------------------------------------------------

if Int_1 < Int_2:
    raise ValueError("!!Error, the Larger Int was not entered first!!")

#----------------------------------------------------------------------------------------------------------------------------------------------------

if Int_1 > (2**31)-1: #Accounting for the error that the int inputted is larger than a int 32 integer
    raise ValueError("!!Error, the input is larger than an int32 integer!!")
if Int_2 > (2**31)-1: #Accounting for the error that the int inputted is larger than a int 32 integer
    raise ValueError("!!Error, the input is larger than an int32 integer!!")
#----------------------------------------------------------------------------------------------------------------------------------------------------

def binary_converter(integer_1, integer_2, bit_size):
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

    if len(result_1) < bit_size:
        result_1 = result_1 + [0] * (bit_size - len(result_1)) 
    if len(result_2) < bit_size:
        result_2 = result_2 + [0] * (bit_size - len(result_2)) 
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

def recursive_bit_adder(a_bits, b_bits, index, carry , bit_size):

    # If the Index (position) = 32 then we return the carry bit
    if index == bit_size:
        return carry

    # Compute a singular bits position using the carry from the previous position, and return a sum bit and a carry
    sum_bit, new_carry = full_adder(a_bits[index], b_bits[index], carry)

    # Return the bit that was just calculated then call the function again, 
    # running it on the next position returning a new sum bit and another new carry until index == 32
    return str(sum_bit) + str(recursive_bit_adder(a_bits, b_bits, index + 1, new_carry, bit_size))

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Create a function the takes the result and converts it back into base 10
def base_10_converter(result, index, bit_size):  
    if index == bit_size:   
        return 0  
    raised_bit = int(result[index]) * 2 ** index  
    return int(raised_bit) +  base_10_converter(result, index + 1, bit_size)

#----------------------------------------------------------------------------------------------------------------------------------------------------

if Sign == 'subtract': #setting if statement for subtraction

    bit1, bit2 = binary_converter(Int_1, Int_2, 32)

    def bit_flipper(bit2, index):
        if index == 32:
            return []
        flipped_bit = bit2[index] ^ 1
        return [flipped_bit] + bit_flipper(bit2, index + 1)

    bit2 = bit_flipper(bit2, 0)

    def complement(bit2):
        one = [1] + [0] * (31)
        return str(recursive_bit_adder(bit2, one, 0, 0, 32))

    sub_result = complement(bit2)

    sub_result = sub_result[:-1]
    sub_result = list(sub_result)
    sub_result = [int(i) for i in sub_result]

    result = recursive_bit_adder(bit1, sub_result, 0, 0, 32)

    def binary_sub_display(result):

        # Call the Full 32 Bit Adder Result, Adding Error statement accounting for Overflow
        carry_bit = result[-1] # Last character in the bit
        result_bits = result[:-1] # 
        result_bits = result_bits[::-1] # Reverse the result 

        # Check for Overflow 
        # Overflow occurs if carry_bit is '1', meaning the result requires a 33rd bit
        return result_bits

    binary_add_display_result = binary_sub_display(result)
    print(f"The Difference of {Int_1} and {Int_2} in 32 Bit Binary is: {binary_add_display_result}")

    base_10_result = base_10_converter(result, 0, 32)
    if Int_1 < Int_2:
        print("\n!!Error: Larger Integer Was Not Entered First!!\n")
    base_10_result = base_10_result - (2 ** 32)
    
    print(f"{binary_add_display_result} in Base 10 is Equal to {base_10_result}, which is equal to {Int_1} - {Int_2}")

#----------------------------------------------------------------------------------------------------------------------------------------------------

elif Sign == 'add': #setting if statement for addition
    bit1, bit2 = binary_converter(Int_1, Int_2, 32)

    #------------------------------------------------------------------------------------------------------------------------------------------------
    if len(bit1) < 32:
        bit1 = bit1 + [0] * (32 - len(bit1)) 
    if len(bit2) < 32:
        bit2 = bit2 + [0] * (32 - len(bit2))     
    #------------------------------------------------------------------------------------------------------------------------------------------------
    

    # Call the result using user inputted integer values, position starting at 0 and increasing, and placeholder carry value of 0
    result = recursive_bit_adder(bit1, bit2, 0, 0, 32)

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
    print(f"The Sum of {Int_1} and {Int_2} in 32 Bit Binary is: {binary_add_display_result}")

    base_10_result = base_10_converter(result, 0, 32)
    print(f"{binary_add_display_result} in Base 10 is Equal to {base_10_result}, which is equal to {Int_1} + {Int_2}")

#----------------------------------------------------------------------------------------------------------------------------------------------------

elif Sign == 'multiply':
    bit1, bit2 = binary_converter(Int_1, Int_2, 64)

    def bin_mult(bit1, bit2, index, total):

        # When index(position) is at 64 all of the multiplier bits have been run, so then we return the final total
        if index == 64:
            return total
        
        # Check if the current bit in the bit2 list (Multiplier) is = 1
        # We only use 1 because if the bit was = 0 there is nothing to store or add
        if bit2[index] == 1:
            # Create a copy of bit1 where we add the position number of zeros to the front of bit1
            bit1_shift = [0] * index + bit1

            # Pad the bit1 copy to ensure it is 64-bits long
            # Saying if the bit1 copy is less than 64 add as many needed 0's to the copy to make it 64-bits
            if len(bit1_shift) < 64:
                bit1_shift = bit1_shift + [0] * (64 - len(bit1_shift))

            # limit the copy of bit1 to 64-bits in case extra zeros were added on due to adding based on bit position
            bit1_shift = bit1_shift[:64] 
            
            # Run the 64-bit bit1 copy to the current total using the recursive bit adder
            total = recursive_bit_adder(total, bit1_shift, 0, 0, 64)
            total = total[:-1] # Remove the last bit (65th bit) from the total
            total = list(total) # Convert the total which is currently a string into a list
            total = [int(i) for i in total] # Convert that list into a list of integers

        # Run the entire function again but on the next bit position regardless of value because we check for that in said function
        return bin_mult(bit1, bit2, index + 1, total)

    # Save the output using previously stated inputs, index position starting at 0 and a total list of 64 zeros since we need 64-bits
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
    print(f"The Binary Result in 64-Bit Form of {Int_1} x {Int_2} = {bin_mult_result}")

    base_10_result = base_10_converter(bin_mult_output, 0, 64) # Call the Base 10 converter using the
    print(f"{bin_mult_result} in Base 10 is Equal to {base_10_result}, which is equal to {Int_1} x {Int_2}")

#----------------------------------------------------------------------------------------------------------------------------------------------------

else:
    print("Please input 'add', 'subtract', or 'multiply' for the last input") # accounting for errors if they don't enter subtract or add

#----------------------------------------------------------------------------------------------------------------------------------------------------
