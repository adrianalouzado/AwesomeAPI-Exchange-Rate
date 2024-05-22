import requests
4


# Request the prices from the API and convert to JSON
price = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

# Extract the exchange rates
exchange_rates = {
    "USD": float(price['USDBRL']['bid']),
    "EUR": float(price['EURBRL']['bid']),
    "BTC": float(price['BTCBRL']['bid'])
}

def convert_currency(currency):
    rate = exchange_rates[currency]
    value_real = float(input(f'How many reais do you want to convert to {currency}? '))
    result = value_real / rate
    print(f'\nTotal in {currency} = {result:.2f}')
    print(f'Total in reais = {value_real:.2f}')

def main():
    options = {"1": "USD", "2": "EUR", "3": "BTC"}
    
    while True:
        print('\n1 - USD \n2 - EUR \n3 - BTC \n4 - END THE PROGRAM')
        choice = input('\nChoose one option above: ')
        
        if choice == "4":
            print('\nEnding the program')
            break
        elif choice in options:
            convert_currency(options[choice])
        else:
            print('\nInvalid option. Please, try again.')

if __name__ == "__main__":
    main()

            


                





