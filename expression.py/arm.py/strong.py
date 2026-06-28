# 1. Find Length of Number
num = int(input("Enter a number: "))
temp = num
length = 0
while temp > 0:
    length += 1
    temp //= 10

# 2. Separate Each Number
temp = num
sum = 0
while temp > 0:
    digit = temp % 10

# 3. Power = Length of Number
power = digit ** length

# 4. Sum
sum += power
temp //= 10

# 5. Check Condition
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")