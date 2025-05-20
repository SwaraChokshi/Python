# this code wont work because the file has not been closed yet
with open("my.txt",mode="r+") as myfile:
    myfile.write("Hello World\n")
    myfile.write("This is my first file") 
    myfile.seek(0)
    print(myfile.read())
    myfile.seek(0)

    print(myfile.read())

    myfile.close()  
