##############################################################################

# Program:Final_PA1_Part2.py

# Authors: Jack Zettlemoyer, Griffin Fee, Kai Behrens, Jacob Fitzmaurice

# Date: 03/24/26

# Purpose: This program takes in two user inputs, converts them into their binary form, and outputs the sum, difference, or product 
#   of these two numbers in binary and Base 10 forms. The program also outputs the binary values of each user input. All Arithmetic
#   is done using exclusively logic operations, attempting to mimic real computer arithmetic process
# 
# Inputs:
#   Int_1 (int) : The larger of two positive user entered base-10 integers
#   Int_2 (int) : The smaller of two positive user entered base-10 integers
#   Sign (string): The operation that needs to be performed: 'add', 'subtract', or 'multiply'
#
# Outputs:
#   The 32-bit, or 64-bit for multiplication, binary conversion of both user inputted integers,
#   the binary representation of the result, and the Base-10 equivalent.
###############################################################################

print("Please do not input numbers in scientific notation") #accounting for scientific notation error
Int_1 = int(input("Input larger number here: ")) #getting larger int value
Int_2= int(input("Input smaller number value here: ")) #getting smaller int value
Sign = input("Do you wish to 'add', 'subtract', or 'multiply' these two numbers:") # getting if they want to add, subtract or multiply
#----------------------------------------------------------------------------------------------------------------------------------------------------
#creating an error statement if the larger integer wasn't entered first, but still allowing the function to run as it would provide the right output
if Int_1 < Int_2:
    print("!!Error, the Larger Integer was not entered first!!")

#----------------------------------------------------------------------------------------------------------------------------------------------------
#The lines check if the integers inputted are larger than the largest int32 integer, and if it is it will stop the program as the code wouldn't work.
if Int_1 >= (2**31):
    raise ValueError("!!Error, the input is larger than an int32 integer!!")
if Int_2 >= (2**31):
    raise ValueError("!!Error, the input is larger than an int32 integer!!")
#----------------------------------------------------------------------------------------------------------------------------------------------------
#This function converts the integers inputted into their binary form
def binary_converter(integer_1, integer_2, bit_size): 
    '''
    Converts two positive Base-10 integers into their binary representations stored as lists of bits ins LSB order.

    Inputs:
        integer_1 (int): The first positive integer to convert
        integer_2 (int): The second positive integer to convert
        bit_size (int): The number of bits for binary form

    Outputs:
        result_1 (list of integers): Binary form of integer_1 as a list of 0's and 1's in LSB form padded to bit_size
        result_2 (list of integers): Binary form of integer_2 as a list of 0's and 1's in LSB form padded to bit_size
    '''
    result_1 = [] #setting an empty list for the results to be inputted
    if integer_1 == 0: #accounting for if the input is 0, making a list of one 0
        result_1.append(0)

    while integer_1 > 0: # creating a while loop with the standard base 10 to base conversions, dividing by 2 and adding the remainder to the list
        if integer_1 % 2 == 1: #using mod to get the remainder
            result_1.append(1)
        else:
            result_1.append(0)
        integer_1 = integer_1 // 2 #taking floor of the integer divided by 2
    

    result_2 = [] #setting an empty list for the results to be inputted
    if integer_2 == 0: #accounting for if the input is 0, making a list of one 0
        result_2.append(0)

    while integer_2 > 0: # creating a while loop with the standard base 10 to base conversions, dividing by 2 and adding the remainder to the list
        if integer_2 % 2 == 1: #using mod to get the remainder
            result_2.append(1)
        else:
            result_2.append(0)
        integer_2 = integer_2 // 2 #taking floor of the integer divided by 2

    #For both of these statements we are adding 0s to the end of the binary form until it is converted to the correct bit size form
    if len(result_1) < bit_size: #checking to see if the binary number is in bit size form yet
        result_1 = result_1 + [0] * (bit_size - len(result_1)) # Adding zeros to the end of the list, we figure out the amount we need by subtracting 32 from what the length of the list is
    if len(result_2) < bit_size: #checking to see if the binary number is in 32 bit binary form yet
        result_2 = result_2 + [0] * (bit_size - len(result_2)) # Adding zeros to the end of the list, we figure out the amount we need by subtracting 32 from what the length of the list is
    return result_1, result_2


