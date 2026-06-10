"""1. You are given a list containing positive, negative, and zero values:

numbers = [15, -3, 25, 0, -10, 40]

Using a for loop and the continue statement:

Ignore all non-positive values.
Calculate the sum of positive numbers only.
Print each positive number that is added to the sum.
Print the final sum."""

numbers=[15,-3,25,0,-10,40]
sum=0
r=[]
for i in numbers:
    if i<=0:
        continue
    print(i)
    sum +=i
    r.append(i)
print(f"The list of all positive number is {r}")
print(f"Sum of all positive number is {sum}")



