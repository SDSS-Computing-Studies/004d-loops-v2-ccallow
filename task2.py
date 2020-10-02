###### Task 2
#Ask the user to enter a name.
#Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of 
# a single if with multiple logical operators

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")
a = str(input("Enter a name: ")).strip()

for i in nameList:
    if a in  nameList:
        print("that name is on the list")
        break
    
else:
    print("That name is not on the list")