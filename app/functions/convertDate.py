def convertDate(date):
    day = int(date.split(', ')[1].split(' ')[0].split('/')[0])
    month = int(date.split(', ')[1].split(' ')[0].split('/')[1])
    year = int(date.split(', ')[1].split(' ')[0].split('/')[2])
    try:
        daydictionary = {
            1: '01',
            2: '02',
            3: '03',
            4: '04',
            5: '05',
            6: '06',
            7: '07',
            8: '08',
            9: '09',
        }[day]
    except:
        daydictionary = day
    try:
        monthdictionary = {
            1: '01',
            2: '02',
            3: '03',
            4: '04',
            5: '05',
            6: '06',
            7: '07',
            8: '08',
            9: '09',
        }[month]
    except:
        monthdictionary = month
    return(f"{year}-{monthdictionary}-{daydictionary}")
