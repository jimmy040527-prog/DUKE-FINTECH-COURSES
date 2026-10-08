import os
import json
import time
import requests
from datetime import datetime, timedelta

# Configuration
API_KEY = ""
BASE_CURRENCY = "USD"
NUM_DAYS = 4000
SLEEP_INTERVAL = 7  # seconds between API calls
BASE_URL = "https://api.freecurrencyapi.com/v1/historical"

# Create output directories if they don't exist
RAW_DATA_DIR = "raw_data"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def get_date_string(date):
    """Format date as YYYYMMDD for API call."""
    return date.strftime("%Y%m%d")

def fetch_historical_data(date):
    """Fetch historical currency data for a specific date."""
    formatted_date = get_date_string(date)
    
    url = f"{BASE_URL}?apikey={API_KEY}&date={formatted_date}&base_currency={BASE_CURRENCY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-2XX responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {formatted_date}: {e}")
        return None

def save_daily_data(data, date):
    """Save the daily data to a file."""
    if data is None:
        return False
    
    filename = os.path.join(RAW_DATA_DIR, f"currency_data_{get_date_string(date)}.json")
    with open(filename, 'w') as f:
        json.dump(data, f)
    
    return True

def merge_files():
    """Merge all the individual files into one consolidated file."""
    print("Merging files...")
    all_data = {}
    
    # Get all JSON files in the directory
    files = [f for f in os.listdir(RAW_DATA_DIR) if f.endswith('.json')]
    
    for file in files:
        filepath = os.path.join(RAW_DATA_DIR, file)
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                # Extract the date and rates from the data
                for date, rates in data.get('data', {}).items():
                    all_data[date] = rates
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {file}")
    
    # Save the consolidated data
    with open('historical_currency_data.json', 'w') as f:
        json.dump({"data": all_data}, f)
    
    print(f"Merged data saved to historical_currency_data.json")

def main():
    # Calculate the date range (from yesterday going back NUM_DAYS)
    end_date = datetime.now() - timedelta(days=1)  # Yesterday
    start_date = end_date - timedelta(days=NUM_DAYS)
    
    current_date = end_date
    success_count = 0
    failure_count = 0
    
    print(f"Starting data collection from {end_date.strftime('%Y-%m-%d')} back to {start_date.strftime('%Y-%m-%d')}")
    
    while current_date >= start_date:
        print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}...")
        
        data = fetch_historical_data(current_date)
        if save_daily_data(data, current_date):
            success_count += 1
        else:
            failure_count += 1
        
        current_date -= timedelta(days=1)
        
        # Sleep to avoid hitting API rate limits, but only if we're not on the last iteration
        if current_date >= start_date:
            print(f"Waiting {SLEEP_INTERVAL} seconds before next request...")
            time.sleep(SLEEP_INTERVAL)
    
    print(f"Data collection complete. Successes: {success_count}, Failures: {failure_count}")
    
    # Merge all files into one
    merge_files()

if __name__ == "__main__":
    main()