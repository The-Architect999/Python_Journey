from bs4 import BeautifulSoup
import requests
req = requests.get('https://remoteok.com/remote-python-jobs')
# req - envelope

#parsing - converting to usable
soup = BeautifulSoup(req.text, 'html.parser')








