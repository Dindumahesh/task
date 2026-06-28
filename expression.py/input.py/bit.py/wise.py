# Bitwise Operators Program
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# AND
print("AND (&) =", a & b)

# OR
print("OR (|) =", a | b)

# XOR
print("XOR (^) =", a ^ b)

# XOR for same values
print("XOR of same values =", a ^ a)

# Check if 1 is Even or Odd
if (1 & 1) == 1:
    print("1 is Odd")
else:
    print("1 is Even")

# NOT
print("NOT (~a) =", ~a)

# Left Shift
print("Left Shift (a << 1) =", a << 1)

# Right Shift
print("Right Shift (a >> 1) =", a >> 1)