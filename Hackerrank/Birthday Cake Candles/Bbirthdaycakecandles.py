import math as m
age=int(input(''))
if age<1 or age>m.pow(10,5):
    print('error')
a=list(map(int,input().split()))
ar=[]
for i in range(age):
    ar.append(a[i])

for i in range(len(ar)):
    if ar[i]<1 or age>m.pow(10,7):
        print('error')

maxi=max(ar)
count=0
for i in range(len(ar)):
    if(ar[i]==maxi):
        count+=1
print(count)

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Coding-Challenges/Hackerrank/Birthday Cake Candles/Bbirthdaycakecandles.py 
4
3 2 1 3
2
>>> 
"""
