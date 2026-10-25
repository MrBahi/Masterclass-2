import requests
API_KEY = "rc_live_demo"  # demo key for testing; swap in your own key after signing up

url = "https://api.restcountries.com/countries/v5/names.common/china"
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # 1. Safety Check: If data is a dictionary error message, gracefully exit
    if isinstance(data, dict) and "status" in data:
        print("API Error message:", data.get("message", "Country data not found."))
    else:
        # 2. Safe to extract elements now because data is verified as an array list
        country = data[0]
        
        name = country["name"]["common"]
        # Use .get() defensively in case capital list fields are blank
        capital = country.get("capital", ["N/A"])[0]
        population = country["population"]
        currency = list(country["currencies"].keys())[0]

        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population:,}")
        print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)