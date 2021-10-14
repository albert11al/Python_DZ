from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

my_list_money = content.split("<Valute")
def currency_rates(self):
    for i in my_list_money:
        if self.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(',', '.'))


print(currency_rates(input('Input currency: ')))
