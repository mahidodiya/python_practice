#decresing pattern
'''
****
***
**
*
'''
for r in range(4,0,-1):
    for c in range(r):
        print("*",end="")
    print()
print("_"*50)    
'''
1234
123
12
1
'''
for r in range(4,0,-1):
    num=1
    for c in range(r):
        print(num,end="")
        num+=1
    print()
print("_"*50)
num=1    
for r in range(1,5):
    for c in range(r):
        print(num,end=" ")
        num+=1
    print()