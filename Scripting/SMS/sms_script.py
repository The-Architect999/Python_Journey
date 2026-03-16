#usecases:
#send myself a text message that checks the stock and sends me a text
#portfolio check notification

import yfinance as yf
import sys

def get_tesla_price():
    try:
        #Create a 'Ticker' object for Tesla
        tesla = yf.Ticker("TSLA")
        #Get 'fast_info' (highly optimized for speed)
        #'last_price' is the standard for real-time price
        data = tesla.fast_info
        price = data['last_price']
        currency = data['currency']
        return f"TSLA Current Price: {price:.2f} {currency}"
    
    except Exception as e:
        return f"Error fetching stock data: {e}"

def send_update(stock):
    from twilio.rest import Client
    account_sid = None
    auth_token = None
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid=None,
    body= f'Scout1: information you asked for Architect: {stock}',
    to=None
    )
    print(f"sid:{message.sid}")


if __name__ == "__main__":
    print("Scout1: sending real time stock feed")
    send_update(get_tesla_price())
    sys.exit(0)