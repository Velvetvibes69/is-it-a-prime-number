#Take two input from user
lower= int(input("Enter a lower range: "))
upper= int(input("Enter an upper range: "))

print("The prime numberes between", lower, "and", upper, "are:")
#Interat loop from lower limit to upper limit
for num in range(lower, upper +1):
    #All numberes are greater than 1
    if num>1:
        for i in range(2,num):
            if (num % i)== 0:
                break
        else:
            print(num)