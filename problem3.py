#Have the user enter an integer that is smaller than 10
#Find the sum of the series:
#1 + 11 + 111 + 1111 + ....
#for the n terms, where the nth term has n number of 1's

n=int(input("Enter a number smaller than 10: "))
a=1
print("the sum of the series is ", end="")
for i in range(1, n+1):
    print(a, end="")
    a=a+1