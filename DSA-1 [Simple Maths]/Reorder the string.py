# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_STRINGPERMUTATION/

# TODO: Implement this method
from typing import List


def stringPermutation(n: int, s: str, per: List[int]) -> str:
    res = [i for i in range(n)]
    for i in range(n):
        res[per[i]-1] = s[i]
    return "".join(res)

# NOTE: Please do not modify this function
def main():
    n = int(input())
    s = input()
    per = list(map(int, input().strip().split(' ')))

    result = stringPermutation(n, s, per)
    print(result)

if __name__=="__main__":
    main()

