# sum of digits
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Sum of digits =", sum)

# reverse a number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number =", reverse)

# count digts in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits =", count)
 
  #check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# check prime number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# find factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)
# find factors of a number
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
# check palindrome number
num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# check arm strong number
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

  #find gcd(hcf) of two number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
while num2 != 0:
    num1, num2 = num2, num1 % num2
print("GCD =", num1)           