import requests 
import json

price = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
price = price.json()
#print(price.content)

price_dolar = float(price['USDBRL']['bid'])
price_euro = float(price['EURBRL']['bid'])
price_bitcoin = float(price['BTCBRL']['bid'])

def conversion_dolar():
    print('\nUpdated value of the dollar in reais : {}'.format(price_dolar))
    value_real = float(input('How many reais you want to convert? '))
    result = value_real / price_dolar
    print('\nTotal em dólar = {}'.format(result))
    print('Total em reais = {}'.format(value_real))

def conversion_euro():
    print('\nUpdated value of the euro in reais : {}'.format(price_euro))
    value_real = float(input('How many reais you want to convert? '))
    reuslt = value_real / price_euro
    print('\nTotal in euro = {}'.format(reuslt))
    print('Total in reais = {}'.format(value_real))

def conversion_bitcoin():
    print('\nUpdated value of the bitcoin in reais :  {}'.format(price_bitcoin))
    value_real = float(input('How many reais you want to convert? '))
    result = value_real / price_bitcoin
    print('\nTotal in bitcoin = {}'.format(result))
    print('Total in reais = {}'.format(value_real))

def main():

    while True: 
        print('\n1 - USD ')
        print('2 - EUR ')
        print('3 - BTC ')
        print('4 - END THE PROGRAM')

        opcao_menu = int(input('\nChoose one option above:  '))

        match opcao_menu:
            case 1: 
                conversion_dolar()

            case 2:
                conversion_euro()
                
            case 3:
                conversion_bitcoin()
            
            case 4:
                print('\nEnding the program')
                break
            
            case _: 
                print('\nInlavid option. Please, try again.')

            


                