#Defining the half adder function
def half_adder(bit_a, bit_b):
    '''
    Constructs a half adder circuit using logic operations (XOR and AND).
    The XOR gate used here is equivalent to (A or B) AND NOT(A AND B), and can
    be constructed from the three fundamental logic gates (OR, AND, NOT).
    Takes two single-bit inputs and produces a sum bit and a carry bit just like a half adder

    Inputs:
        bit_a (int): First single bit input (0 or 1)
        bit_b (int): Second single bit input (0 or 1)

    Outputs:
        sum_val (int): the sum bit, computed using bit_a XOR bit_b (A XOR B)
        carry_val (int): the carry bit, computed using bit_a AND bit_b (A AND B)
    '''
    # Returns (sum, carry) for two bits.
    # XOR returns 1 when exactly 1 input is 1
    sum_val = bit_a ^ bit_b # defining the sum value using the or operator
    # Carry is 1 only when both inputs are 1
    carry_val = bit_a & bit_b # defining the carry value using the and operator
    return (sum_val, carry_val)
# defining the full adder function

def full_adder(bit_a, bit_b, carry_in):
    '''
    Mimics a full adder circuit by chaining two half adders together.
    Takes two individual single bit inputs and a carry_in bit, and produces a sum bit and a carry out bit
    like in the given diagram.

    Inputs:
        bit_a (int): First single bit input (0 or 1)
        bit_b (int): Second single bit input (0 or 1)
        carry_in (int): Carry in bit from the previously computed addition (0 or 1)

    Outputs:
        sum2 (int): the final sum bit for its bit position
        carry_out (int) the carry out bit to be passed on to the next bit position
    '''
    # Returns (sum, carry_out) for three bits.
    sum1, carry1 = half_adder(bit_a, bit_b) # getting the sum and carry values from adding bit 1 and bit 2 by using the half adder
    sum2, carry2 = half_adder(sum1, carry_in) # getting the sum and carry values from adding the first sum with the carry in input using the half adder
    carry_out = carry1 | carry2 # using a bitwise or operator to get the carry out value
    return (sum2, carry_out)

def recursive_bit_adder(a_bits, b_bits, index, carry , bit_size):
    '''
    Recursively adds two binary numbers bit by bit using the previously saved full adder,
    starting from the LSB/ position 0 (index 0) up to the bit size (bit_size)

    Inputs:
        a_bits (list of integers): First binary number as a list of individual bits (LSB)
        b_bits (list of integers): Second binary number as a list of individual bits (LSB)
        index (int): Current bit position being run
        carry (int) Carry bit from the previous bit
        bit_size (int) Total number of bits to pad

    Outputs:
        string : a string of bits that represent the sum, with an extra carry bit on the end. The string is in LSB order

    '''

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
    '''
    Recursively converts a binary number back into its base 10 integer representation

    Inputs:
        result (list of strings): Binary number as a list or string of bits LSB
        index (int): Current bit position being run
        bit_size (int) Total number of bits to pad

    Outputs:
        integer : the Base-10 integer of the binary number
    '''
    if index == bit_size: #if the index is the same as the bit size, it will return zero
        return 0  
    raised_bit = int(result[index]) * 2 ** index  #taking each integer value of the list and multiplying it by 2 to the power of the index
    return int(raised_bit) +  base_10_converter(result, index + 1, bit_size) #taking the result of each value produced by the previous line and adding all the values together so we can output the base 10 value of this int

#----------------------------------------------------------------------------------------------------------------------------------------------------

