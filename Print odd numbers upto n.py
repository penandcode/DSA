#https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_ODDNUMBERS/

# TODO: Implement this method
from typing import List


def oddNumbers(n: int) -> List[int]:
    ans = []
    for i in range(n+1):
        if(i % 2 != 0):
            ans.append(i)
    return ans
        

# NOTE: Please do not modify this function
def main():
    n = int(input())

    ans = oddNumbers(n)
    print(*ans)


if __name__ == "__main__":
    main()
