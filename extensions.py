import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: int):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote != keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту: {quote}{KeyError}')

        try:
            base != keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту: {base}{KeyError}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}{ValueError}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base * amount
