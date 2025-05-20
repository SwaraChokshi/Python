myfile = open("my.txt","w")

myfile.write("Hello World\n ")
myfile.write("This is my first file")

myfile.close()

m= open("my.txt","r")
print(m.read())
print(m.read()) #this will not print anything because as after one read function the file position has gone to the end of the file 

m.seek(0)
print(m.read())
myfile.close()
