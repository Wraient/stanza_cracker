import requests

# base_url = 'http://10.201.21.1'

# Make a GET request to check the connection status
# status_response = requests.get(base_url)
# print(status_response.headers)
# if "http://10.201.21.1/logout" in str(status_response._content):
#     print("YES")
# print(status_response.headers)
# print(status_response.headers)

# Check if the response status code is 200 and parse the JSON data
# if status_response.status_code == 200:
#     response_json = status_response.json()

logout = requests.get('http://10.201.21.1/logout?')
