## webbrowser module comes with python and opens a browser to a specific page
## requests module downloads files and web pages from the internet
## bs4 parses HTML, the format that web pages are written internet
## selenium launches and controls a web browser.  The selenium module is able to fill in forms and simulate mouse clicks in this browser

##### Opening a tab in your default browser
##### Opening a tab in your default browser
##### Opening a tab in your default browser
## import webbrowser 
## webbrowser.open('https://www.nutshell.news/') ## running a script containing just this functioon would open the default browser to the string 


##### Downloading files from the web
##### Downloading files from the web
##### Downloading files from the web
## requests lets you easily download files from the web
## pip install --user requests

#import requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#type(res)
#res.status_code == requests.codes.ok
#len(res.text)
#print(res.text[:250])
## if the requests succeeds, the downloaded webpage is stored as a string in the response object's text variable
## the raise_for_status() is a good way to check details of an error, and ensure a program halts if there's an error
# res = requests.get('https://inventedurl.com/page_that_doesnt_exist')
#res.raise_for_status()


##### Save the data the your harddrive
##### Save the data the your harddrive
##### Save the data the your harddrive
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):  ## itercontent returns chunks that are x bytes large (the number you pass)
    playFile.write(chunk)
playFile.close()

