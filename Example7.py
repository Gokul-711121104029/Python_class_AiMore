"""3. You are given a list of student marks:

marks = [85, 90, 78, 92, 88]

Using a for loop:

Calculate the sum of all marks.
Determine the average mark.
Print the total number of students and the average mark.

Do not use Python's built-in sum() function."""

marks=[85,90,78,92,88]
sum=0
count=0
for i in marks:
    count +=1
    sum=sum+i
avg=sum/count
print(f"The Total number of students is {count}")
print(f"The average mark is {avg}")
print(f"The sum of all marks is :{sum}")
