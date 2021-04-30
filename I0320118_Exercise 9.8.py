import array
li = [10,20,30,40,50]

C = array.array('i',[10,20,30,40,50])
C.fromlist(li)
print(type(C))

for nilai in C:
    print(" %d " % nilai, end= '')