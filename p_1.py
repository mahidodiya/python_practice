#pattern level-1
'''
*
**
***
****
'''
for r in range(1,5):
    for c in range(1,r+1):
        print("*",end='')
    print()
    
'''
1
12
123
1234
'''

for r in range(1,5):
    num=1
    for c in range(1,r+1):
        print(num,end='')
        num+=1
    print()
    
'''
1
22
333
4444
'''
num=1
for r in range(1,5):
    for c in range(1,r+1):
        print(num,end='')
    num+=1
    print()
    
