#https://docs.python.org/3/library/pdb.html

def sum_two_num(a, b):
    return a+b

def method_to_debug(myArray):
    a = myArray
    findValue = True
    total = 0
    breakpoint()
    if(findValue):
        for number in a:
            total += number
    print(total)


array1 = [10, 20, 30, 40, 50]
method_to_debug(array1)

#print some values
#continue -> to keep the execution going
#next -> next step
#return -> end current method