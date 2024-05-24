import requests
import hashlib

# sha hash generator - https://passwordsgenerator.net/sha1-hash-generator/
# pwned password - https://haveibeenpwned.com/Passwords
# requests library -  https://pypi.org/project/requests/
#hashlib module - https://docs.python.org/3/library/hashlib.html


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching {res.status_code}, check the API and try again")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    #print(hashes)
    for h, count in hashes:
        print(h, count)


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1password[:5]
    tail = sha1password[5:]
    #print(sha1password)
    #print(first5_char) 
    #print(tail)
    response = request_api_data(first5_char)
    #print(first5_char)
    #print(tail)
    #print(response)
    return get_password_leaks_count(response, tail)

#request_api_data('CBFDA')

pwned_api_check('123')
