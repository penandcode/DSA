# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_FINDLARGESTNUMBER/
# TODO: Implement this method
def findLargestNumber(a: float, b: float, c: float) -> float:
    if(a > b and a > c):
        return a
    if(b > a and b > c):
        return b
    if(c > b and b < c):
        return c

# NOTE: Please do not modify this function
def main():
    a, b, c = map(float, input().split(' '))
    ans = findLargestNumber(a, b, c)
    if(ans.is_integer()):
        ans = int(ans)
    print(ans)  


if __name__ == "__main__":
    main()
