##### Task 1
#Ask the user to enter an integer.
#Print the multiplication tables up to 12 for that number
#using a for loop instead of a while loop.

num=int(input("Enter number: "))

for i in range(1, 13):
    print(num*i ,end=" ")