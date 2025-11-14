def time_string(hours, minutes, time_format):
    
    if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and time_format == '12' or time_format == '24':
        if time_format == '24':
            print(f'{hours:02}:{minutes:02}')
        if time_format == '12':
            if hours < 12 and hours > 0:
                print(f'{hours:02}:{minutes:02}am')
            elif hours == 12:
                print(f'{hours:02}:{minutes:02}pm')
            elif hours == 0:
                print(f'{hours + 12:02}:{minutes:02}am')
            elif hours >= 13 and hours <= 23:
                print(f'{hours - 12:02}:{minutes:02}pm')
            

time_string(15, 38, '24') #returns '15:38'
time_string(8, 3, '24') #returns '08:03'
time_string(0, 5, '24') #returns '00:05'
time_string(11, 15, '12') #returns '11:15am'
time_string(0, 7, '12') #returns '12:07am'
time_string(7, 30, '12') #returns '7:30am'
time_string(12, 46, '12') #returns '12:46pm'
time_string(13, 10, '12') #returns '1:10pm'
time_string(19, 2, '12') #returns '7:02pm'