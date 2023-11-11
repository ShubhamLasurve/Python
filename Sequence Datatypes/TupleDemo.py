
print("Demonstration of Tuple")

Tuple1 = (11,"Hello",90.89,False)       # Heterogenous & Ordered 
print(Tuple1)

print(type(Tuple1))
print(len(Tuple1))

print(Tuple1[1])        #Indexed

#Tuple1[0] = 12
#print(Tuple1)          #This is not allowed 

#Tuple1.append(67)      #This is not allowed 

Tuple2 = (11,89,11,67,11)       # Duplicate allowed
print(Tuple2)

for value in Tuple2:
    print(value)

for i in range(len(Tuple2)):
    print(Tuple2[i])