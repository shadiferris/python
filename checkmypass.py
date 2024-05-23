import requests
import hashlib

# sha hash generator - https://passwordsgenerator.net/sha1-hash-generator/
# pwned password - https://haveibeenpwned.com/Passwords
# requests library -  https://pypi.org/project/requests/
#hashlib module - https://docs.python.org/3/library/hashlib.html


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching {res.status_code}, check the api and try again ")
    print(res)

def pwned_api_check(password):

    #h = hashlib.new('sha256')
    #h.update(b"password")
    #print(h.hexdigest().upper())

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1password)

request_api_data('CBFDA')

pwned_api_check('password123')
