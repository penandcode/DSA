# https://www.codechef.com/problems/PRIZEPOOL
# cook your dish here
t = int(input())
for i in range(t):
    t1, t2 = map(int, input().split())
    print(t1*10 + t2*90)
