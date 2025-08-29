#TASK 1

a=input("enter any number: ")
a=int(a)
if a % 2 == 0:
    print(a,"is an even number.")
else:
    print(a,"is an odd number.")

#TASK 2

sum=0
for i in range(1,51):
    sum += i
print("The sum of numbers from 1 to 50 is:", sum)

