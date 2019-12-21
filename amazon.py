"""
Name    John Park
Github  john-yohan-park
Date    10/16/2019

System Requirements
    Name:           Command:
    Homebrew        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    Python 3        brew install python
    Requests        pip3 install requests           to send HTTP requests
    Beautiful Soup  pip3 install beautifulsoup4     parsing html files
    Gecko Driver    brew install geckodriver        link between Selenium / Beautiful Soup and Firefox
    Firefox         brew cask install firefox

Program Requirements
    Sender's email needs to be gmail with 2-step verification (google.com/landing/2step)
    Recipient's email
    Google App Password
        - accounts.google.com
        - login with sender's email
    Your User Agent
        - google 'my user agent' and copy & paste result
    URL of desired item from Amazon.com
    Max price you're willing to pay

To run, type into terminal: python3 amazon.py
To exit, press CTRL + C
"""

# import libraries
import  requests
import  smtplib
import  time
from    bs4 import BeautifulSoup

# define variables
sender_email        = 'abc123@gmail.com'
recipient_email     = 'def456@gmail.com'
google_app_password = 'xyz789'
URL                 = 'www... '
userAgent           = {'User-Agent': 'abcd'}
max_price           = 123 # enter XXX or XXX.YY. No commas and dollar signs

def check_price():
    page  = requests.get(URL, headers = userAgent)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id = 'productTitle').get_text().strip()
    price = soup2.find(id = 'priceblock_ourprice').get_text()   # str $1,998.00
    price = price.replace('$', '').replace(',', '')             # remove $ and ,
    float_price = float(price)                                  # convert str to float
    str_price = '{:.2f}'.format(round(float_price, 2))          # round to nearest cent

    if(float_price <= max_price): send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)    # TLS encryption port
    server.ehlo()       # establish connection with email server
    server.starttls()   # create secure connection
    server.ehlo()       # re-establish connection
    server.login(sender_email, google_app_password)

    subject = "This item meets your desired price point $" + str(max_price)
    body = 'Visit ' + URL
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(sender_email, recipient_email, msg)
    print('Email has been sent')
    server.quit()

while(True):
    check_price()
    time.sleep(3600)   # check every hour
