


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
n=int(input("enter the size of the array"))
array_list=[]
for i in range(0,n):
    ele=int(input("enter array elements"))
    array_list.append(ele)

insertionSort(array_list)
print('Sorted Array in Ascending Order:')
print(array_list)