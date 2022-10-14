def binary_array_to_decimal(binary_array):
    decimal = 0
    for i, bit in enumerate(binary_array):
        if bit == 1:
            decimal += 2 ** (len(binary_array) - 1 - i)
    
    return decimal

binary_numbers = []
bit_frequency = []
with open('input.txt') as f:
    binary_numbers = f.readlines()

bit_frequency = [0 for i in range(0, len(binary_numbers[0].strip()))]

for bin in binary_numbers:
    for i in range(0, len(bin) - 1):
        bit_frequency[i] = bit_frequency[i] + int(bin[i])

gamma_rate_binary = []

for on_bits_count in bit_frequency:
    off_bits = len(binary_numbers) - on_bits_count
    gamma_rate_binary.append(0 if off_bits > on_bits_count else 1)
    # print(f'Bit pos {i} ¦ 1: {on_bits}, 0: {off_bits}')


epsilon_rate_binary = [0 if x == 1 else 1 for x in gamma_rate_binary]
print(binary_array_to_decimal(gamma_rate_binary) * binary_array_to_decimal(epsilon_rate_binary))