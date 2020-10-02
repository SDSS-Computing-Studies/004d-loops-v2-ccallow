##### Task 3
#Given a typle that contains a series of numbers, list all the ones that are
# divisible by 5

numList = (25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99)

for i in numList:
    if i/5 == int(i/5.0):
        print(i)
print("\"\"\"")