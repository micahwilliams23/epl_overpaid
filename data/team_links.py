from bs4 import BeautifulSoup as soup
import requests as req

list_url = 'https://www.spotrac.com/epl/'

page_html = req.get(list_url).content

page_soup = soup(page_html, 'html.parser')

team_links = page_soup.findAll('div',{'class':'teamname'})

with open('team_links.txt', 'w') as f:
    for item in team_links:
        f.write(item.a['href']+'\n')