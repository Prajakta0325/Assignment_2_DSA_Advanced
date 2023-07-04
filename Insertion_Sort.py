def Insertion_Sort(array):
    n=len(array)
    for i in range(1,n):
        temp=array[i]
        j=i-1
        while j>=0 and temp<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=temp
    return array
        
print(Insertion_Sort([98,34,14,12,54,130,130]))