num=int(input(''))

for i in range(num):
    for j in range(num):
        if j<num-1-i:
            print(" ",end="")
        else:
            print('#',end="")
    print("")

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Coding-Challenges/Hackerrank/Staircase/Staircase.py 
6
     #
    ##
   ###
  ####
 #####
######

>>> 
"""
            

