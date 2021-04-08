def getModuleName():
    name = input ("Enter name of Module: ")
    return name


def getTestOne():
    t1 = int(input("Enter mark of Test 1: "))
    """while not isDigit(t1):
        print("Please enter a number")
        t1 = int(input("Enter mark of Test 1: "))"""
    
    while t1 <0 and t1 >100:
        print("Mark must be between 0 and 100")
        t1 = int(input("Enter mark of Test 1: "))
    
    return t1


def getTestTwo():
    t2 = int(input("Enter mark of Test 2: "))
    """while not isDigit(t2):
        print("Please enter a number")
        t2 = int(input("Enter mark of Test 2: "))"""
    
    while t2 <0 and t2 >100:
        print("Mark must be between 0 and 100")
        t2 = int(input("Enter mark of Test 2: "))
    
    return t2

def getTestThree():
    t3 = int(input("Enter mark of Test 3: "))
    """while not isNotDigit(t3):
        print("Please enter a number")
        t3 = int(input("Enter mark of Test 3: "))"""
    
    while t3 <0 and t3 >100:
        print("Mark must be between 0 and 100")
        t3 = int(input("Enter mark of Test 3: "))
    
    return t3

def getTestFour():
    t4 = int(input("Enter mark of Test 4: "))
    """while not isDigit(t4):
        print("Please enter a number")
        t4 = int(input("Enter mark of Test 4: "))"""
    
    while t4 <0 and t4 >100:
        print("Mark must be between 0 and 100")
        t4 = int(input("Enter mark of Test 4: "))
    
    return t4


def getExamMark():
    exam = int(input("Enter exam mark: "))
    """while not isDigit(exam):
        print("Please enter a number")
        exam = int(input("Enter exam mark: "))"""

    while exam <0 and exam >100:
        print("Mark must be between 0 and 100")
        exam = int(input("Enter exam mark: ")) 
    
    return exam * 0.6 

def getDuaPerformance(t1, t2, t3, t4):
    dp = (t1+t2+t3+t4)/4
    return dp

def printStatus(finalResult, module):
    if finalResult >=75:
        print("Congratulations! You passed "+module+" with a distinction! Well done!")
    elif finalResult >=50:
        print("Congratulations! You passed "+module+" and have been promoted to the next level!")
    else:
        print("I am sorry, you have failed. You will have to repeat "+module)

def result():
    moduleName = getModuleName()
    test1 = getTestOne()
    test2 = getTestTwo()
    test3 = getTestThree()
    test4 = getTestFour()

    dp = getDuaPerformance(test1, test2, test3, test4)
    print("DP "+str(dp))
    if dp <40:
        print("You did not qualify to write exams. You will have to repeat "+moduleName+ " next year.")
        exit(0)

    dp = dp *0.4
    exam = getExamMark()
    '''print(exam)'''
    finalResult = dp + exam
    print(finalResult)
    printStatus(finalResult, moduleName)

if __name__ == "__main__":
    result()