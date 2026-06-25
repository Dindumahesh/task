# 1. Square Pattern
print("1. Square Pattern")
for i in range(4):
    for j in range(4):
        print ("*", end=" ")
    print()


# 2. Right Triangle
print("\n2. Right Triangle")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 3. Number Triangle
print("\n3. Number Triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 4. Repeated Number Triangle
print("\n4. Repeated Number Triangle")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# 5. Alphabet Triangle
print("\n5. Alphabet Triangle")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# 6. Inverted Star Triangle
print("\n6. Inverted Star Triangle")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()