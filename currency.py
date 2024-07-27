import requests

# API key is not needed for this endpoint
BASE_URL = 'https://v6.exchangerate-api.com/v6/bf8564b8c225c26d0b1c2073/latest/'

# List of currencies to check
CURRENCIES = ['USD', 'EUR', 'INR', 'PKR', 'GBP', 'JPY', 'AUD', 'AED','OMR']

def get_exchange_rates(base_currency='USD'):
    url = BASE_URL + base_currency
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data, Status code {response.status_code}")
        return None

def display_target_rate(rates, target_currency, base_currency, amount):
    rate = rates.get(target_currency, 'N/A')
    if rate == 'N/A':
        print(f"Exchange rate for {target_currency} is not available.")
    else:
        equivalent_amount = amount * rate
        print(f"{amount} {base_currency} = {equivalent_amount} {target_currency}")

def main():
    # Prompt user for base currency
    base_currency = input(f"Enter the base currency code from  {', '.join(CURRENCIES)}: ").upper()
    
    if base_currency not in CURRENCIES:
        print(f"Invalid base currency code: {base_currency}. Please enter a valid code.")
        return
    
    data = get_exchange_rates(base_currency)
    
    if data:
        rates = data.get('conversion_rates', {})  # Adjust key based on actual response
        
        # Prompt user for target currency
        target_currency = input(f"Enter the target currency code from {', '.join(CURRENCIES)}: ").upper()
        
        if target_currency not in CURRENCIES:
            print(f"Invalid target currency code: {target_currency}. Please enter a valid code.")
            return
        
        # Prompt user for the amount in base currency
        try:
            amount = float(input(f"Enter the amount in {base_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return
        
        display_target_rate(rates, target_currency, base_currency, amount)

if __name__ == '__main__':
    main()


