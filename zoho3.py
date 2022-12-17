
str="find my reversal i am a sentence"
newstr=""
rev=0
for i in range(0,len(str)):
    if str[i]==" " or i==len(str)-1:
        for j in range(i,rev-1,-1):
            newstr+=str[j]
        rev=i
        newstr+=" "
print(newstr)

