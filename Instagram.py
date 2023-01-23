# https://www.codechef.com/problems/INSTAGRAM
# cook your dish here

for i in range(int(input())):
    t1, t2 = map(int, input().split())
    if(t1 > t2 * 10):
        print("YES")
    else:
        print("NO")
