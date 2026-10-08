# History Currency Conversion

In this assignment, you will create a currency conversion system that allows 
users to convert between different currencies and analyze how exchange rates 
have changed over time. The system will use historical exchange rate data
provided in a JSON file to perform currency conversions and analyze trends.

## Learning Objectives
- Working with nested data structures (dictionaries within dictionaries)
- Processing JSON data in Python
- Implementing currency conversion logic
- Calculating and displaying percentage changes
- Handling user input and formatting output

## Getting Started with JSON
JSON (JavaScript Object Notation) is a lightweight data-interchange format that 
is easy for humans to read and write and easy for machines to parse and generate. 
Source: [json.org](https://www.json.org/json-en.html)

In this assignment, you'll be working with a JSON file that contains historical 
currency exchange rate data.

Python provides a built-in json module that makes it easy to work with JSON data:

```python
import json

# To load JSON data from a file
with open('historical_currency_data.json', 'r') as file:
    currency_data = json.load(file)
```

The currency data is structured as a nested dictionary:

The outer dictionary uses dates as keys (format: "YYYY-MM-DD").
Each date points to an inner dictionary where:

Keys are currency codes (e.g., "USD", "EUR", "CNY").
Values are the exchange rates relative to USD for that date

For example:
```json
{
    "2024-09-05": {
        "AUD": 1.4836202771,
        "EUR": 0.8998501761,
        "JPY": 143.4054205392,
        ...
    },
    "2025-05-13": {
        "AUD": 1.544910166,
        "EUR": 0.8939101759,
        "JPY": 147.5500656321,
        ...
    },
    ...
}
```

## Data Formats
When working with structured data like currency information, various data 
formats can be used to represent and exchange this information: JSON, CSV, XML, 
and Markdown. While not necessary to complete this assignment, we have provided
several different versions of currency information (abbreviations, full names, 
and symbols) for you to see how the different formats represent the same 
information. As with JSON, Python contains application programming interfaces
(APIs) [[wikipedia]](https://en.wikipedia.org/wiki/API) to parse and store these 
different representations.

[JSON](https://en.wikipedia.org/wiki/JSON)  is widely used for APIs and modern 
web applications due to its lightweight structure and ease of parsing by 
programming languages. It supports lists and dictionaries. JSON can also nest 
data structures. Depending upon the complexity and formatting, JSON may or may 
not be human-friendly for casual viewing.

[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) (Comma-Separated 
Values) is a simple, flat format ideal for spreadsheets and quick data 
exchange, but it lacks support for complex or hierarchical structures and 
metadata.

[XML](https://en.wikipedia.org/wiki/XML) (eXtensible Markup Language) is a 
verbose yet powerful format that supports nested structures, data validation 
via schemas, and is ideal for document-centric applications or configurations—
though it can be harder to read and process compared to JSON. At one point,
XML was the leading format used for web and data exchange. It is commonly used 
for enterprise application integration, configuration files, document markup, 
and industry-specific data formatting standards.

[Markdown](https://en.wikipedia.org/wiki/Markdown) offers a clean, readable way
to present data in tables and text—perfect for documentation or user-facing 
content—but it's not suited for programmatic data exchange or complex logic.

Each of these formats excels in different contexts: JSON and XML in structured 
systems integration, CSV in simple data storage and tabular analysis, and 
markdown in readable reports or documentation.

## Assignment Details
Write a Python program in a file called `conversion.py` that performs the
following tasks:

1. Prompts the user to enter a source currency code and allows the user to 
   enter the corresponding three-character code.
2. Prompts the user to enter a target currency code and allows the user to 
   enter that value.
3. Prompts the user to enter an amount to convert and allows the user to
   enter that value.
4. Prompts the user to enter a historical date in the format of YYYY-MM-DD
   and allows the user to enter the date.
5. Loads `historical_currency_data.json` that uses USD as the base currency.
6. Converts the source amount into the corresponding target currency based on 
   both the historical date entered and the most recent date available in the 
   JSON file. Outputs both of these target amounts.
7. Provides a simple analysis to show whether the target currency has
   gained or lost in value by a percentage to two decimal places between
   the two dates.
8. While your user prompts for data do not have to match the sample execution
   below, your output lines must follow the same format.

You can assume that the user has entered valid currency codes, an initial 
amount, and a target date. In a later assignment, we will extend this work
to include data validation.

Once you have validated your program functions correctly on your computer,
submit the assignment to Gradescope for testing.

We have provided `conversion.py` that contains the function to load the 
currency conversion data as well as some sample usages of that data as a
starting point.

## Sample Execution
```
Enter source currency code: USD
Enter target currency code: EUR
Enter amount to convert: 100
Enter historical date (YYYY-MM-DD): 2024-04-01

Historical value (2024-04-01, rate: 0.93117): 93.12 EUR
Latest value (2025-05-16, rate: 0.89497): 89.50 EUR
Change in value: -3.89%
```

## Additional Data Notes
We used [FreecurrencyAPI](https://freecurrencyapi.com/) to gather the historical
data using the `collector.py` program. You do not need to gather the data 
yourself - we have already provided this in `historical_currency_data.json`.
Some items to mention:
- To simplify the data requirements, we assume USD is used as the base 
  currency. In reality, other conversion factors may exist such as 
  directly from the Chinese Yuan to the Euro that may differ slightly.
- We use Python's `datetime` library to help manage dates - specifically for 
  moving from one day to another. While we do not specifically cover
  this API during the class, we have provided an overview of 
  [date/time processing](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/28-DateTime.html)
  in the course notebooks. Inevitably, you will find yourself using dates and 
  times in processing financial data.
- We registered for an API key. If you examine `collector.py`, you'll see 
  that there's a variable to track that key. As API keys are considered "secret"
  information (typically, these keys provide access to a paid resource or 
  can manipulate other systems) they should not be stored in code repositories
  like `git`
- The API has a rate limit of 10 queries per minute on the free plan. As such,
  the program pauses between each request. Additionally, only 5,000 queries
  can be made per month for free accounts.
- In the next course, you will gain more exposure using APIs to access various
  types of data.
- While this amount of data is relatively small, imagine potential problems
  if it were larger. While these questions are out of scope for this current
  class, they will need to be considered in other courses as well as in
  actual use.
  - How do you store the data?
  - Can you load the data completely into memory? If not, how do you 
    access the data?
  - What effects does the data size have on computation time?
  - ...
