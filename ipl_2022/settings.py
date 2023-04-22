BOT_NAME = "ipl_2022"

SPIDER_MODULES = ["ipl_2022.spiders"]
NEWSPIDER_MODULE = "ipl_2022.spiders"


CONCURRENT_REQUESTS = 12
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) ' \
             'AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'

DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en',
    'User-Agent': USER_AGENT
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
