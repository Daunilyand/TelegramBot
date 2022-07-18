import datetime
from time import sleep
import string
time_now = datetime.datetime.now()
print(f'time now: {time_now}')

""" Создаем базу данных для последующего определения времени в строке """
words = {'через': 1}
hour2 = {'час': 1, '1 час': 1, '2 часа': 2, '3 часа': 3, '4 часа': 4, '5 часов': 5, '6 часов': 6,
         '7 часов': 7, '8 часов': 8, '9 часов': 9, '10 часов': 10, '11 часов': 11, '12 часов': 12,
         '13 часов': 13, '14 часов': 14, '15 часов': 15, '16 часов': 16, '17 часов': 17, '18 часов': 18,
         '19 часов': 19, '20 часов': 20, '21 час': 21, '22 часа': 22, '23 часа': 23, }
minute2 = {'минуту': 1, '1 минуту': 1, '2 минуты': 2, '3 минуты': 3, '4 минуты': 4, '5 минут': 5, '6 минут': 6, '7 минут': 7,
           '8 минут': 8, '9 минут': 9, '10 минут': 10, '11 минут': 11,
           '12 минут': 12, '13 минут': 13, '14 минут': 14, '15 минут': 15, '16 минут': 16, '17 минут': 17,
           '18 минут': 18, '19 минут': 19, '20 минут': 20, '21 минуту': 21, '22 минуты': 22,
           '23 минуты': 23, '24 минуты': 24, '25 минут': 25, '26 минут': 26, '27 минут': 27, '28 минут': 28,
           '29 минут': 29, '30 минут': 30, '31 минуту': 31, '32 минуты': 32, '33 минуты': 33,
           '34 минуты': 34, '35 минут': 35, '36 минут': 36, '37 минут': 37, '38 минут': 38, '39 минут': 39,
           '40 минут': 40, '41 минуту': 41, '42 минуты': 42, '43 минуты': 43, '44 минуты': 44,
           '45 минут': 45, '46 минут': 46, '47 минут': 47, '48 минут': 48, '49 минут': 49, '50 минут': 50,
           '51 минуту': 51, '52 минуты': 52, '53 минуты': 53, '54 минуты': 54, '55 минут': 55, '56 минут': 56,
           '57 минут': 57,
           '58 минут': 58, '59 минут': 59}
day = {'1 ': 1, '2 ': 2, '3 ': 3, '4 ': 4, '5 ': 5, '6 ': 6, '7 ': 7, '8 ': 8, '9 ': 9, '10 ': 10,
       '11 ': 11, '12 ': 12, '13 ': 13, '14 ': 14, '15 ': 15, '16 ': 16, '17 ': 17, '18 ': 18, '19 ': 19,
       '20 ': 20, '21 ': 21, ' 22 ': 22, '23 ': 23, '24 ': 24, '25 ': 25, '26 ': 26, '27 ': 27,
       '28 ': 28, '29 ': 29, '30 ': 30, '31 ': 31}
month = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
         'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
year = {'2022': 2022, '2023': 2023}
hour = {'01:': 1, '02:': 2, '03:': 3, '04:': 4, '05:': 5, '06:': 6, '07:': 7, '08:': 8, '09:': 9, '10:': 10, '11:': 11,
        '12:': 12,
        '13:': 13, '14:': 14, '15:': 15, '16:': 16, '17:': 17, '18:': 19, '19:': 20, '20:': 20, '21:': 21, '22:': 22,
        '23:': 23}
minute = {':01': 1, ':02': 2, ':03': 3, ':04': 4, ':05': 5, ':06': 6, ':07': 6, ':08': 8, ':09': 9, ':10': 10,
          ':11': 11, ':12': 12, ':13': 13, ':14': 14, ':15': 15,
          ':16': 16, ':17': 17, ':18': 18, ':19': 19, ':20': 20, ':21': 21, ':22': 22, ':23': 23, ':24': 24, ':25': 25,
          ':26': 26, ':27': 27, ':28': 28, ':29': 29, ':30': 30,
          ':31': 31, ':32': 32, '33': 33, '34': 34, '35': 35, '36': 36, '37': 37, '38': 38, '39': 39, '40': 40,
          '41': 41, '42': 42, '43': 43, '44': 44, '45': 45,
          '46': 45, '47': 47, '48': 48, '49': 49, '50': 50, '51': 51, '52': 52, '53': 53, '54': 54, '55': 55, '56': 56,
          '57': 57, '58': 58, '59': 59}

""" Делаем несколько циклов для прогона БД и вычисления даты в тексте, далее заносим полученные данные в переменные """

mess = 'Разбудить через 2 часа 1 минуту'
def timer():
    time_now = datetime.datetime.now()
    for k, v in words.items():
        qwe = k in mess
        if qwe == 1:
            year1 = time_now.year
            month1 = time_now.month
            day1 = time_now.day
            for k, v in hour2.items():
                exist = k in mess
                if exist == 1:
                    hour1 = hour2[k]
                    break
                else:
                    hour1 = 0

            print(f'hour {hour1}')
            for k, v in minute2.items():
                exist = k in mess
                if exist == 1:
                    minute1 = minute2[k]
                    break
                else:
                    minute1 = 0
            print(f'minute {minute1}')
            words_list = list(words.keys())
            hour2_list = list(hour2.keys())
            minute2_list = list(minute2.keys())
            res_list = hour2_list + words_list + minute2_list
            print(res_list)
            message = mess
            for word in res_list:
                if word in message:
                    message = message.replace(word, '')
            print(message)
            time = minute1 * 60 + hour1 * 60 * 60
            sleep(time)
            print('даб')
            break


def Alarm_Clock():
    time_now = datetime.datetime.now()
    for k, v in year.items():
        exist = k in mess
        if exist == 1:
            year1 = year[k]
            break
        else:
            year1 = time_now.year
    print(f'year {year1}')
    for k, v in month.items():
        exist = k in mess
        if exist == 1:
            month1 = month[k]
            break
        else:
            month1 = time_now.month
    print(f'month {month1}')
    for k, v in day.items():
        exist = k in mess
        if exist == 1:
            day1 = day[k]
            break
        else:
            day1 = time_now.day
    print(f'day {day1}')
    for k, v in hour.items():
        exist = k in mess
        if exist == 1:
            hour1 = hour[k]
            break
        else:
            hour1 = time_now.hour
    print(f'hour {hour1}')
    for k, v in minute.items():
        exist = k in mess
        if exist == 1:
            minute1 = minute[k]
            break
        else:
            minute1 = time_now.minute
    print(f'minute {minute1}')
    # Создаем будильник

    while True:
        time_now = datetime.datetime.now()
        if time_now.year == year1 and time_now.month == month1 and time_now.day == day1 and time_now.hour == hour1 and time_now.minute == minute1:
            print('бам бум')
            break
        sleep(1)
timer()
