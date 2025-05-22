def gen(max):
    count = 1 
    while count<=max :
        yield count
        count +=1

greet = gen(5)
for cnt in greet:
    print(cnt)