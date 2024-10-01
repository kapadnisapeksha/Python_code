from itertools import permutations
# Given digits
digits = [2, 3, 0]
# Generate all permutations of the digits
all_permutations = permutations(digits)
# Print the permutations
for perm in all_permutations:
    print(' '.join(map(str, perm)))
