# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_COPRIMENUMBERS/assessment/


def hcfnaive(x, y):
    while(y):
       x, y = y, x % y
    return x

# TODO: Implement this method
def coprimeNumbers(n: int) -> int:
    coPrimes = []
    for i in range(0, n):
        if hcfnaive(i,n) == 1:
            if i not in coPrimes:
                # print(i)
                coPrimes.append(i)
    return(len(coPrimes))


# NOTE: Please do not modify this function
def main():
    n = int(input().strip())

    countCoPrime = coprimeNumbers(n)
    print(countCoPrime)


if __name__ == "__main__":
    main()
