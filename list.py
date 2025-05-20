def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    list = []
   
    n = int(input())

    for i in range(0,n) :
        temp = int(input())
        list.append(temp)
       
    
    index_to_delete = int(input("Index"))

    list.pop(index_to_delete-1)

    
    print(list)

if __name__ == '__main__':
    
    main()
