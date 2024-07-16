from datetime import datetime
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