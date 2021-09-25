from dotenv import dotenv_values

# Set dotenv
config = dotenv_values(".env")

# Get API token
todoist_token = config['TODOIST_TOKEN']

# Scrapy general settings
scrapy_settings = {
    "FEEDS": {
        "items.json": {"format": "json"},
    },
    'FEED_EXPORT_ENCODING': 'utf-8',
}
