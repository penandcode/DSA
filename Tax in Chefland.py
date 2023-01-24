# https://www.codechef.com/problems/TAXES
# cook your dish here
for i in range(int(input())):
    t = int(input())
    if(t > 100):
        print(t - 10)
    else:
        print(t)
