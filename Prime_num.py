def func(num):
 a = 2
count = 0
while count < num:
    for b in range(2, int(a ** 0.5)+1):
        if a % b == 0:
            break
        else :
            print(a)
            count +=1
            a +=1
            
           num = 20
func(num)