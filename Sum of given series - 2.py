#  https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_SERIESSUMII/assessment/

# TODO: Implement this method
# from numpy import double


def seriesSumII(A: float, R: float):
    if 1 > R:
        sm = A/(1-R)
    else:
        sm = A/(R-1)
    return sm

# NOTE: Please do not modify this function
def main():

    [A, R] = list(map(float, input().split()))

    result = seriesSumII(A, R)

    print(result)


if __name__ == "__main__":
    main()
