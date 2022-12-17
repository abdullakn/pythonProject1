n=int(input("enter the size of the array"))
array_list=[]
for i in range(0,n):
    ele=int(input("enter array elements"))
    array_list.append(ele)
search=int(input("enter search values"))
for i in range(0,n):
    if array_list[i] == search:
        flag=i
        break


if flag==0:
    print("element not found")
else:
    print("element found at position",flag+1)





