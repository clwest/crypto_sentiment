import urllib.request
import json
from jinja2 import Environment, FileSystemLoader


tickers = ''
for i in range(1, 3):
    # 250 tickets per page.  we are going to request 10 pages from Coingecko so that is 2,500 tickers
    endpoint = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={i}&sparkline=false'

    with urllib.request.urlopen(endpoint) as url:
        # convert to a json
        data = json.loads(url.read().decode())
        for crypto in data:
            tickers = tickers + "'" + crypto['symbol'].upper() + "'" + ','
file_loader = FileSystemLoader('./')
env = Environment(loader=file_loader)
# dynamically create a file of tickers using the template file so it is in the correct format for the program
template = env.get_template('sentiment_reddit_temp.py')
output = template.render(tickers=tickers)
# save the results in sentiment_reddit_config.py
with open("sentiment_reddit_config.py", "w") as fh:
    fh.write(output)