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
        'M+ #Vamos': '#Vamos',
        'M+ LaLiga TV': 'M+ LaLiga',
        'M+ LaLiga TV 2': 'M+ LaLiga TV 2',
        'M+ LaLiga TV 3': 'M+ LaLiga TV 3',
        'M+ LaLiga TV 4': 'M+ LaLiga TV 4',
        'M+ LaLiga TV 5': 'M+ LaLiga TV 5',
        'LA LIGA TV Hypermotion': 'LaLiga TV Hypermotion',
        'LA LIGA TV Hypermotion 2': 'LaLiga TV Hypermotion 2',
        'LA LIGA TV Hypermotion 3': 'LaLiga TV Hypermotion 3',
        'M+ Liga de Campeones': 'M+ Liga de Campeones',
        'M+ Liga de Campeones 1': 'M+ Liga de Campeones 1',
        'M+ Liga de Campeones 2': 'M+ Liga de Campeones 2',
        'M+ Liga de Campeones 3': 'M+ Liga de Campeones 3',
        'M+ Liga de Campeones 4': 'M+ Liga de Campeones 4',
        'M+ Liga de Campeones 5': 'M+ Liga de Campeones 5',
        'M+ Liga de Campeones 6': 'M+ Liga de Campeones 6',
        'M+ Liga de Campeones 7': 'M+ Liga de Campeones 7',
        'M+ Liga de Campeones 8': 'M+ Liga de Campeones 8',
        'M+ Liga de Campeones 9': 'M+ Liga de Campeones 9'
        }
    for item_channel in channel:
        channel_name = item_channel.split("(")[0].rstrip()
        for item in dictionary:
            if item == channel_name:
                return(dictionary[channel_name])
