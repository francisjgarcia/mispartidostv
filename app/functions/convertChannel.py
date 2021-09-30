def convertChannel(channel):
    dictionary = {
        'La 1 TVE': 'La 1',
        'Antena 3': 'Antena 3',
        'La Sexta': 'La Sexta',
        'Cuatro': 'Cuatro',
        'Telecinco': 'Telecinco',
        'beMad': 'beMad',
        'Energy': 'Energy',
        'GOL': 'GOL',
        'DAZN': 'DAZN',
        '#Vamos': '#Vamos',
        'Movistar LaLiga': 'Movistar LaLiga',
        'Movistar LaLiga 1': 'Movistar LaLiga 1',
        'Movistar LaLiga 2': 'Movistar LaLiga 2',
        'Movistar LaLiga 3': 'Movistar LaLiga 3',
        'Movistar LaLiga 4': 'Movistar LaLiga 4',
        'Movistar LaLiga 5': 'Movistar LaLiga 5',
        'Movistar LaLiga 6': 'Movistar LaLiga 6',
        'Movistar LaLiga 7': 'Movistar LaLiga 7',
        'Movistar LaLiga 8': 'Movistar LaLiga 8',
        'Movistar LaLiga 9': 'Movistar LaLiga 9',
        'M. Liga de Campeones': 'Movistar Liga de Campeones',
        'M. Liga de Campeones 1': 'Movistar Liga de Campeones 1',
        'M. Liga de Campeones 2': 'Movistar Liga de Campeones 2',
        'M. Liga de Campeones 3': 'Movistar Liga de Campeones 3',
        'M. Liga de Campeones 4': 'Movistar Liga de Campeones 4',
        'M. Liga de Campeones 5': 'Movistar Liga de Campeones 5',
        'M. Liga de Campeones 6': 'Movistar Liga de Campeones 6',
        'M. Liga de Campeones 7': 'Movistar Liga de Campeones 7',
        'M. Liga de Campeones 8': 'Movistar Liga de Campeones 8',
        'M. Liga de Campeones 9': 'Movistar Liga de Campeones 9',
        }
    for item_channel in channel:
        channel_name = item_channel.split("(")[0].rstrip()
        for item in dictionary:
            if item == channel_name:
                return(dictionary[channel_name])
