from telegram.ext import BaseFilter

class FilterTwitterURL(BaseFilter):
    def filter(self, message):
        return 'https://twitter.com/' in message.text

filter_twitter_url = FilterTwitterURL()