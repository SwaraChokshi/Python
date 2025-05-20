def solution(tuple1):
    max_time = 0
    employee_name =''
    for name,time in tuple1:
        if time > max_time:
            max_time = time
            employee_name = name 
            
    return [employee_name,max_time]







tup1 = [("Billy",200),("Sam",300),("John",400)]

result = solution(tup1)
print(result)