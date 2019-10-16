# Amazon_Price_Checker
Checks price of an item on Amazon every hour. Sends email if price drops to desired price proint. 

Written in Python. Powered by Beautiful Soup. Uses TLS Server Encryption.

System Requirements
To run this program, you will need
    Name:           Mac Terminal Command to Download:
    Homebrew        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    Python 3        brew install python
    Requests        pip3 install requests
    Beautiful Soup  pip3 install beautifulsoup4
    Gecko Driver    brew install geckodriver
    Firefox         brew cask install firefox

Program Requirements
To run this program, you will need to define
    Sender's email
        - Needs to be gmail with 2-step verification (visit google.com/landing/2step)
    Recipient's email
    Google App Password
        - visit accounts.google.com and log-in with sender's email
    Your User Agent
        - Google 'my user agent' and copy & paste top result
    URL of the desired item from Amazon.com
    Desired price point for the item
