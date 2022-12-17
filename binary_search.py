def binary_search(array_list,search,n):

    lower=0
    upper=n-1
    flag=0

    while(lower<=upper):
        mid=int(lower+upper/2)
        if array_list[mid] == search:
            return mid
           # flag=1
           # print("item found",mid+1)
           # break

        elif array_list[mid] < search:
            lower=mid+1

        else:
            upper=mid-1
    return -1


n=int(input("enter the size of the array"))
array_list=[]
for i in range(0,n):
    ele=int(input("enter array elements"))
    array_list.append(ele)
search=int(input("enter search values"))

array_list.sort()
print(array_list)
position=binary_search(array_list,search,n)




if position == -1:
    print("not found")

else:
    print("found at",position+1)


# def binary_search(item_list, item):
#     first = 0
#     last = len(item_list) - 1
#     found = False
#     while (first <= last and not found):
#         mid = (first + last) // 2
#         if item_list[mid] == item:
#             found = True
#         else:
#             if item < item_list[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found
#
#
# print(binary_search([1, 2, 3, 5, 8], 6))
# print(binary_search([1, 2, 3, 5, 8], 5))

