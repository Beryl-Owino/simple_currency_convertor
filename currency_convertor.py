# this program takes in amount in kenya shilings and coverts it to the desire curreny

exchange_rates = {
    'USD':1.0,
    'EUR':0.85,
    'GBP':0.75,
    'KSH':0.02

}

amount = float(input("Please the amount you will wish to convert: "))
print("supported currency are:")
for index, currency in enumerate(exchange_rates.keys(), start=1):
    print(f"{index}. {currency}")

original_currency = input("what is your currency source: ").upper()
targeted_currency = input("What is you targeted currency(pick from the above list): ").upper()

user_choices = exchange_rates.keys()
if original_currency in user_choices and targeted_currency in user_choices:
    converted_amount = amount * (exchange_rates[targeted_currency] / exchange_rates[original_currency])
    print(f"{amount} in {original_currency} is equal to {converted_amount:.2f} {targeted_currency}")
else:
    print("Invalid currency codes")


