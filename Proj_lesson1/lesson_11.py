import requests
import pprint

# resp = requests.get('https://api.monobank.ua/bank/currency')
# print(resp)
# print(resp.status_code)
# print(resp.headers)
#
# cont_type = resp.headers['Content-Type']
# print(cont_type)
# js_resp = resp.json()
# print(js_resp)
#
# my_currencies = {
#     980: '🇺🇦',
#     840: '🇺🇸',
#     978: "🇪🇺",
# }
#
# my_rates = []
# for obj in resp.json():
#     if obj['currencyCodeA'] in my_currencies:
#         my_rates.append(obj)
#
# print(my_rates)

# gif_for_word = input('Print a word - I find GIFs: > ')
# resp = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=4hBaD17Isr71fBi1P9cEKoNpwM7wk9Fj&q={gif_for_word}&limit=25&offset=0&rating=g&lang=en')
#
# print(resp)
# stat_code = resp.status_code
# print(stat_code)

# js_resp = resp.json()
# gif_link = js_resp['data'][0]['images']['downsized_medium']['url']
#
# for i in range(len(js_resp['data'])):
#     print(f"gif {i + 1}: {js_resp['data'][i]['images']['downsized_medium']['url']}")


# import requests
#
API_KEY = "4hBaD17Isr71fBi1P9cEKoNpwM7wk9Fj"
API_URL = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}"

def search_gifs(query, limit=25, offset=0, rating="g", lang="en"):
    try:
        resp = requests.get(f"{API_URL}&q={query}&limit={limit}&offset={offset}&rating={rating}&lang={lang}")
        resp.raise_for_status()
        data = resp.json()["data"]
        return [gif["images"]["downsized_medium"]["url"] for gif in data]
    except (requests.exceptions.RequestException, KeyError, requests.exceptions.HTTPError) as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    query = input("Enter a word to search for GIFs: ")
    gifs = search_gifs(query)
    for i, url in enumerate(gifs, start=1):
        print(f"GIF {i}: {url}")
