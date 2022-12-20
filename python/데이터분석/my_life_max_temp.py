import csv
f1 = open('temp(1978-).csv','r')
f = csv.reader(f1)

# head pass``
header = next(f)
max_temp = -999
day = ''
year = int(input('태어난 해를 입력하세요:'))
for row in f:
    if len(row) >2:                     # 빈 줄이 포함되어 있어 제외가 필요함.
        y,m,d = row[2].split('-')       # 일시정보 구하기 2007-01-02
        if int(y) >= year:              # 태어난 해부터 이후 날 
            if row[4]!='':              # 기상청 데이터 중 없는 것이 존재함.
                tmp = float(row[4])
                if max_temp < tmp :
                    max_temp = tmp
                    day = row[2]
            
print('내 생에 가장 더운 날은 :',day,'기온은:',max_temp)

f1.close()
