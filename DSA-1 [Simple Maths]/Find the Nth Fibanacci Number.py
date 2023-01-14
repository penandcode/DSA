# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_NTHFIBONACCINUMBER/assessment/

# TODO: Implement this method
def nthFibonacciNumber(n: int) -> int:
    n1 = 0
    n2 = 1
    nth = 0
    if(n == 0):
        return n1
    elif(n == 1):
        return n2
    else:
        for i in range(n-1):
            nth = n1 + n2
            n1 = n2
            n2 = nth
        return nth
# NOTE: Please do not modify this function
def main():
    n = int(input())
    result = nthFibonacciNumber(n)
    print(result)

if __name__=="__main__":
    main()
