import requests

url = 'http://data.fixer.io/api/latest?access_key=054870e781acd0e5e57e731ae4aa271c'

def currency_converter():
    from_currency = input('Enter the country you want to convert from:')
    to_currency = input('Enter the country you want to convert to:')
    amount = float(input('Enter the amount:'))
    
    response = requests.get(url)
    rate = response.json()['rates'][from_currency.upper()]
    amount_conversion = amount/rate
    amount = amount_conversion*(response.json()['rates'][to_currency.upper()])
    amount = round(amount,2)
    return amount

print(currency_converter())