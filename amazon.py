"""
Name    John Park
Github  john-yohan-park
Date    10/16/2019

Introduction
    Checks hourly to see if an item from Amazon.com meets a pre-defined pricepoint
    If so, sends an email to the user

System Requirements
    Name:           Command:
    Homebrew        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    Python 3        brew install python
    Requests        pip3 install requests           sends HTTP requests
    Beautiful Soup  pip3 install beautifulsoup4     parsing html files
    Gecko Driver    brew install geckodriver        links Beautiful Soup and Firefox
    Firefox         brew cask install firefox       browser from which email is sent

Program Requirements
    Sender's email needs to be gmail with 2-step verification (google.com/landing/2step)
    Recipient's email
    Google App Password
        - login with sender's email
        - follow the instructions here(https://support.google.com/mail/?p=InvalidSecondFactor)
    Your User Agent
        - google 'my user agent' and copy & paste result
    URL of desired item from Amazon
    Max price you're willing to pay

To run, type into terminal: python3 amazon.py
To exit, press CTRL + C
"""

# import libraries
import requests
import smtplib
import time
from   bs4 import BeautifulSoup

# initialize local variables whose scope exist only within this program file 'amazon.py'
sender_email        = 'annie.xiu.lam@gmail.com' # email password: beyonce365
google_app_password = 'tykgzchypgcbrurh'        # not email password. It should be a 16-character password google generates for you
recipient_email     = 'john.vegan.park@gmail.com'
URL                 = 'https://www.amazon.com/AbergBest-Rechargeable-Digital-Students-cameras/dp/B078YR3MNK/ref=sr_1_1?keywords=camera&qid=1576992299&sr=8-1'
userAgent           = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
max_price           = 45  # enter XXX or XXX.YY. No commas and dollar signs

# check_price function
def check_price():
    page  = requests.get(URL, headers = userAgent)         # using the URL, get page
    soup1 = BeautifulSoup(page.content, 'html.parser')     # scrape the page's HTML contents
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser') # do it again, so we can format its contents
                                                           # we have to parse its HTML contents 2X because
                                                           # Amazon.com generates its HTML pages automatically
    #print(soup2)       # uncomment this line if you want to see extracted HTML contents
    global title
    title = soup2.find(id = 'productTitle').get_text().strip()  # scrape product title from parsed HTML contents
    price = soup2.find(id = 'priceblock_ourprice').get_text()   # scrape product price
    price = price.replace('$', '').replace(',', '')             # remove $ and ,
    float_price = float(price)                                  # convert str to float
    #str_price = '{:.2f}'.format(round(float_price, 2))         # round to nearest cent
    global emailHasBeenSent
    emailHasBeenSent = False

    if(float_price <= max_price): 
        send_email()
        emailHasBeenSent = True

# send_email function
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)    # TLS encryption port
    server.ehlo()       # establish connection with email server
    server.starttls()   # create secure connection
    server.ehlo()       # re-establish connection
    server.login(sender_email, google_app_password)

    subject = "This item meets your desired price point of $" + str(max_price)
    body = 'Interested in buying ' + title + '?\n\nVisit ' + URL
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(sender_email, recipient_email, msg)
    print('Email has been sent')
    server.quit()

# main function
while(True):           # infinite loop
    check_price()
    if(emailHasBeenSent): break
    time.sleep(3600)   # check every hour
