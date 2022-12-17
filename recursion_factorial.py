def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)




num=int(input("enter number"))
sum=factorial(num)
print("the the factorial of ",num,"is",sum)
