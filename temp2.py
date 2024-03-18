
import requests
url = "http://10.201.21.1"
response = requests.get(url, allow_redirects=False)

if response.status_code == 302:
    redirect_url = response.headers['Location']
    final_response = requests.get(redirect_url)
    print('redirected! to: ', redirect_url)
    print(final_response.headers)
else:
    print("No redirect")
    print(response.headers)