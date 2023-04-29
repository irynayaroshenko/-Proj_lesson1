import requests

city = input("> ")
data = eval(requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e90fab7014064d2c88795d9fd95afa6f").text)
# print(data)
# print(type(data))  # str
# print(eval(data))  # magic method which terns strings into needed data type
# print(data.get(['main']))

# beautiful soup package for work with inet pages
# Crtl + Alt + L - format json text in new file
# print(eval(input('>')))  # the shortest calculator in Python

'''
https://rapidapi.com/hub 
many APIs to learn, watch
'''