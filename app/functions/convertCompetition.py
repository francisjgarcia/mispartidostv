def convertCompetition(competition):
    dictionary = {
        'La Liga EA Sports': 'LaLiga EA Sports',
        'Copa del Rey': 'Copa del Rey',
        'LaLiga Hypermotion': 'LaLiga Hypermotion',
        'Premier League': 'Premier League',
        'Serie A Italiana': 'Serie A',
        'Bundesliga': 'Bundesliga',
        'Francia Ligue 1': 'Ligue 1',
        'Champions League': 'Champions League',
        'Europa League': 'Europa League',
        'Supercopa de Europa': 'Supercopa de Europa',
        'Supercopa de España': 'Supercopa de España',
        'UEFA Nations League': 'UEFA Nations League',
        'Eurocopa 2024': 'Eurocopa 2024'
        }
    for item in dictionary:
        if item == competition:
            return(dictionary[competition])
