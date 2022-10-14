def reduce_numbers_by_frequency(by_most_common, numbers):
    if len(numbers) == 0:
        return None

    for i in range(0, len(numbers[0])):
        if len(numbers) == 1:
            return numbers[0]

        active_bits = 0
        for line in numbers:
            active_bits += 1 if line[i] == "1" else 0

        inactive_bits = len(numbers) - active_bits

        bit_criteria = None
        if by_most_common:
            bit_criteria = "1" if active_bits >= inactive_bits  else "0"
        else:
            bit_criteria = "1" if active_bits < inactive_bits else "0"
        
        numbers = list(filter(lambda x: (x[i] == bit_criteria), numbers))
    
    return numbers[0] if len(numbers) == 1 else None


all_numbers = None
with open('input.txt') as file:
    all_numbers = [line.strip() for line in file.readlines()]

oxygen_gen_rating = reduce_numbers_by_frequency(True, all_numbers[:])
co2_scrub_rating = reduce_numbers_by_frequency(False, all_numbers[:])

print(f'oxygen_gen_rating: {oxygen_gen_rating}')
print(f'co2_scrub_rating: {co2_scrub_rating}')

print(f'result: {int(oxygen_gen_rating, base=2) * int(co2_scrub_rating, base=2)}')