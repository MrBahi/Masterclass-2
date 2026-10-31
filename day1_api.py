import requests
API_KEY = "rc_live_demo"  # demo key for testing; swap in your own key after signing up

url = "https://api.restcountries.com/countries/v5/names.common/china"
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    body = response.json()
    countries = body.get("data", {}).get("objects", [])

    if not countries:
        print("No country found.")
    else:
        country = countries[0]

        name = country["names"]["common"]
        capital = country["capitals"][0]["name"]
        population = country["population"]
        currencies = country["currencies"]
        first = currencies[0]
        currency = first["code"] if isinstance(first, dict) else first
        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population:,}")
        print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)
    print(response.json().get("errors"))