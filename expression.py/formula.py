#implict type conversion
a=25
b=10.3
set=a+b
print(set)
print(type(set))

#Explicit type conversion
z=30
print(type(z))
y=str(z)
print(type(y))

# all 24 combinations
#int to float
x=20
y=float(x)
print(x)
print(type(y))

#int to string
x=40
y=str(x)
print(y)
print(type(y))

#int to complex
x=40
y=complex(x)
print(y)
print(type(y))

#int to bool
x=40
y=bool(x)
print(y)
print(type(y))

#float to int
x=40.2
y=int(x)
print(y)
print(type(y))

#float to string
x=40.2
y=str(x)
print(y)
print(type(y))

#float to bool
x=40.2
y=bool(x)
print(y)
print(type(y))

#float to complex
x=40.2
y=bool(x)
print(y)
print(type(y))

#string to int
x="40"
y=int(x)
print(y)
print(type(y))

#string to float
x="40"
y=float(x)
print(y)
print(type(y))

#string to bool
x="40"
y=bool(x)
print(y)
print(type(y))

#string to complex
x="40"
y=complex(x)
print(y)
print(type(y))

#complex to int
x=40+5j
y=int(x.real)
print(y)
print(type(y))

#complex to float
x=40+5j
y=float(x.real)
print(y)
print(type(y))

#complex to str
x=40+5j
y=str(x)
print(y)
print(type(y))

#complex to bool
x=40+5j
y=bool(x)
print(y)
print(type(y))