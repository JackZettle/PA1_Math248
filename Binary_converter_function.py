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
    # result_1 = int("".join(map(str,result_1)))


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
    # result_2 = int("".join(map(str,result_2)))
    return result_1, result_2

#-----------------------------------------------------------------------------

print(binary_converter(18,50))

#-------------------------
#Two's compliment --> Way to subtract a binary number 
# take 

bin1, bin2 = binary_converter(18,50) # assigns bin1 and bin2 to their respective 

def subtract_two_integers(bin1, bin2): 
    
    #Compute twos compliment of smaller number 
    def Twos_complement_of_list(bin1): 
        # Ones Compliment
        ones = [1 - bit for bit in bin1]
        # add 1
        carry = 1
        for i in range(len(ones)-1, -1, -1):
            total = ones[i] + carry
            ones[i] = total % 2
            carry = total // 2
        if carry:
            ones.insert(0, 1)
        twos = ones
        return twos
    
    # Add two binary lists using half/full adder 
    def add_binary(A,B):
        def half_adder(A, B):
            sum_bit = A ^ B
            carry = A & B
            return sum_bit, carry
        def full_adder(A, B, Cin):
            s1, c1 = half_adder(A, B)
            s2, c2 = half_adder(s1, Cin)
            cout = c1 | c2
            return s2, cout

        print(full_adder(0,0,0))
        print(full_adder(0,0,1))
        print(full_adder(0,1,0))
        print(full_adder(0,1,1))
        print(full_adder(1,0,0))
        print(full_adder(1,0,1))
        print(full_adder(1,1,0))
        print(full_adder(1,1,1))

        def half_adder(bit_a, bit_b):
            """Returns (sum, carry) for two bits."""
            sum_val = bit_a ^ bit_b
            carry_val = bit_a & bit_b
            return (sum_val, carry_val)
        
        def full_adder(bit_a, bit_b, carry_in):
            """Returns (sum, carry_out) for three bits (including carry_in)."""
            sum1, carry1 = half_adder(bit_a, bit_b)
            sum2, carry2 = half_adder(sum1, carry_in)
            carry_out = carry1 | carry2
            return (sum2, carry_out)
        
        
        def two_bit_adder_logic(a_bits, b_bits):
            """
            Adds two 2-bit numbers represented as tuples/lists of integers (LSB first).
            e.g., '11' would be [1, 1]
            """
            # Ensure inputs are integers
            a0, a1 = int(a_bits[1]), int(a_bits[0]) # Assuming string input: index [1] is LSB
            b0, b1 = int(b_bits[1]), int(b_bits[0])
            
            # Add the LSB (least significant bit) using a half adder
            s0, c0 = half_adder(a0, b0)
            
            # Add the MSB (most significant bit) using a full adder with carry from LSB
            s1, c1 = full_adder(a1, b1, c0)
            
            # Result is carry, s1, s0
            return (c1, s1, s0)

        # Example usage:
        num1_bits = '11' # 3 in decimal
        num2_bits = '01' # 1 in decimal
        carry_out, sum1, sum0 = two_bit_adder_logic(num1_bits, num2_bits)

        print(f"The sum of {num1_bits} and {num2_bits} in binary is: {carry_out}{sum1}{sum0}") 
        # Output: The sum of 11 and 01 in binary is: 100
    
    # Subtract by adding 2's complement to the larger number
    bin2_twos = Twos_complement_of_list(bin2)
    result = add_binary(bin1, bin2_twos)
    return result

final_result = subtract_two_integers(bin1, bin2) ### where bin2 is larger
print("Binary subtraction result (bin1 - bin2):", final_result)