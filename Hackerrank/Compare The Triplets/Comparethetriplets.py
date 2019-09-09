
Alice=input("")
Bob=input("")

print(Alice)
print(Bob)

Alice=Alice.split()
Bob=Bob.split()


a=0
b=0
for i in range(3):

    if(int(Alice[i])>int(Bob[i])):
        a+=1
    if(int(Alice[i])<int(Bob[i])):
        b+=1
    else:
        continue

print(a,b)

"""
 RESTART: C:/Users/admin/Desktop/old codes/Hackerrank/Compare The Triplets/Comparethetriplets.py 
5 6 7
3 6 10
5 6 7
3 6 10
1 1
>>> 
 RESTART: C:/Users/admin/Desktop/old codes/Hackerrank/Compare The Triplets/Comparethetriplets.py 
17 28 30
99 16 8
17 28 30
99 16 8
2 1
>>> 


"""

        

        
