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


def two_bit_adder_logic(a_bits, b_bits):
    """
    Adds two 2-bit numbers (strings like '10', '01')
    Returns (carry, s1, s0)
    """

    # Convert to list of ints
    a = [int(bit) for bit in a_bits]
    b = [int(bit) for bit in b_bits]

    # Reverse so index 0 = LSB
    a.reverse()
    b.reverse()

    # LSB addition
    s0, c0 = half_adder(a[0], b[0])

    # MSB addition (with carry)
    s1, c1 = full_adder(a[1], b[1], c0)

    return (c1, s1, s0)

# Example usage:
num1_bits = '10' # 3 in decimal
num2_bits = '01' # 1 in decimal
carry_out, sum1, sum0 = two_bit_adder_logic(num1_bits, num2_bits)

print(f"The sum of {num1_bits} and {num2_bits} in binary is: {carry_out}{sum1}{sum0}") 
# Output: The sum of 11 and 01 in binary is: 100