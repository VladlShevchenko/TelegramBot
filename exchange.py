import re
import requests
import json


from requests.api import get
URL = 'https://api.exchangerate.host/latest'

class Exchange:
    def __init__(self):
        
        self.base_currency = self.base_input() 
        self.print_database(self.get_database(self.base_currency))

    
    def get_database(self, base: str = "UAH")->dict: 
        """
        func takes base currency and according to this, show exchange rates
        """
        database = requests.get(URL, locals()).json()
        return database

    def get_list_of_currencies(self):
        """
        func return list of all currencies
        """
        database = requests.get(URL).json()
        value = database["rates"].keys()
        return " ".join(map(str, value))
    
    def print_database(self, database):
        """
        func print list of all currencies
        """
        print("\n".join((map(str, database["rates"].items()))).replace(", ", "="))

    def input_ammount_price(self):
        """
        input of second currency and it ammount
        """
        second = input("Enter second currency:")
        ammount = input("Enter ammount of base currency:")
        self.get_ammount_price(second, ammount)

    def get_ammount_price(self, second, ammount):
        """
        return json with rate according to ammount and second currency
        """
        keys = {'base':self.base_currency, 'symbols':second, 'amount':ammount}
        database = requests.get(URL, params=keys).json()
        print("".join(map(str,database["rates"].values())))
        return database["rates"].values()
    
   

    def base_input(self):
        base = input("Enter base currency: ")
        return base

if __name__ == "__main__":
    x = Exchange()
    x.input_ammount_price()





