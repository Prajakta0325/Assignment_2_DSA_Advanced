def quick_sort(array):
    if len(array)<1:
        return array
    else:
        pivot = array.pop()
    greater =[]
    smaller = []
    for i in array:
        if pivot<i:
            greater.append(i)
        else:
            smaller.append(i)
    return quick_sort(smaller)+[pivot]+quick_sort(greater)

print(quick_sort([10,80,30,90,40,60]))