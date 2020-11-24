import requests

# function = "TIME_SERIES_DAILY"
# symbol = "MSFT"
# interval = false
# apikey = "V99OXX7I53299L7A"

# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min

msft = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=V99OXX7I53299L7A")
response = msft.json()
# print(response)


# MSFT close price.(Microsoft)
print("Microsoft stock price for 11/23/2020")
print(f"${response['Time Series (Daily)']['2020-11-23']['4. close']}")

# AAPL close price.(Apple)
print("Apple Stocks price for 11/23/2020")
appl = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=V99OXX7I53299L7A")
response = appl.json()
# print(response)
print(f"${response['Time Series (Daily)']['2020-11-23']['4. close']}")

# GOOGL close price(Google)
print("Google stocks price for 11/23/2020")
googl = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&apikey=V99OXX7I53299L7A")
response = googl.json()
print(f"${response['Time Series (Daily)']['2020-11-23']['4. close']}")
# HPQ close price
print("HP stocks price for 11/23/2020")
hpq = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=HPQ&apikey=V99OXX7I53299L7A")
response = hpq.json()
print(f"${response['Time Series (Daily)']['2020-11-23']['4. close']}")

#########################################################################

