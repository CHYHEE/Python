from gisa import GisaQuiz
def goTestCenter():
    quiz2 = GisaQuiz()
    students3 = quiz2.makeDataFromFile('.\data','Abc1115.csv')
    temp = quiz2.solveQuiz1(students3)
    quiz2.marking(1,temp)
    temp = quiz2.solveQuiz2(students3)
    quiz2.marking(2,temp)
    temp = quiz2.solveQuiz3(students3)
    quiz2.marking(3,temp)
    temp = quiz2.solveQuiz4(students3)
    quiz2.marking(4,temp)
    pass

if __name__ == '__main__':
    print(__name__)
    print('gisa test quiz start')
    goTestCenter()
    print('gisa test quiz end')
    