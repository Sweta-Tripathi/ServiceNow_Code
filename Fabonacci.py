print('My Fabonacci Series')
nnum = 10000
num = 0
num1 = 0
num2 = 1
count = 0

while(num < nnum):
    print(num1)
    num = num1 + num2
    num1 = num2
    num2 = num
    count +=1