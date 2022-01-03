# on the console:
# > pip install requests
# > pip list

import requests

response = requests.get("https://google.com/")
print(response) # should produce -> <Response [200]>