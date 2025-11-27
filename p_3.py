#pattern level-3
'''
   *
  ***
 *****
*******
'''
for r in range(1,5):
    print(" "*(5-r)+"*"*(2*r-1))
    
'''
   1
  121
 12321
1234321
'''
for r in range(1,5):
    for c in range(5-r):
        print(" ",end="")
    for c in range(1,r+1):
        print(c,end="")
    for c in range(r-1,0,-1):
        print(c,end="")
    print()
    
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
n = int(input("Enter number of rows: "))

# TOP part (normal pyramid)
for r in range(1, n+1):
    # 1) Spaces
    for c in range(n-r):
        print(" ", end="")
    # 2) Stars
    for c in range(2*r-1):
        print("*", end="")
    print()

# BOTTOM part (reverse pyramid)
for r in range(n-1, 0, -1):
    # 1) Spaces
    for c in range(n-r):
        print(" ", end="")
    # 2) Stars
    for c in range(2*r-1):
        print("*", end="")
    print()
