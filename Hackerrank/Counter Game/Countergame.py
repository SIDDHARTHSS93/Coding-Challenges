import math

t=int(input(''))
if t>10 or t<1:
    print('error')
n=int(input(''))
if n<0 or n>math.pow(2,64)-1:
    print('error')
l=n
r=0

for i in range(1,t+1):
    if l==1:
        print(l)
        break
    if r==1:
        print(r)
        break
    l=l//2
    r=l
    r=r//2
    l=r
            

            
        
