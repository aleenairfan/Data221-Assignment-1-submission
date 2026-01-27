# Controlled Multiplication Loop

threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    product *= currentNumber
    currentNumber += 1

print("Final product:", product)
print("Integer that caused product to exceed threshold:", currentNumber - 1)
