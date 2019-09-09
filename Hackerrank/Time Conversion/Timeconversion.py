StTime=input('')

hr=StTime[0]+StTime[1]
hr=int(hr)
milhr=0
rem=""
if(StTime[8]=='P'):
    if hr<12:
       milhr=12+hr
    if hr==12:
        milhr=str('12')
if(StTime[8]=='A'):
    if hr<10:
       milhr='0'+str(hr)
    if hr==12:
        milhr=str('00')
for i in range(2,8):
    rem+=StTime[i]
print(str(milhr)+rem)

"""
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Coding-Challenges/Hackerrank/Time Conversion/Timeconversion.py 
12:45:02PM
12:45:02
>>> 
"""
