import json
import requests

# Get access token from application, provide login credentials.
tokenUrl = 'http://localhost:8000/api/token/'
data={"username": "anjan", "password":"anjan123"}

# Make POSE request to the token url
res = requests.post(tokenUrl,data=data)

# Make dict object from the response
result = json.loads(res.text)

# Obtain access token from the dict object
print(result.get('access'))

# Api end point which needed access token
apiUrl = 'http://localhost:8000/customers'

# Provide access token in the request header.
headers = {}
headers['Authorization'] = 'Bearer '+""+ str(result.get('access'))

# Make api GET call
res = requests.get(apiUrl, headers=headers)
# show api response
print(res.text)

