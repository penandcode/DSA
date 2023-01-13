# https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_GRADINGSYSTEM/

# TODO: Implement this method
def gradingSystem(score: float) -> str:
    if(score >=0 and score < 25):
        return "F"
    if(score >=25 and score < 45):
        return "E"
    if(score >=45 and score < 50):
        return "D"
    if(score >=50 and score < 60):
        return "C"
    if(score >=60 and score < 80):
        return "B"
    if(score >=80 and score <= 100):
        return "A"
    else:
        return "Invalid"

# NOTE: Please do not modify this function
def main():
    score = float(input())
    grade = gradingSystem(score)
    print(grade)

if __name__=="__main__":
    main()