if Sign == 'subtract': #setting if statement for subtraction

    bit1, bit2 = binary_converter(Int_1, Int_2, 32) # calling binary converter for the integers inputted

    #creating a function so that we can display the bit values in a string instead of a list of each characters in the string
    def bit_display(a):
        '''
        Converts a list of bits in LSB order into the correct displayable string in standard MSB form

        Inputs:
            a (list of integers): Binary number in individual list form, LSB

        Outputs:
            string: Binary number as a string in MSB form
        '''
        a = a[::-1] #reverses the list
        a = "".join(map(str,a)) #joins all the strings in the list into one string
        return a
    
    #calls the bit display function so we can display the bits in a string
    bit1_bin = bit_display(bit1)
    bit2_bin = bit_display(bit2)
   
    #creating a bit flipper, which takes the complement of the int32 integer
    def bit_flipper(bit2, index):
        '''
        Recursively computes the ones complement of a binary number by fliping each bit using XOR with 1
        
        Inputs:
            bits (list of integers): Binary number as a list
            index (int): Current bit position being run
        
        Outputs:
            list of integers: The ones complement of a binary number
        '''
        if index == 32:
            return []
        flipped_bit = bit2[index] ^ 1 # getting a flipped bit by using the or function to get the opposite of what was inputted
        return [flipped_bit] + bit_flipper(bit2, index + 1) # repeating this process for every single bit in the 32int integer

    bit2 = bit_flipper(bit2, 0)

    #Creating a function which takes the complement of bit 2 (ass this is the smaller bit which we use in subtraction) and adds 1 to that value
    def complement(bit2):
        '''
        Calculates the twos complement of a 32-bit binary number by taking the result of the bit flipper (ones complement)
        and adding 1 using the recursive bit adder

        Inputs:
            bit2 (list of integers): Binary number as a list LSB form

        Outputs:
            string: The twos complement as a string in LSB form with the carry bit included
        '''
        one = [1] + [0] * (31) # creating one in 32 bit binary form
        return str(recursive_bit_adder(bit2, one, 0, 0, 32)) # adding 1 to the complement of bit 2 so we can use it in the subtraction method

    sub_result = complement(bit2) #calling the value of the complement of bit 2 + 1

    #These next few lines of code make sure that we have the right form to input the complement + 1 into the recursive bit adder
    sub_result = sub_result[:-1] #taking away the last value of the string of the complement + 1
    sub_result = list(sub_result) #making the complement + 1 into a list of each individual bit
    sub_result = [int(i) for i in sub_result] # making each value string value in the list into an integer

    result = recursive_bit_adder(bit1, sub_result, 0, 0, 32) #adding bit 1 and the complement of bit 2 + 1

    def binary_sub_display(result):
        '''
        Formats the binary Substitution result string for display by removing the extra carry bit and reversing ro put into MSB form

        Inputs:
            result (string): Binary result string from the recursive bit adder LSB form

        Outputs:
            string: The 32-bit binary result in MSB form 
        '''

        # Call the Full 32 Bit Adder Result, Adding Error statement accounting for Overflow
        carry_bit = result[-1] # Last character in the bit is now the carry bit
        result_bits = result[:-1] # Removes the last bit of the result which would be the first bit once reversed (which you need to remove that bit in this subtraction method)
        result_bits = result_bits[::-1] # Reverse the result 
        return result_bits

    binary_add_display_result = binary_sub_display(result) #Make the result in displayable form
    print(f"The Difference of {Int_1} and {Int_2} in 32 Bit Binary is: {binary_add_display_result}") # print the results in 32 bit binary form

    base_10_result = base_10_converter(result, 0, 32) #converting the result into base 10
    if Int_1 < Int_2:
        base_10_result = base_10_result - (2 ** 32) #accounting to be able to take in negative numbers for the resuklt of the subtraction
    
    print(f"{binary_add_display_result} in Base 10 is Equal to {base_10_result}, which is equal to {Int_1} - {Int_2}") #printing the results in base 10 form
    print(f"{Int_1} in 32-Bit Binary is {bit1_bin}, {Int_2} in 32-Bit Binary is {bit2_bin}") #printing the converted integer values that were inputted at the start of the program

#----------------------------------------------------------------------------------------------------------------------------------------------------

