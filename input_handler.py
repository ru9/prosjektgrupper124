from datetime import datetime

def isInt(n):
    try:
        return int(n)
    except:
        if n == '':
            return 'default'
        return False

def inputDateTime():

    
    date = inputDate()
    year = date.year
    month = date.month
    day = date.month
    time = inputTime()
    h = time[0]
    m = time[1]

    return datetime(year, month, day, h, m)

def inputDate():
    now = datetime.now()
    year = None
    month = None
    day = None
        #sjekker år, måned og dag input for at det er et gyldig int. Hvis ingen ting skrives, brukes dagens dato
    while not year:  
        year = isInt(input ('År (Press enter for nåværende år): '))
        if year == 'default':
            year = now.year
            break
        elif not year:
            print(f'''Skriv et nummer''')
            year = None
        
    while not month:
        month = isInt(input ('Måned (Press enter for nåværende måned): '))
        if month == 'default':
            month = now.month
            break
        if not month:
            print(f'''skriv et nummer''')            
            month = None
        elif month > 12 or month < 1 :
            print('Skriv et tall mellom 1 og 12 ')
            month = None
    while not day:
        day = isInt(input ('Dag (Press enter for idag): '))
        if day == 'default':
            day = now.day
            break
        if not day:
            print(f'''Invalid entry. Input a number''')
            day = None
        elif day < 1 or day > 31:
            print('Skriv et tall mellom 1 og 31')
            day = None

    return datetime(year, month, day)
   


def inputTime():
    h = None
    m = None
    while not h:
        h = isInt(input ('Hour: '))
        if not h or h =='default':
            print(f'''Invalid entry. Input a number''')
            h = None
        elif h < 0 or h > 23:
            print(f'''Invalid entry. Input a number between 0 and 23''')
        else:
            break
        h = None
    while not m:
        m = isInt(input ('Minute: '))

        if not m or m =='default':
            print(f'''Invalid entry. Input a number''')
        elif m < 0 or m > 60:
            print(f'''Invalid entry. Input a number between 0 and 60''')
        else:
            break
        m = None
    return (h, m)


