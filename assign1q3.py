# Safe Function Application

def power(base, exponent):
    return base ** exponent


pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []

for base, exponent in pairs:
    if exponent < 0:
        continue
    results.append(power(base, exponent))

print(results)
