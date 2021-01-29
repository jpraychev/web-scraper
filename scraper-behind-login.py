import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://localhost:8000/accounts/login/'
PROFILE_URL = 'http://localhost:8000/accounts/profile/'

def login(login_url, data_url):

    with requests.Session() as session:

        # Request login page to retrieve CSRF token and cookies
        r = requests.get(login_url)
        bs = BeautifulSoup(r.text, 'html.parser')
        csrf_token = bs.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']

        # Build credentials
        credentials = {
            'username': '',
            'password': '',
            'csrfmiddlewaretoken': csrf_token
        }

        # Post data to login page
        session.post(login_url, cookies = r.cookies, data = credentials)

        profile = session.get(data_url)

        return profile

if __name__ == '__main__':

    profile_page = login(LOGIN_URL, PROFILE_URL)
    print (profile_page.text)