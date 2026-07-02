import requests

API_Key = 'd25b7dfc51bd5fa5e70d69997bcc6251'
url = f'https://api.currencylayer.com/live?access_key={API_Key}'

response = requests.get(url)
# print(response.json())

data = response.json()

print('Disclaimer starting value is in USD')
print()

amount = float(input("Enter the amount of USD you have: "))
currency = input("Convert to (e.g. GHS, GBP, EUR): ").upper()

if f'USD{currency}' in data['quotes']:
  rate = data['quotes'][f'USD{currency}']
  conversion = round (amount * rate, 2)
  print(f'{amount} USD = {conversion} {currency}')
else:
  print(f'Sorry, {currency} is not listed (Or input right currency.)')