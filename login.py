import requests
import sys

username = "23TSFBA000"
password = "0000"

base_url = 'http://10.201.21.1'


def logged_in(password_str=-1):
    status_response = requests.get(base_url, allow_redirects=False)

    if status_response.status_code == 302:
        redirect_url = status_response.headers['Location']
        if redirect_url==base_url+"/status":
            return True  # Exit the loop if login and status check are successful
        elif redirect_url==base_url+"/login":
            return False
        else:
            final_response = requests.get(redirect_url)
            print("\n\n\nsomething is wrong!\n\n\n")
            print(redirect_url)
            print(final_response.headers)
            sys.exit(1)


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
magic_url = base_url+'/login'
magic_data = {
    'username': 'STN-'+username,
    'password': password,
    'magic': ''
}
magic_response = requests.post(magic_url, data=magic_data)

if logged_in:
    print("Login Successful.")
else:
    print("Login Failed.")
