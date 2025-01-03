#1.Write a Python function to find the Max of three numbers.

a = 546777
b = 569485
c = 958564

def maxnum(a,b,c):
    if a > b:
        print("a is max")
    elif b > c:
        print("b is max")
    elif c > a and c > b:
        print("c is max")

maxnum(a,b,c)

#2.Write a Python function to sum all the numbers in a list.

def sumall(num):
    return sum(num)

num = [938575,74854,939848]
Total = sumall(num)
print(Total)

#3.Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

number = [73464, 746347,83747]
multi = multiply(number)
print(multi)
