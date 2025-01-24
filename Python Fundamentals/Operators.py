a,b,c=10,5,0
# Arithmetic operation
print("Arithmetic operation")
print(f"The sum of a and b is {a+b+c}")
print(f"The difference is {a-b-c}")
print(f"The product is {a*b*c}")
print(f"The division is {a/b}")
print(f"The floor value is {a//b}")
print(f"The remainder is {a%b}")
print(f"The exponent is {a**b}")
print("\n")

# comparision operator
print("Comparision operator")
print(f"a==b is {a==b}")
print(f"a!=b is {a!=b}")
print(f"a>b is {a>b}")
print(f"a<b is {a<b}")
print(f"a>=b is {a>=b}")
print(f"a<=b is {a<=b}")
print("\n")

#logical operator
print("logical operator")
print(f"a>b and b>c is {a>b and b>c}")
print(f"a>b or b>c is {a>b or b>c}")
print(f"not a>b is {not a>b}")
print("\n")
# Assignment operator

# a,b,c=10,5,0
a=b+c
print(f"a={a}")
a+=b
print(f"a={a}")
a-=b
print(f"a={a}")
a*=b
print(f"a={a}")
a//=b
print(f"a={a}")
a**=b
print(f"a={a}")

# Bitwise operator
x,y=4,3
print(f"x & y={x & y}")
print(f"X | Y={x|y}")
print(f"x ^ y ={x^y}")
print(f"not x ={~x}")
print(f"left shift ={x<<1}")
print(f"right shift ={x>>1}")

# membership function
my_list = [1,2,3,4,5]
print(my_list)
print(f"3 in my list :{3 in my_list}")
print(f"10 in my list ={10 in my_list}")
print(f"10 not in my list ={10 not in my_list}")