elif Sign == 'add': #setting if statement for addition
    bit1, bit2 = binary_converter(Int_1, Int_2, 32) # calling the binary values of the integers inputted

    #creating a function so that we can display the bit values in a string instead of a list of each characters in the string
    def bit_display(a):
        '''
        Converts a list of bits in LSB order into the correct displayable string in standard MSB form

        Inputs:
            a (list of integers): Binary number in individual list form, LSB

        Outputs:
            string: Binary number as a string in MSB form
        '''
        a = a[::-1] #reverses the list
        a = "".join(map(str,a)) #joins all the strings in the list into one string
        return a
    
    #calls the bit display function so we can display the bits in a string
    bit1_bin = bit_display(bit1)
    bit2_bin = bit_display(bit2)

    # Call the result using user inputted integer values, position starting at 0 and increasing, and placeholder carry value of 0
    result = recursive_bit_adder(bit1, bit2, 0, 0, 32)

    # Create a function to properly display the result and check for overflow
    def binary_add_display(result):
        '''
        Formats the binary Substitution result string for display by removing the extra carry bit and reversing ro put into MSB form,
        while also checking for overflow

        Inputs:
            result (string): Binary result string from the recursive bit adder LSB form

        Outputs:
            string: The 32-bit binary result in MSB form 
        '''

    # Call the Full 32 Bit Adder Result, Adding Error statement accounting for Overflow
        carry_bit = result[-1] # Last character in the bit
        result_bits = result[:-1] #setting result equal to the result bits stopping at the last character in the bit
        result_bits = result_bits[::-1] # Reverse the result 

        # Check for Overflow 
        # Overflow occurs if carry_bit is '1', meaning the result requires a 33rd bit
        if carry_bit == '1' or result_bits[0] == '1': #accounting for the overflow errors by checking the values of the carry and result bits
            print("!!Overflow has Occurred!!")
        else:
            result_bits = result_bits
        return result_bits

    binary_add_display_result = binary_add_display(result) #Make the result in displayable form
    print(f"The Sum of {Int_1} and {Int_2} in 32 Bit Binary is: {binary_add_display_result}") # print the results in 32 bit binary form

    base_10_result = base_10_converter(result, 0, 32)#converting the result into base 10
    print(f"{binary_add_display_result} in Base 10 is Equal to {base_10_result}, which is equal to {Int_1} + {Int_2}") #printing the results in base 10 form
    print(f"{Int_1} in 32-Bit Binary is {bit1_bin}, {Int_2} in 32-Bit Binary is {bit2_bin}") #printing the converted integer values that were inputted at the start of the program


#----------------------------------------------------------------------------------------------------------------------------------------------------

elif Sign == 'multiply': 
    bit1, bit2 = binary_converter(Int_1, Int_2, 64) #calling bit 1 and bit 2 from the binary converter function using the integers inputted

    def bin_mult(bit1, bit2, index, total):
        '''
        Recursively multiples two binary numbers using the shifting and adding process, built using the recursive bit adder.
        For each bit in the multiplier, if that bit is 1, we create a shifted copy of the bit were multiplying by and
        then add it to the total

        Inputs:
            bit1 (list of integers): The bit were multiplying in binary LSB form and 64-Bits
            bit2(list of integers): The multiplier bit in LSB form and 64 bits

        Outputs:
            list of integers: The final product as a list of bits
        '''

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
        '''
        Converts a list of bits in LSB order into the correct displayable string in standard MSB form,

        Inputs:
            i(list of integers): Binary number in individual list form, LSB

        Outputs:
            string: Binary number as a string in MSB form
        '''
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
    print(f"{bin_mult_result} in Base 10 is Equal to {base_10_result}, which is equal to {Int_1} x {Int_2}") #Outputting the final result

#----------------------------------------------------------------------------------------------------------------------------------------------------

else:
    print("Please input 'add', 'subtract', or 'multiply' for the last input") # accounting for errors if they don't enter subtract, add or multiply

#----------------------------------------------------------------------------------------------------------------------------------------------------