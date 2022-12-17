print("enter the string")
str=input()
str1=" "
for i in str:
  asc=ord(i)+3
  if asc <= 122:
      str1+=chr(asc)
  else:
      str1 += chr(96 + asc%122)
print(str1)
# print(chr(asc))