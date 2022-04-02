import requests, bs4

## Request a url, check for errors, define a string of the html
res = requests.get('https://nostarch.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
# print(soup)


## the html.parser module comes with python, but lxml is faster
## pip install --user lxml

## beautiful soup has different selector methods
# soup.select('div') # all elements named div
# soup.select('#author') # the element with an id attribute of author
# soup.select('.notice') # all elements that use a CSS classNAme 'notice'
# soup.select('div span') # all elements named <span> that are within an element named <div>
# soup.select('div > span') # all span elements directly within divs, with no elements in between
# soup.select('input[name]') # all elements named input that have a name attribute with any value
# soup.select('input[type='button']') # all input elments with an attribute named type with value button
## soup.select('p #author') selects all <p> elements with id author

#print(soup.select('.leaf'))
elems = soup.select('.leaf')
print(elems[0])
print(elems[0].getText()) ## returns a string of the inside text
print(elems[0].attrs) ## prints related attributes
