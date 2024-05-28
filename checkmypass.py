import requests
import hashlib
import sys

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
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0


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

#pwned_api_check('123')
def main():
    password = input("Enter a password to check if it has been pwned: ")
    count = pwned_api_check(password)
    if count:
        print(f"The password '{password}' has been found {count} times... you should probably change it!")
    else:
        print(f"The password '{password}' was NOT found. Carry on!")
if __name__ == "__main__":
    main()

# can be executed using the following method:
# --> python3 checkmypass.py
# input will check password strength one at a time