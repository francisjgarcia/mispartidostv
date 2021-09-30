def teamPriority(team):
    dictionary = {
        # LaLiga Santander
        'FC Barcelona': 6,
        'Real Madrid': 5,
        'At. Madrid': 5,
        'Sevilla FC': 2,
        'Valencia CF': 2,
        'Athletic Club': 2,
        'Real Sociedad': 2,
        'Villarreal': 2,
        'Celta': 1,
        # LaLiga SmartBank
        'Málaga': 3,
        'Sporting Gijón': 1,
        'Eibar': 1,
        'Leganés': 1,
        'UD Almería': 1,
        'Girona': 1,
        'Real Oviedo': 1,
        'Huesca': 1,
        'Real Valladolid': 1,
        # Premier League
        'Liverpool': 4,
        'Manchester City': 4,
        'Manchester Utd.': 4,
        'Chelsea': 4,
        'Arsenal': 4,
        'Tottenham': 4,
        'Leicester City': 3,
        'Southampton': 2,
        'Everton': 2,
        'Leeds Utd': 1,
        'Watford': 1,
        'Wolves': 1,
        'West Ham': 1,
        # Serie A
        'Juventus': 3,
        'Inter Milan': 3,
        'AC Milan': 3,
        'Napoli': 3,
        'AS Roma': 2,
        'Atalanta': 2,
        'Fiorentina': 2,
        'Torino': 1,
        # BundesLiga
        'FC Bayern': 3,
        'Borussia Dortmund': 3,
        'RB Leipzig': 2,
        'Bayer Leverkusen': 2,
        'Borussia M\'gladbach': 2,
        'VfL Wolfsburg': 2,
        'Eintracht Frankfurt': 1,
        'Mainz 05': 1,
        # Ligue 1
        'PGS': 3,
        'O. Lyonnais': 2,
        'AS Monaco': 2,
        'O. Marseille': 2,
        # Eredivisie
        'Ajax': 3,
        # Primeira Liga
        'Benfica': 3,
        'FC Porto': 3,
        'Sporting CP': 2,
        # Selecciones
        'España': 6,
        'Francia': 4,
        'Alemania': 4,
        'Italia': 4,
        'Inglaterra': 4,
        'Argentina': 4,
        'Brasil': 4,
        'Holanda': 3,
        'Portugal': 3,
        'Bélgica': 3,
        'México': 3,
        'Colombia': 3,
        'Uruguay': 3,
        'Croacia': 3,
        'Chile': 2,
        'Dinamarca': 2,
        'Suiza': 2,
        'Rusia': 1,
        'Ucrania': 1,
        'Suecia': 1,
        'Venezuela': 1,
    }
    try:
        return dictionary[team]
    except:
        return(0)

def competitionPriority(competition):
    dictionary = {
        'La Liga': 3,
        'Copa del Rey': 1,
        'LaLiga SmartBank': 0,
        'Premier League': 3,
        'Serie A Italiana': 1,
        'Bundesliga': 1,
        'Francia Ligue 1': 0,
        'Champions League': 3,
        'Europa League': 2,
        'Supercopa Europa': 3,
        'Supercopa de España': 2,
        'UEFA Nations League': 3,
        'FIFA Copa Mundial Catar 2022': 3
    }
    try:
        return dictionary[competition]
    except:
        return(0)

def fullPriority(local, visitor, competition):
    local_priority= teamPriority(local)
    visitor_priority = teamPriority(visitor)
    competition_pririty = competitionPriority(competition)
    total_priority = local_priority + visitor_priority + competition_pririty
    # return(local_priority, visitor_priority, competition_pririty, total_priority)
    if total_priority >= 0 and total_priority <= 3:
        return(1)
    elif total_priority >= 4 and total_priority <= 6:
        return(2)
    elif total_priority >= 7 and total_priority <= 10:
        return(3)
    elif total_priority >= 11 and total_priority <= 15:
        return(4)

# print(fullPriority("FC Barcelona", "Málaga", "Champions League"))