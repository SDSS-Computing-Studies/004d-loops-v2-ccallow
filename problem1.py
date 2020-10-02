#Ask the user to enter in the width and height of a box. 
# This should be an integer value less than 10 Draw a box filled with "*" symbols that matches the width and height. 
# You will need 2 nested loops to draw the contents of 1 row and the number of rows.

n=int(input("Enter the width/height:  "))

for i in range(1, n+1):
    if i <= n:
            print("*"*n)