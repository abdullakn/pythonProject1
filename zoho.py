len=(int(input("Enter the size of the pattern : ")))
space=len-1
for row in range(len):
    val=row+1
    inc=len-1
    for sp in range(space):
        print(end="  ")
    space=space-1
    for col in range(row+1):
        print(val, end=" ")
        val = val + inc
        inc = inc - 1
    print()

# It contain small alignment problem, because number greater than 10 take 2 digits


# commented on zoho in origin master


