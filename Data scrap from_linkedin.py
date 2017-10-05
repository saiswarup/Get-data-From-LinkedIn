from BeautifulSoup import BeautifulSoup
import requests
import re
client = requests.Session()
HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html)
csrf = soup.find(id="loginCsrfParam-login")['value']
login_information = {
    'session_key':'Your email id For LinkedIN',
    'session_password':'Your Password',
    'loginCsrfParam': csrf,
}
client.post(LOGIN_URL, data=login_information)
response = client.get('https://www.linkedin.com/feed/')
raw_data = response.text
email = re.findall('Email: (.*?)&.*', raw_data)
if email:
    email = email[0]
else:
    email = "Doesn't Exist"
first_name = re.findall('firstName&quot;:&quot;(.*?)&quot;', raw_data)
last_name = re.findall('lastName&quot;:&quot;(.*?)&quot;', raw_data)
if not first_name:
    first_name = ['']
if not last_name:
    last_name = ['']
feed_names = re.findall('publicIdentifier&quot;:&quot;(.*?)&quot;', raw_data)
names = zip(first_name, last_name)
for i in names:
    print i[0], i[1]
