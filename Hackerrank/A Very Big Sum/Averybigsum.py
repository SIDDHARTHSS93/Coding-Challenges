import math
n=0
n=int(input(""))
if n<1 and n>10:
    print('error')   
ar=[]
sum=0
ar=input()

ar=ar.split()

for i in range(n):
    sum=sum+int(ar[i])

print(sum)

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Hackerrank/A Very Big Sum/Averybigsum.py 
5
1000000001 1000000002 1000000003 1000000004 1000000005
5000000015
>>> 
"""

