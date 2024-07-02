# Stock-News-Alert

This Python script monitors the stock price of a company (e.g., Tesla Inc.) and sends a WhatsApp message with news articles when the stock price changes significantly.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your system.
- Necessary Python packages installed. You can install them using `pip`:
  ```
  pip install requests twilio
  ```
- API keys for Alpha Vantage and News API.
- Twilio account SID and Auth Token for sending WhatsApp messages.

## Setup

1. **Environment Variables:**
   - Set the following environment variables:
     - `stock_api_key`: API key for Alpha Vantage.
     - `news_api_key`: API key for News API.
     - `account_sid`: Twilio account SID.
     - `auth_token`: Twilio auth token.

2. **API Key Setup:**
   - Get API keys from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and [News API](https://newsapi.org/docs/get-started).

3. **Twilio Setup:**
   - Sign up for a Twilio account at [Twilio](https://www.twilio.com/try-twilio).
   - Obtain your account SID and auth token from the Twilio console.

4. **Environment Variable Example (Linux/macOS):**
   - Add the following lines to your shell profile (e.g., `.bash_profile`, `.zshrc`):
     ```
     export stock_api_key="your_alpha_vantage_api_key"
     export news_api_key="your_news_api_key"
     export account_sid="your_twilio_account_sid"
     export auth_token="your_twilio_auth_token"
     ```

5. **Run the Script:**
   - Execute the Python script:
     ```
     python stock_news_alert.py
     ```

## Functionality

- The script fetches daily stock prices for the specified company (e.g., Tesla).
- It calculates the percentage change in stock price between yesterday and the day before yesterday.
- If the percentage change is 5% or more, it retrieves the top 3 news articles related to the company using the News API.
- Each article headline and brief description, along with the percentage change in stock price, are sent via WhatsApp using Twilio.

## Notes

- Ensure your environment variables are correctly set before running the script.
- Make sure your Twilio account has sufficient balance or credits to send WhatsApp messages.
- The script assumes a WhatsApp phone number is provided in international format (e.g., `whatsapp:+14042039765`).

---

Save the above content into a file named `README.md` in the same directory as your Python script (`stock_news_alert.py`). This README will help others (and yourself) understand how to set up and use your script effectively. Adjust the instructions as necessary based on your specific setup and requirements.