# https://www.codechef.com/problems/SLOWSOLN

# cook your dish here
import math
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    c=x*y
    if(c>=z):
      a=z//y
      k=y*a 
      g=z-k
      result=(a*y*y)+g*g
      print(result)
    else:
        print(x*y*y)
    
