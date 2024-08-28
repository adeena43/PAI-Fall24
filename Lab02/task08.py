
conversion_rates = {
    'EUR': 0.93,
    'USD': 1.0,
    'PKR': 280.0,
    'INR': 82.0,
    'JPY': 139.0
}

# List of currencies
currencies = list(conversion_rates.keys())

print("Welcome to the Basic Currency Converter")
print("\nAvailable currencies:")
for i, currency in enumerate(currencies):
    print(f"{i + 1}. {currency}")
from_currency_index = int(input("Choose the number of the currency you want to convert from: ")) - 1
from_currency = currencies[from_currency_index]
amount = float(input(f"Enter the amount in {from_currency}: "))
to_currency_index = int(input("Choose the number of the currency you want to convert to: ")) - 1
to_currency = currencies[to_currency_index]
amount_in_usd = amount / conversion_rates[from_currency]
converted_amount = amount_in_usd * conversion_rates[to_currency]
print(f"\n{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
