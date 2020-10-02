#Calculate the factorial of a number. 
#A factorial is defined as:
#5! = 1 * 2 * 3 * 4 * 5
#5! = 120

n=int(input("Enter a number: "))
a=1

for i in range(1, n+1):
    a=a*i
print(str(n) + "! is "+ str(a))


