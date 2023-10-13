import requests
from requests import Session
import secrets
from pprint import pprint as pp



# Test a basic Request
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
# headers = { 'Accepts': 'application/json','X-CMC_PRO_API_KEY': secrets.API_KEY, }
# r = requests.get(url, headers=headers) 


# Build up a class so we can easily make the REST API calls
class CMC:
    # https://coinmarketcap.com/api/documentation/v1/#
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = { 'Accepts': 'application/json','X-CMC_PRO_API_KEY': token, }
        self.session = Session()
        self.session.headers.update(self.headers)
    
    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getPrice(self, symbol):
        url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
        # create the dictionary object that will allow for the "symbol" choice to work 
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data
        
cmc = CMC(secrets.API_KEY)
pp(cmc.getPrice('BTC'))