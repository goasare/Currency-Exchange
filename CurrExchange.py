import os
import requests
import sqlalchemy as db
import pandas as pd

API_Key = os.environ.get('CURRENCY_API_KEY')

if not API_Key:
    print("Error: CURRENCY_API_KEY environment variable not set.")
    exit(1)

url = f'https://api.currencylayer.com/live?access_key={API_Key}'

response = requests.get(url)

data = response.json()

quotes = data['quotes']
df = pd.DataFrame.from_dict(quotes, orient='index', columns=['rate'])
df.index.name = 'pair'
df = df.reset_index()

engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('exchange_rates', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(
        db.text("SELECT * FROM exchange_rates;")).fetchall()
    print(pd.DataFrame(query_result))

print('*****Disclaimer starting value is in USD*****')
print()

amount = float(input("Enter the amount of USD you have: "))
currency = input("Convert to (e.g. GHS, GBP, EUR): ").upper()

if f'USD{currency}' in data['quotes']:
    rate = data['quotes'][f'USD{currency}']
    conversion = round(amount * rate, 2)
    print(f'{amount} USD = {conversion} {currency}')
else:
    print(f'Sorry, {currency} is not listed (Or input right currency.)')
