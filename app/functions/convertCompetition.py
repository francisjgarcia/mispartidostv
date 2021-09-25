def convertCompetition(competition):
    dictionary = {
        'La Liga': 'LaLiga Santander',
        'Copa del Rey': 'Copa del Rey',
        'LaLiga SmartBank': 'LaLiga SmartBank',
        'LaLiga SmartBank': 'LaLiga SmartBank',
        'Premier League': 'Premier League',
        'Serie A Italiana': 'Serie A',
        'Bundesliga': 'Bundesliga',
        'Francia Ligue 1': 'Ligue 1',
        'Champions League': 'Champions League',
        'Supercopa Europa': 'Supercopas',
        'Supercopa de España': 'Supercopas',
        'UEFA Nations League': 'Selecciones',
        'FIFA Copa Mundial Catar 2022': 'Selecciones'
        }
    for item in dictionary:
        if item == competition:
            return(dictionary[competition])
