
print("Demonstration of Set")

Set1 = {11,78.89,"Hello",True}      #Heterogenous
print(Set1)                 #Unordered

#print(Set1[1])          # Unindexed

for value in Set1:
    print(value)

Set2 = {11,78,89,11,78}
print(Set2)

Set2.add(101)       # Used to add element
print(Set2)

Set2.remove(101)        # Used to remove element
print(Set2)

print("Enter the value that you want to search in Set")
No = int(input())

for value in Set2:
    if(No == value):
        print("Element is present")
        break
    