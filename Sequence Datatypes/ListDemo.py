
print("Demonstration of list")

List1 = [10,"Hello", 67.90,True]        # Heterogenous and Orderedfeature
print(List1)

print(List1[0])     # Indexed feature

List2 = [11,78,90,11,45,78]     # Duplicate allowed
print(List2)

List2[1] = 79       # Data of list is mutable
print(List2)

List2.append(101)       # List id mutable
print(List2)

List2.remove(11)
print(List2)