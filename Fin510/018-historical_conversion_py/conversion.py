import json


def load_currency_data():
    """Load the historical currency data from the JSON file."""
    try:
        with open('historical_currency_data.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("The historical currency data file does not exist.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from the historical currency data file.")
        return None


source_currency_code = input("Enter source currency code: ")
target_currency_code = input("Enter target currency code: ")
amount = float(input("Enter amount to convert: "))
historical_date = str(input("Enter historical date (YYYY-MM-DD): "))

historical_data = load_currency_data()
historical_rate = (
    historical_data[historical_date][target_currency_code]
    / historical_data[historical_date][source_currency_code]
)

converted_amount_historical = amount * historical_rate

last_date = max(historical_data.keys())

last_rate = (
    historical_data[last_date][target_currency_code]
    / historical_data[last_date][source_currency_code]
)

converted_amount_last = amount * last_rate

value_change = (
    (converted_amount_last - converted_amount_historical)
    / converted_amount_historical
    * 100
)

print()

print(
    f"Historical value ({historical_date}, rate: {historical_rate:.5f}): "
    f"{converted_amount_historical:.2f} {target_currency_code}"
)

print(
    f"Latest value ({last_date}, rate: {last_rate:.5f}): "
    f"{converted_amount_last:.2f} {target_currency_code}"
)

print(f"Change in value: {value_change:.2f}%")