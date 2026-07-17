import os
import requests
import sqlalchemy as db
import pandas as pd


def convert(amount, rate):
    # Normal: convert(100, 13.4) -> 1340.0
    # Weird: convert(0, 13.4) -> 0.0
    # Breaking: convert("100", 13.4) -> TypeError
    return round(amount * rate, 2)


def get_rate(data, currency):
    # Normal: get_rate(data, "GHS") -> USDGHS rate
    # Weird: get_rate(data, "XYZ") -> None
    key = f'USD{currency}'
    if key in data['quotes']:
        return data['quotes'][key]
    return None


def main():
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

    print('*****Disclaimer starting value is in USD*****')
    print()

    amount = float(input("Enter the amount of USD you have: "))
    currency = input("Convert to (e.g. GHS, GBP, EUR): ").upper()

    rate = get_rate(data, currency)
    if rate is not None:
        print(f'{amount} USD = {convert(amount, rate)} {currency}')
    else:
        print(f'Sorry, {currency} is not listed (Or input right currency.)')


if __name__ == '__main__':
    main()
