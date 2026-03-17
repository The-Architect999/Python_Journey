import pprint #make things preety print
import requests
from bs4 import BeautifulSoup
#think of this as the browser,
#this is also what chrome does to load the browser
res = requests.get(f'https://news.ycombinator.com/')
#gets an envelope that includes all the contents of 
#the html file on the website

"""to work on a while loop and generator that 
keeps pulling data from the site for practice"""

'''pipeline: to learn: scrapy framework (just like a language)'''

#parse it - convert it from a string to something we can use
soup = BeautifulSoup(res.text, 'html.parser')
#(beautifulsoup also works with xml)
#using css selector (to learn)

#will return a list for both the link and votes 
#in the order that they are in
#got timeline and score from inspecting webpage
#.select uses css selectors to instanciate object from the class on html
# The '>' means "find the 'a' tag that is a direct child of 'titleline'"
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

#sorting the list
def sort_by_votes(hnlist):
    return sorted(hnlist, key = lambda k: k['votes'], reverse=True)

def custom_news(links, subtext):
    hn = []
    # enumerate gives (index, item)
    # we use it to grab title and link at same index
    for idx, item in enumerate(links):

        title = links[idx].getText() #links is an object of beautifulsoup 
        #Now that you have the object, getText() is the tool that 
        #reaches inside and pulls out only the human-readable string
        #.get to get the attribute
        href = links[idx].get('href', None)
        #can use item instead of links[idx] in the for loop
        #as it just returns the item at index as links is a list
        
        #select score class in subtext
        vote = subtext[idx].select('.score')
        #if len of vote is > 0 - it is a list
        #skips number if .score doesn't exist
        if len(vote):
            #get the readable text, replace points with nothing 
            #and convert to int so we can use it
            points = int(vote[0].getText().replace(' points', ''))

            #create a list of dicts if points 99+
            if points > 150:
                hn.append({'Title': title, "Link": href, 'votes': points})
    return sort_by_votes(hn)

# pprint.pprint(custom_news(links, subtext))

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()
email['from'] = 'pyhtonscripterbot@gmail.com'
email['to'] = 'x.com'
email['subject'] = 'filtered articles for today: 150+ points'

#news data first
news_data = custom_news(links, subtext)

#Convert that list into a readable string
# We use a join or a loop to make it look like a list
body_text = "Here is your High-Value Intel:\n\n"
for item in news_data:
    body_text += f"TITLE: {item['Title']}\nLINK: {item['Link']}\nVOTES: {item['votes']}\n"
    body_text += "-"*30 + "\n"

# 3. Set the content
email.set_content(body_text)

# 4. Connect to the RIGHT host
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo_or_helo_if_needed()
    smtp.starttls()
    smtp.login('pyhtonscripterbot@gmail.com', 'hola git bot, we meet again') 
    smtp.send_message(email)
    print('Done, my liege!')