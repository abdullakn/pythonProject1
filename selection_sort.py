def selectionSort(array, size):
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j
        temp=array[i]
        array[i]=array[min_idx]
        array[min_idx]=temp



n=int(input("enter the size of the array"))
array_list=[]
for i in range(0,n):
    ele=int(input("enter array elements"))
    array_list.append(ele)
size = len(array_list)
selectionSort(array_list, size)
print('Sorted array')
print(array_list)
