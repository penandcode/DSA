# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_NUMBEROFDIVISORSANDSUM/assessment/

# TODO: Implement this method
from typing import List


def numberOfDivisorsAndSum(n: int) -> List[int]:
    t = 0
    add = 0
    for i in range(1, n+1):
        if(n % i == 0):
            t += 1
            add += i
    return [t, add]

# NOTE: Please do not modify this function
def main():
    n = int(input())
    list=numberOfDivisorsAndSum(n)
    print(*list)

if __name__=="__main__":
    main()
