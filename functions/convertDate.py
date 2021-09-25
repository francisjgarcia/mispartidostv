def convertDate(date):
    day = int(date.split(', ')[1].split(' ')[0])
    month = date.split(', ')[1].split(' ')[2]
    year = int(date.split(', ')[1].split(' ')[4])
    dictionary = {
        'enero': 1,
        'febrero': 2,
        'marzp': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9, 
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }[month]
    return(f"{day}/{dictionary}/{year}")
