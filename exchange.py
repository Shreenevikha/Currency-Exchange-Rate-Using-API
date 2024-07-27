import requests

# API key is not needed for this endpoint
BASE_URL = 'https://v6.exchangerate-api.com/v6/bf8564b8c225c26d0b1c2073/latest/'

# List of currencies to check
CURRENCIES = ['USD', 'EUR', 'INR', 'PKR', 'GBP', 'JPY', 'AUD', 'AED','CAD']

def get_exchange_rates(base_currency='USD'):
    url = BASE_URL + base_currency
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data, Status code {response.status_code}")
        return None

def display_rates(rates, base_currency):
    print(f"Exchange rates based on {base_currency}:")
    for currency in CURRENCIES:
        if currency == base_currency:
            continue  # Skip displaying the base currency rate
        rate = rates.get(currency, 'N/A')
        print(f"1 {base_currency} = {rate} {currency}")

def main():
    # Prompt user for base currency
    base_currency = input(f"Enter the base currency code from {', '.join(CURRENCIES)}: ").upper()
    
    if base_currency not in CURRENCIES:
        print(f"Invalid base currency code: {base_currency}. Please enter a valid code.")
        return
    
    data = get_exchange_rates(base_currency)
    
    if data:
        rates = data.get('conversion_rates', {})  # Adjust key based on actual response
        display_rates(rates, base_currency)

if __name__ == '__main__':
    main()



