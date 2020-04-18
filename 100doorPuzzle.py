from array import *

doors = array('i', [])
open_count = array('i', [])
closed_count = array('i', [])

# initially all doors will be closed

for i in range(1, 11):
    door = 0
    doors.append(door)
    open_count.append(door)
    closed_count.append(door)
print(doors)
print(open_count)
print(closed_count)

#iterate each walk of the person

for p in range(1, 11):
    #print("WALK", p)
    for d in range(p, 11, p):
        if(d<=10):
            if(doors[d-1]==0):
                doors.insert(d-1, 1)
                doors.pop(d)
                open_count.insert(d-1, open_count[d-1]+1)
                open_count.pop(d)
            else:
                doors.insert(d-1, 0)
                doors.pop(d)
                closed_count.insert(d-1, closed_count[d-1]+1)
                closed_count.pop(d)
    d+=p
#print("The Doors open in the end are ", doors)

count = 1
print("The Doors open \t was opened \t was closed")
for e in doors:
    if(e==1):
        print(count, "\t\t\t",open_count[count-1], "\t\t",closed_count[count-1])
    count+=1


