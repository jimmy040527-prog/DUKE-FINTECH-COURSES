import json
import sys


def load_currency_data(filename):
    """Load the historical currency data from the JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Data file does not exist", file=sys.stderr)
        sys.exit(3)
    except json.JSONDecodeError:
        print("Data file contains invalid JSON", file=sys.stderr)
        sys.exit(4)


if len(sys.argv) != 2:
    print("Invalid number of command-line arguments", file=sys.stderr)
    sys.exit(2)

filename = sys.argv[1]

historical_data = load_currency_data(filename)

sample_date = next(iter(historical_data))

source_currency_code = input("Enter source currency code: ")
if source_currency_code not in historical_data[sample_date]:
    print("Invalid currency code", file=sys.stderr)
    sys.exit(5)

target_currency_code = input("Enter target currency code: ")
if target_currency_code not in historical_data[sample_date]:
    print("Invalid currency code", file=sys.stderr)
    sys.exit(5)

try:
    amount = float(input("Enter amount to convert: "))
except ValueError:
    print("Invalid amount to convert", file=sys.stderr)
    sys.exit(8)

if amount <= 0:
    print("Invalid amount to convert", file=sys.stderr)
    sys.exit(8)

historical_date = input("Enter historical date (YYYY-MM-DD): ")
if historical_date not in historical_data:
    print("Invalid date / date not in file", file=sys.stderr)
    sys.exit(6)

if not isinstance(historical_data[historical_date], dict):
    print("Invalid date / date not in file", file=sys.stderr)
    sys.exit(6)

source_rate = historical_data[historical_date][source_currency_code]
target_rate = historical_data[historical_date][target_currency_code]

if not isinstance(source_rate, (int, float)):
    print("Date rate for a particular current code is not > 0", file=sys.stderr)
    sys.exit(7)

if not isinstance(target_rate, (int, float)):
    print("Date rate for a particular current code is not > 0", file=sys.stderr)
    sys.exit(7)

if source_rate <= 0 or target_rate <= 0:
    print("Date rate for a particular current code is not > 0", file=sys.stderr)
    sys.exit(7)

historical_rate = target_rate / source_rate

converted_amount_historical = amount * historical_rate

last_date = max(historical_data.keys())

last_source_rate = historical_data[last_date][source_currency_code]
last_target_rate = historical_data[last_date][target_currency_code]

if not isinstance(last_source_rate, (int, float)):
    print("Date rate for a particular current code is not > 0", file=sys.stderr)
    sys.exit(7)

if not isinstance(last_target_rate, (int, float)):
    print("Date rate for a particular current code is not > 0", file=sys.stderr)
    sys.exit(7)
    
if last_source_rate <= 0 or last_target_rate <= 0:
    print("Date rate for a particular current code is not > 0", file=sys.stderr)
    sys.exit(7)

last_rate = last_target_rate / last_source_rate

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