# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_FACTORIAL/

# TODO: Implement this method
def factorial(n: int) -> int:
    if(n == 0): return 1
    if(n == 1): return 1
    return n * factorial(n - 1)

# NOTE: Please do not modify this function
def main():
    n = int(input())

    ans = factorial(n)
    print(ans)


if __name__ == "__main__":
    main()
