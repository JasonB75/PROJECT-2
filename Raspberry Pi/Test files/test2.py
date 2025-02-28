import requests

# importing the requests library
import requests

# api-endpoint
URL = "http://127.0.0.1:5000/get_data"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'volume':250, "format":"float", "precision":5}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

print(r.json()['output'])