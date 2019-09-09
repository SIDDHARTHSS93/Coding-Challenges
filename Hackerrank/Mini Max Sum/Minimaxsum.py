a=list(map(int,input().split()))
arr=[]
for i in range(5):
    arr.append(a[i])

arr.sort()
mini=0
maxi=0
for i in range(4):
    mini+=arr[i]

for i in range(1,5):
    maxi+=arr[i]

print(mini,maxi)

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Coding-Challenges/Hackerrank/Mini Max Sum/Minimaxsum.py 
1 2 3 4 5
10 14
>>> 
"""
