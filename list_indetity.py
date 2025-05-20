array1 = [[0,0],[0,1]]
length = len(array1)
print(length)
count = 0
for i in range (0,len(array1)):
    for j in range (0,len(array1)):
        if i==j:
            if(array1[i][j] == 1):
                count += 1
            else:
                break

if count == length:
    print("Identity matrix")
else:
    print("Not an identity matrix")