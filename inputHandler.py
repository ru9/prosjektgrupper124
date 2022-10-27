import datetime

def isInt(n):
    try:
        return int(n)
    except:
        if n == '':
            return 'default'
        return False

def isValidChoice(choice, choices):
    if choice in choices:
        return True
    else:
        return False

def inputDate():
    now = datetime.datetime.now()
    year = False
    month = None
    day = None
    h = None
    m = None


    #sjekker år, måned og dag input for at det er et gyldig int. Hvis ingen ting skrives, brukes dagens dato
    while not year:  
        year = isInt(input ('Year (Press enter for current year): '))
        if year == 'default':
            year = now.year
            break
        if not year:
            print(f'''Invalid entry. Input a number''')
            year = None
    while not month:
        month = isInt(input ('Month (Press enter for current month): '))
        if month == 'default':
            month = now.month
            break
        if not month:
            print(f'''Invalid entry. Input a number''')
            month = None
    while not day:
        day = isInt(input ('Day (Press enter for current day): '))
        if day == 'default':
            day = now.day
            break
        if not day:
            print(f'''Invalid entry. Input a number''')
            day = None
   
    #sjekker at time og minutter er gyldige int, og at de er gyldige tidspunkt
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

    return datetime.datetime(year, month, day, h, m)