import requests

#print(requests.__version__)

r = requests.get('https://raw.githubusercontent.com/apollo-online/404lab1/main/printversion.py')
print(r.content)