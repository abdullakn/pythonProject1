def add_num(num):
    if num <= 1:
        return num
    else:
        return num+add_num(num-1)


num=int(input("enter number"))
sum=add_num(num)
print("the sum sequence is",sum)

