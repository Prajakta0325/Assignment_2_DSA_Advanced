def binary_search(array,key):
    high=len(array)-1
    low=0
    mid=0
    while low<=high:
        mid=(high+low)//2
        if array[mid]<key:
            low=mid+1
        elif array[mid]>key:
            high=mid-1
        else:
            return mid
    return -1
print("Enter Array Elements ")
array= [int(i) for i in input().split()]
key=int(input("Enter value which you want to search :"))
ans= binary_search(array,key)

if ans!=-1:
    print("Element Found at index: ",ans)
else:
    print('element Not Found')
