dim=int(input(''))
arr=[]

for i in range(dim):
    arr.append('[]')
for i in range(dim):
    arr[i]=list(map(int,input().split()))
l=0
r=0
for i in range(dim):
   for j in range(dim):
        if i==j:
            l+=arr[i][j]
        if(j==dim-1-i):
            r+=arr[i][j]    

print(abs(l-r))

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Hackerrank/Diagonal Difference/Diagonaldifference.py 
3
11 2 4
4 5 6
10 8 -12
15
>>> 
"""
