#empty set
s = set()
print(type(s))

#non empty set 
s1 = {1,2,3,4,1,2}
print(s1)

#Adding the item in the set 

s1.add(10)
print(s1)

#updating the set 
name ="Swara"
s1.update(name)
print(s1)

#deeting the item fro the set 
s1.pop()
print(s1)

s1.remove(4)

print(s1)