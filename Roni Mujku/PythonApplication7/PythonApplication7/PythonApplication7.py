class GradeBook():

    def __init__(self):
        self.__myDict = {}
        self.flag = False

    def Add_Student(self):
        myStudent = input("Enter student name:")
        mytempGrade = input("Enter student grade(s):")
        myGrade = mytempGrade.split(",")
        self.__myDict[myStudent] = myGrade
        print("New entry complete!")

    def Add_Grades(self):
        myStudent = input("Enter student name:")
        GradetoAdd = input("Enter students new grade(s):")
        tempGrade = self.__myDict[myStudent]
        tempGrade.append(GradetoAdd)
        self.__myDict[myStudent] = tempGrade
        print("Grades Updated")

    def View_GradeBook(self):
        print(self.__myDict)

    def Calc_Avg(self):
        temp = list(self.__myDict.values())
        total = 0
        num = 0
        for items in temp:
            for i in items:
                total = total + int(i)
                num += 1
        print (total / num)



def run_Program():
    myGradebook = GradeBook()
    flag = False
    while flag != True:
        ChosenFunc = input("What would you like to do?:")
        if (ChosenFunc == "Add Student"):
            myGradebook.Add_Student()
        elif (ChosenFunc == "Add Grades"):
            myGradebook.Add_Grades()
        elif (ChosenFunc == "View Gradebook"):
            myGradebook.View_GradeBook()
        elif (ChosenFunc == "Calculate Average"):
            myGradebook.Calc_Avg()
        elif (ChosenFunc == "Quit"):
            print("End of program")
            flag = True


run_Program()