def convertDate(date):
    day = int(date.split(', ')[1].split(' ')[0])
    month = date.split(', ')[1].split(' ')[2]
    year = int(date.split(', ')[1].split(' ')[4])
    dictionary = {
        'enero': '01',
        'febrero': '02',
        'marzo': '03',
        'abril': '04',
        'mayo': '05',
        'junio': '06',
        'julio': '07',
        'agosto': '08',
        'septiembre': '09', 
        'octubre': '10',
        'noviembre': '11',
        'diciembre': '12'
    }[month]
    return(f"{year}-{dictionary}-{day}")
