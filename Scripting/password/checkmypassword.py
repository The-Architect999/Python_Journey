import requests
# allows requests like a browser - browser without an actual browser
import hashlib
#builtin module for hash
import sys
#def1 - comminucates with the api - gives it the 5 chars and the api returns a list of the tail of every 
# hashed password that matches
def request_api_data (quer_char):
    url = "https://api.pwnedpasswords.com/range/" + quer_char
    res = requests.get(url)
    print(res.text)
    if res.status_code != 200: #if the server isn't working
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and tr again!')
    return res #envelope with the package - tells the system - package delivered status code [200]

def get_leak_count(hashes, hash_to_check):
    #takes the envelope
    #comprehension: .text - returns the text in the envelope - hashed passwords
    #.splitlines() returns the lines seperately with the for loop
    #.split splits the hashed passwords, example: FFD7087991CE11EC76B58AB18EC0EA7F568:384 - 
    hashes = (line.split(':') for line in hashes.text.splitlines()) #returns tuples of (tail, count)
    for h,count in hashes:
        # if tail == our input tail, return count
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #need to encode in order to convert to hash object
    #then we can convert hash object to hash
    sha1 = hashlib.sha1(password.encode('utf8')).hexdigest().upper() #api demands uppercase
    #split first 5 and the rest
    first_5, tail = sha1[:5], sha1[5:]
    #run def with arg first 5 chars of passwords
    response = request_api_data(first_5) #returns all the passwords from the api in an envelope
    return get_leak_count(response, tail) #finally for the check

def main(args):
    #passwords from terminal
    for password in args:
        count = pwned_api_check(password)
        #after all the operations above, returns count of leaks
        if count:
            print(f'{password} was found {count} times, you should change it!')
        else: #0/Flase
            print(f"{password} not found, you're good!")
    print('Pwned Test complete!') #work done
    return 0 #tells the terminal - code executed with no errors

#run if i run this file
if __name__ == '__main__':
    # exit after running main
    sys.exit(main(sys.argv[1:]))
