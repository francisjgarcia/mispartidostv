from dotenv import dotenv_values

# Set dotenv
config = dotenv_values(".env")

# Get API token
todoist_token = config['TODOIST_TOKEN']

# Scrapy general settings
scrapy_settings = {
    'FEED_EXPORT_ENCODING': 'utf-8',
    'LOG_ENABLED': 'False',
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
}
