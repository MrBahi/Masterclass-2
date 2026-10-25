import os
import requests
from dotenv import load_dotenv

# 1. Safely load the environment file properties into system memory
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

def fetch_exchange_rates():
    # Defensive Pre-Check: Guard against structural loading setup errors
    if not API_KEY or API_KEY == "YOUR_FREE_API_KEY_HERE":
        print("❌ Configuration Error: Valid API key is missing from your hidden .env file.")
        return

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

    # 2. Use try-except boundaries to explicitly catch structural error variations
    try:
        response = requests.get(url, timeout=10)
        
        # Error Type 1 Handled Explicitly: Catch HTTP issues (e.g. 403 Forbidden, 404 Not Found)
        response.raise_for_status()
        
        data = response.json()
        
        # Safe structural dictionary parsing extraction
        rates = data.get("conversion_rates", {})
        
        print("=" * 38)
        print("    LIVE EXCHANGE RATE MATRIX (USD)   ")
        print("=" * 38)
        print(f"American Dollars (USD) : {rates.get('USD', 'N/A')}")
        print(f"Kenyan Shilling (KES)  : {rates.get('KES', 'N/A'):,}")
        print(f"British Pound (GBP)    : {rates.get('GBP', 'N/A')}")
        print(f"Burundian Francs (BIF) : {rates.get('BIF', 'N/A')}")
        print("=" * 38)

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ Network HTTP Error: Server request rejected. Details: {http_err}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Unable to contact server. Check your internet link.")
        
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The server took too long to reply back.")

fetch_exchange_rates()