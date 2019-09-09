n=int(input(''))
if(n<0 or n>100):
    print('error')

arr=[]

arr=list(map(int,input().split()))
for i in range(n):
    if(arr[i]<-100 or arr[i]>100):
        print('error')
p=0
m=0
z=0

for i in range(n):
    if(arr[i]<0):
        m+=1
    if(arr[i]>0):
        p+=1
    if(arr[i]==0):
        z+=1

p=round(p/n,6)
m=round(m/n,6)
z=round(z/n,6)

print("{:.6f}".format(p))
print("{:.6f}".format(m))
print("{:.6f}".format(z))

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Coding-Challenges/Hackerrank/Plus Minus/Plusminus.py 
6
-4 3 -9 0 4 1
0.500000
0.333333
0.166667
>>> 
"""  
