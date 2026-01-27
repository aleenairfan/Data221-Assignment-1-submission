# Sorted Search with Conditions

from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

matchingIndices = [i for i, value in enumerate(values) if value >= x]

print("Sorted values:", values)
print("x:", x)

if matchingIndices:
    print("First matching index:", matchingIndices[0])
else:
    print("No values greater than or equal to x")
