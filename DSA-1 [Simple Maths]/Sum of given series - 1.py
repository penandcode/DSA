# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_SERIESSUMI/assessment/

# TODO: Implement this method
def seriesSumI(n: int) -> int:
    return (n * (4 * n * n + 6 * n - 1) // 3);

# NOTE: Please do not modify this function
def main():
    n = int(input())

    ans = seriesSumI(n)

    print(ans)


if __name__ == "__main__":
    main()

