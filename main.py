import datetime as dt
import requests
from twilio.rest import Client
import html
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = os.environ.get("stock_api_key")
news_api_key = os.environ.get("news_api_key")

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : stock_api_key
}

news_params = {
    "apiKey" : news_api_key,
    "q" :COMPANY_NAME,
    "pageSize": 5,
    "language" : "en",
    "sortBy" : "popularity"
}

stock_response = requests.get(url= stock_url, params= stock_params)
stock_response.raise_for_status()
data = stock_response.json()
now = dt.datetime.now()
yesterday = now - dt.timedelta(days= 1)
i: int = 2
day_before_yesterday = now - dt.timedelta(days= i)
while day_before_yesterday.weekday() > 4:
    i += 1
    day_before_yesterday = now - dt.timedelta(days= i)
yesterday_stock_price = data["Time Series (Daily)"][f"{yesterday.date()}"]["4. close"]
day_before_yesterday_stock_price = data["Time Series (Daily)"][f"{day_before_yesterday.date()}"]["4. close"]
percentage_change = abs(((float(yesterday_stock_price) - float(day_before_yesterday_stock_price)) / float(day_before_yesterday_stock_price)) * 100)
increase = (((float(yesterday_stock_price) - float(day_before_yesterday_stock_price)) / float(day_before_yesterday_stock_price)) * 100) > 0
worthy_to_report = percentage_change >= 5

if worthy_to_report:
    news_response = requests.get(url= news_url, params= news_params)
    news_response.raise_for_status()
    articles_list = news_response.json()["articles"]
    final_list = []
    for articles in articles_list:
        if len(final_list) == 3:
            break
        if articles["title"] != "[Removed]":
            final_list.append(articles)
    for articles in final_list:
        client = Client(account_sid, auth_token)
        headline = html.unescape(articles["title"])
        brief = html.unescape(articles["description"])
        img = ""
        if increase:
            img = "🔺"
        else:
            img = "🔻"
        body=f"{STOCK}: {img}{int(percentage_change)}%\n{headline}\nBrief: {brief}"
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=body,
            to="whatsapp:+14042039765"
        ) 
        print(message.status)