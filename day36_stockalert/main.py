import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "ENTER YOUR API KEY"
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": "ENTER YOUR API KEY"
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
close_value =[value for (key, value) in stock_data.items()]

yesterday_data = close_value[0]
yesterday_closing_price = float(yesterday_data["4. close"])


day_before_yesterday_data = close_value[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])


difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
percentage_difference = (difference / yesterday_closing_price) * 100

if percentage_difference > 0:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    article = news_response.json()["articles"]

    three_articles = article[:3]

    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
