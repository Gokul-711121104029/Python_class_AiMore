""" Design a login system using Python.

Requirements:

The correct password is "python123".
Track the number of login attempts.
Display the attempt number before each password prompt.
If the user enters the correct password, print "Access Granted!" and terminate the loop.
After three unsuccessful attempts, print "Too many failed attempts. Account locked." and terminate the program.

Sample Output:

Attempt 1: Enter password: wrong
Incorrect. Try again.

Attempt 2: Enter password: wrong2
Incorrect. Try again.

Attempt 3: Enter password: wrong3
Too many failed attempts. Account locked."""

p="python123"
for i in range(1,4):
    l=input(f"Attempt {i}: Enter the password:")
    if l==p:
        print("Access Granted!")
        break
    elif(i<4):
        print("Incorrect Try Again")
else:
    print("Too many failed attempts. Account locked.")

# using the while loop
p="python123"
i=1
a=3
while i<=a:
    l=input(f"Attempt {i}: Enter the password:")
    if l==p:
        print("Access Granted!")
        break
    elif (i<=3):
        print("Incorrect Try again")
    i+=1
else:
    print("Too many failed attempts. Account locked.")

