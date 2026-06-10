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

login ="python123"
attempt=3
for i in range(3,0,-1):
    l=input("Enter the password:")
    if l==login:
        print("Access Granted!")
        break
    elif(i>1):
        attempt-=1
        print(f"Try again.{attempt} attempts left")
else:
    print("Too many failed attempts. Account locked.")

            



        
