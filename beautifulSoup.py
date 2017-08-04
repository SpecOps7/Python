from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://skiplagged.com/flights/DFW/BOS/2017-07-14/2017-07-16'

#opening up connection, grabbing the page
uClient = uReq(my_url)
#off load contents into a variable
page_html = uClient.read()
#close the connection
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
# grabs all prices
prices = page_soup.findAll("div", {"class":"span2 trip-cost text-success"})

prices
