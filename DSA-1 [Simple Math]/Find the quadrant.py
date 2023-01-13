# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_FINDQUADRANT/

# TODO: Implement this method
def findQuadrant(x: float, y: float) -> int:
    if(x > 0 and y > 0):
        return "1"
    if(x < 0 and y > 0):
        return "2"
    if(x < 0 and y < 0):
        return "3"
    if(x > 0 and y < 0):
        return "4"

# NOTE: Please do not modify this function
def main():
    x, y = map(float, input().split(' '))
    quadrant = findQuadrant(x, y)
    print(quadrant)


if __name__ == "__main__":
    main()
