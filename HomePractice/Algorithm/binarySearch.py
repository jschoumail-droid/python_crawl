#list must be sorted
n=[2,3,5,8,11,12,18]
print(n)

searchFor=12
print('search for:',searchFor)

sliceStart=0
sliceEnd=len(n)-1
found=False

while sliceStart<=sliceEnd and not found:
    location=(sliceStart+sliceEnd)//2
    if n[location]==searchFor:
        found=True
    else:
        if searchFor>n[location]:
            sliceStart=location+1
        else:
            sliceEnd=location-1

print("found={}, index={}".format(found,location))