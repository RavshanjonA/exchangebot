import requests
from pprint import pprint as print

API_KEY  = '3ce4d7b84e64c4d2965a370e'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

r = requests.get(url)
res = r.json()
print(f"Bugungi kurs 1 AQSH dollari {res['conversion_rate']} so'm")
