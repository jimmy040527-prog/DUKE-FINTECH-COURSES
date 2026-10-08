# Historical Currency Conversion
Here's an algorithm which can help users convert currency from one into another. The system will use both the historical exchange rate and the current exchange rate to compare the conversion results.

## Algorithm
1. Create a list of currencies in the database that contains all available currencies. Also create a database that contains historical and current exchange rates.
2. Let the user enter the source currency and the target currency. Ask the user to enter the abbreviations of the two currencies, such as USD or EUR.
3. Check whether the currencies entered exist in the currency list. If ’yes‘, continue to the next step. If ’no‘, ask the user to enter them again.
4. Ask the user to enter the historical date that he wants to check. The format of the date should be restricted.
5. Find the historical exchange rate for that date and the current exchange rate in the database.
6. Ask the user to enter the amount of source currency he wants to convert.If it's negative, warn the user and try again.
7. Calculate how much target currency can be converted using both the historical exchange rate and the current exchange rate. Then display the results.
8. Compare the historical and current results. Determine whether the target currency has gained or lost purchasing power.
9. Calculate the percentage change in purchasing power and display the result.

## Tests
- Enter source currency:EUR 
        target currency:USD
        amount:100
        historical time: 05/27/2004
        got correct result
- Enter source currency:EUR 
        target currency:UUU
        output ‘the currency name is not correct, try again'
- Enter source currency:EUR 
        target currency:USD
        amount:100000000 or 0.01
        historical date: 05/27/2004
        still got correct result
- Enter source currency:EUR 
        target currency:USD
        amount:-1
        output 'amount can not be negative'
  

