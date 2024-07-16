import mycal
def useCalendar(year,month):
    mycal.viewCalendar(year,month)
    pass


if __name__ == '__main__':
    print('start calendar')
    year,month = map(int, input().split())
    useCalendar(year,month)
    print('\n\nend calendar')
