10###############################################################################
# Program: Programming_Assignment_1_Part1.py
# Authors: Jack Zettlemoyer, Griffin Fee, Kai Behrens, Jacob Fitzmaurice
# Date: 03/24/26
# Purpose: This program adds two 2-bit binary numbers using exclusively
#   logical operations (AND, OR, XOR), mimicking how a physical digital
#   circuit performs addition through logic gates. The program uses a
#   half adder for the least significant bit and a full adder for the
#   most significant bit to produce a 3-bit binary sum and its base-10
#   equivalent. The user inputs two 2-digit binary strings, and the
#   program outputs the result in both binary and base-10 form.
#
# Inputs:
#   num1_bits (str) - First 2-bit binary number as a string (e.g., '10', '01', '11', '00')
#   num2_bits (str) - Second 2-bit binary number as a string (e.g., '10', '01', '11', '00')
#
# Outputs:
#   The 3-bit binary sum (carry_out, sum1, sum0) of the two inputs,
#   printed as a binary string, along with the corresponding base-10
#   addition statement.
###############################################################################

# ----------------------------------------------------------------------------------------------------------------------------------------------------


def half_adder(bit_a, bit_b):
    """
    Simulates a half adder circuit using logic gates (XOR, AND).
    The XOR gate used here is equivalent to (A OR B) AND NOT(A AND B),
    and can be constructed from the three fundamental gates (OR, AND, NOT).
    Takes two single-bit inputs and produces a sum bit and a carry bit.

    Inputs:
        bit_a (int): First single-bit input (0 or 1).
        bit_b (int): Second single-bit input (0 or 1).

    Outputs:
        sum_val   (int): The sum bit, computed as A XOR B.
        carry_val (int): The carry bit, computed as A AND B.
    """
    # S = A XOR B — the XOR gate is equivalent to (A OR B) AND NOT(A AND B),
    # meaning it can be constructed from OR, AND, and NOT gates.
    # XOR returns 1 when exactly one input is 1.
    sum_val = bit_a ^ bit_b
    # Cout = A AND B — carry is 1 only when both inputs are 1
    carry_val = bit_a & bit_b
    return (sum_val, carry_val)


def full_adder(bit_a, bit_b, carry_in):
    """
    Simulates a full adder circuit by chaining two half adders together.
    Takes two single-bit inputs and a carry-in bit, and produces a sum bit
    and a carry-out bit.

    Inputs:
        bit_a    (int): First single-bit input (0 or 1).
        bit_b    (int): Second single-bit input (0 or 1).
        carry_in (int): Carry-in bit from a previous addition (0 or 1).

    Outputs:
        sum2      (int): The final sum bit for this bit position.
        carry_out (int): The carry-out bit to be passed to the next position.
    """
    sum1, carry1 = half_adder(bit_a, bit_b)  # getting the sum and carry values from adding bit_a and bit_b using the half adder
    sum2, carry2 = half_adder(sum1, carry_in)  # getting the sum and carry values from adding the first sum with the carry_in using the half adder
    carry_out = carry1 | carry2  # using a bitwise OR operator to get the carry out value
    return (sum2, carry_out)


# ----------------------------------------------------------------------------------------------------------------------------------------------------


def two_bit_adder_logic(a_bits, b_bits):
    """
    Adds two 2-bit binary numbers using a half adder for the least significant
    bit position and a full adder for the most significant bit position, as
    specified in the assignment circuit diagram. No arithmetic operations are
    used — all computation is performed through logic gates (XOR, AND, OR).

    Inputs:
        a_bits (str): First 2-bit binary number as a string (e.g., '10', '11').
        b_bits (str): Second 2-bit binary number as a string (e.g., '01', '11').

    Outputs:
        carry_out (int): Carry-out bit (0 or 1).
        s1        (int): Most significant bit of the sum (0 or 1).
        s0        (int): Least significant bit of the sum (0 or 1).
    """
    # Convert each character in the binary string to a list of integers
    a = [int(bit) for bit in a_bits]
    b = [int(bit) for bit in b_bits]

    # Reverse so index 0 = LSB (least significant bit first)
    a.reverse()
    b.reverse()

    # LSB addition: half adder adds the two least significant bits
    s0, c0 = half_adder(a[0], b[0])

    # MSB addition: full adder adds the two most significant bits with the carry from the LSB
    s1, c1 = full_adder(a[1], b[1], c0)

    return (c1, s1, s0)


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Getting user inputs as 2-bit binary strings

num1_bits = input("Enter first 2-bit binary number (e.g. 00, 01, 10, 11): ")  # getting first 2-bit binary input
num2_bits = input("Enter second 2-bit binary number (e.g. 00, 01, 10, 11): ")  # getting second 2-bit binary input

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Input validation: ensuring inputs are valid 2-bit binary strings

if len(num1_bits) != 2 or len(num2_bits) != 2:
    raise ValueError("!!Error, both inputs must be exactly 2 digits!!")

for char in num1_bits:
    if char != '0' and char != '1':
        raise ValueError("!!Error, inputs must contain only 0s and 1s!!")

for char in num2_bits:
    if char != '0' and char != '1':
        raise ValueError("!!Error, inputs must contain only 0s and 1s!!")

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Running the two-bit adder on the user's inputs

carry_out, sum1, sum0 = two_bit_adder_logic(num1_bits, num2_bits)  # calling the two-bit adder with the user inputs

# Converting inputs to base 10 for display
a_dec = int(num1_bits[0]) * (2 ** 1) | int(num1_bits[1]) * (2 ** 0)  # base-10 value of input A
b_dec = int(num2_bits[0]) * (2 ** 1) | int(num2_bits[1]) * (2 ** 0)  # base-10 value of input B
sum_dec = carry_out * (2 ** 2) | sum1 * (2 ** 1) | sum0 * (2 ** 0)  # base-10 value of the sum

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Outputting the results to the user

print(f"The Sum of {num1_bits} and {num2_bits} in Binary is: {carry_out}{sum1}{sum0}")  # printing the binary result
print(f"{carry_out}{sum1}{sum0} in Base 10 is Equal to {sum_dec}, which is equal to {a_dec} + {b_dec}")  # printing the base 10 result
print(f"{num1_bits} in Base 10 is {a_dec}, {num2_bits} in Base 10 is {b_dec}")  # printing the converted input values

# ----------------------------------------------------------------------------------------------------------------------------------------------------