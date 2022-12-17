import requests

params = {
  'access_key': '3964442e933678c640eb5d454b940bcd'
}

api_result = requests.get('https://api.marketstack.com/v1/tickers/aapl/eod', params)

api_response = api_result.json()

for stock_data in api_response['data']:
    print((stock_data))
    # print(u'Ticker %s has a day high of  %s on %s' % (stock_data['symbol'],stock_data['high'],stock_data['date']))ate']))