from datetime import datetime

message = 'hello'
def getMonthInfo(year,mon):
    space = 0
    lastDay = 0
    now = datetime(year,mon,1)
    
    lastDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if mon==2:
        if year%400==0 or (year%4==0 and year%100!=0):
            lastDays[1] = 29    
    #요일 정보와 빈칸정보의 비교를 통해서 +1을 하면 빈칸 데이터가 나옴
    space = (now.weekday()+1) % 7
    #print(space)
    lastDay = lastDays[mon-1]
    return space,lastDay

def viewCalendar(year,mon):
    #빈칸, 마지막 날 정보를 얻기위해 getMonthInfo함수 사용
    space,lastDay = getMonthInfo(year,mon)   
    print('\t\t\t',year,'년 ',mon,'월')
    print('일','월','화','수','목','금','토',sep='\t',end='\n')
    day = 1
    for _ in range(space):
        print('\t',end='')
    for _ in range(lastDay):
        print(day,end='\t')
        if (space+day)%7==0:
            print()
        day = day + 1    
        pass



class GisaQuiz:
    def makeDataFromFile(self,fileDir,fileName):
        students = []
        with open(fileDir+'\\'+fileName,'r') as file:
            #1-1. 파일안의 컨텐츠에 연결하여 모든 라인을 가져온다.
            lines = file.readlines()
        for line in lines:
            student = []
            # 3.가져온 한줄을 분리한다.(콤마로 분리)
            temp = line[:-1].split(',')
            # 4.분리된 데이터를 타입에 맞추어 분리한다
            stdNo = int(temp[0])
            student.append(stdNo)
            student.append(temp[1])
            for ele in temp[2:8]:
                val = int(ele)
                student.append(val)
            # 5.분리한 데이터를 리스트에 저장한다.
            for ele in temp[8:]:
                student.append(ele)
            # 6.리스트를 리스트에 저장한다.
            students.append(student)
        return students

    def solveQuiz1(self,data):
        #data = makeDataFromFile('.\data','Abc1115.csv')
        quiz1Data = [] #정렬의 대상을 저장할 리스트
        for temp in data:
        #지역코드가 B인 데이터를 quiz1Data에 저장하시오.
            if temp[10] == 'B':
                temp.append(temp[2]+temp[3])
                quiz1Data.append(temp)
            pass
        for index,_ in enumerate(quiz1Data[:-1]):
            for idx,value in enumerate(quiz1Data[index+1:]):
                number = quiz1Data[index][-1]
                if number < value[-1]:
                    temp = quiz1Data[index] #number
                    quiz1Data[index] = value #i
                    quiz1Data[idx+(index+1)] = temp
                    #break
                #print(idx,i)
                elif number == value[-1]:
                    # 점수가 같을 경우 학번을 오름차순으로 정렬하기
                    number = quiz1Data[index][0]
                    if number > value[0]:
                        temp = quiz1Data[index] #number
                        quiz1Data[index] = value #i
                        quiz1Data[idx+(index+1)] = temp
                    pass
                    
                pass
    
        return quiz1Data[4][0]

    def solveQuiz2(self,students):
        #students = makeDataFromFile('.\data','Abc1115.csv')
        quiz2Max = 0
        for student in students:
            quiz2Temp = student[2]+student[3]
            if student[10]=='B':
                if quiz2Max < quiz2Temp:
                    quiz2Max = quiz2Temp    
        return quiz2Max

    def solveQuiz3(self,students):
        #students = makeDataFromFile('.\data','Abc1115.csv')
        quiz3Answer = 0
        count = 0
        for student in students:
            #영어+수학점수 120 이상자료
            if student[3]+student[4] >= 120:
                count = count + 1
                # 총점+점수포인트
                point = 5
                if student[9]=='B':
                    point = 15
                elif student[9]=='C':
                    point = 20
                quiz3Answer = quiz3Answer + (student[7]+point)
            pass
        return quiz3Answer

    def solveQuiz4(self,students):
        #students = makeDataFromFile('.\data','Abc1115.csv')
        count = 0 
        for student in students:
        #성취도가 A, B인 자료에 대해서  
            if student[9]=='A' or student[9]=='B':
                point = 5
                if student[10]=='B':
                    point = 10
                elif student[10]=='C':
                    point = 15
        #국어점수 + 포인트 >= 50 인
                if student[2]+point >=50:
                     #자료건수
                    count = count + 1
        return count

    def marking(self,markNo,answer):
        file = open('.\data\Ans'+str(markNo)+'.txt','w')
        file.write(str(answer))
        file.close()
        pass
    pass
