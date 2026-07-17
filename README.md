# Currency Exchange Converter

[![Check Style](https://github.com/goasare/Currency-Exchange/actions/workflows/style.yaml/badge.svg)](https://github.com/goasare/Currency-Exchange/actions/workflows/style.yaml)
![Tests](https://github.com/goasare/Currency-Exchange/actions/workflows/tests.yaml/badge.svg)

A Python program that fetches live exchange rates from the CurrencyLayer API,
stores them in a SQLite database, and converts an amount from USD into a
currency of your choice.

## Setup

Install the required libraries:

    pip install requests sqlalchemy pandas

Set your CurrencyLayer API key as an environment variable:

    export CURRENCY_API_KEY=your_key_here

You can get a free API key by registering at https://currencylayer.com.

## How to Run

    python3 CurrExchange.py

You'll be prompted to enter an amount in USD and a target currency
(e.g. GHS, GBP, EUR).

## How It Works

- The program calls the CurrencyLayer `/live` endpoint to pull current
  USD-based exchange rates.
- The rates (a dictionary of currency pairs) are loaded into a pandas
  DataFrame and written to a SQLite database using SQLAlchemy.
- It queries the database to display all stored rates, then converts the
  user's USD amount into the chosen currency using the matching rate.
