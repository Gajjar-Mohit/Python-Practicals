sgpa = int(input('Enter your SGPA: '))


def calculateGrade(sgpa):
    if (sgpa == 10):
        print("you scored O grade")
    elif (sgpa == 9):
        print('you scored A+ grade')
    elif (sgpa == 8):
        print('you scored A grade')
    elif (sgpa == 7):
        print('you scored B+ grade')
    elif (sgpa == 6):
        print('you scored B grade')
    elif (sgpa == 5):
        print('you scored C+')
    elif (sgpa == 4):
        print('you scored P grade')
    elif (sgpa < 4 & sgpa > 0):
        print('you scored F grade')
calculateGrade(sgpa)