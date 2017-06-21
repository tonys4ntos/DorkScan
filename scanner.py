"""
Aziz google dork scanner (Exploit tools coming soon!!)
this tool requires python3 and bs4, docopt modules to run
if you dont have the modules already you can install them from your
terminal by typing:
   sudo python3 -m pip install <module name>
if you are on windows:
    pip install <module name>
Usage:
    scanner.py <dork> <number>
    scanner.py (-h | --help for better help)

Arguments:
    <dork> ---> the dork you want to search... exp: inurl:*.php?*=
    <number> the number of pages you want to scan

Options:
   -h, --help ---> show this text

(Bing ip search and reverse domain lookup coming soon!!)
This is still a very basic and simple dork scanner if you face any issues
or have any suggestions please contact me.
Have a nice day!
                               -Aziz
"""
#Just importing the needed modules here
import requests, re #So this line here imports the requests module xD
from docopt import docopt
from bs4 import BeautifulSoup
from time import time as timer

#OK now we are done importing modules
#The next thing to do now is to define our functions lol..

def get_urls(search_string, start):
     #here we defined a function called "get_urls" that takes two arguments: start page and the dork to search
     #empty list to store the urls
     temp = []
     url = 'http://www.google.com/search' #the url used to search
     payload = {'q' : search_string, 'start' : start} #What we need in order to search
     my_headers = {'user-agent' : 'Mozilla/11.0'} #That's our user-agent
     r = requests.get(url, params = payload, headers = my_headers)

     soup = BeautifulSoup(r.text, 'html.parser') #This line will get the results after the request and show the in text
     h3tags = soup.find_all('h3', class_='r')# will filer the urls we need from that text
     for h3 in h3tags:
         try:
             temp.append( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1))
         except:
             continue
     return temp


def main():
    start = timer()
    #Empty list to store the urls
    result = []
    arguments = docopt(__doc__, version='Aziz Google dork scanner V 0.0.1')
    search = arguments['<dork>']
    pages = arguments['<number>']
    #Calling the function  [number] times
    for page in range(0, int(pages)):
        #Getting the urls in the list
        result.extend( get_urls( search, str(page*10)))
    #Adding a line between the results
    result = list( set( result ) )
    print( *result, sep = '\n')
    print( '\nTotal URLs found : %s ' % str(len(result)))
    print( 'the script was running for : %s' % (timer() - start, ))


if __name__ == '__main__':
    main()

#That's it...
