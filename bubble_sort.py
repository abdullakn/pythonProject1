def bubbleSort(array):
    for i in range(len(array)):
         for j in range(0, len(array) - i - 1):  #after first iteration last value sorted so necxt time cannot travel sorted elements
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

n=int(input("enter the size of the array"))
array_list=[]
for i in range(0,n):
    ele=int(input("enter array elements"))
    array_list.append(ele)
bubbleSort(array_list)

print('Sorted array')
print(array_list)